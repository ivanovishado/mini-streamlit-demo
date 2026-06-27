from datetime import date
from pathlib import Path
from typing import Iterable

import pandas as pd


REQUIRED_COLUMNS = {
    "Date",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Year",
    "Month",
    "Daily_Return",
}


MONTH_NAMES = {
    1: "Ene",
    2: "Feb",
    3: "Mar",
    4: "Abr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dic",
}


def prepare_bitcoin_data(data: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        missing_columns = ", ".join(sorted(missing))
        raise ValueError(f"Faltan columnas requeridas: {missing_columns}")

    data = data.copy()
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.sort_values("Date").reset_index(drop=True)
    data["Month_Name"] = data["Month"].map(MONTH_NAMES)
    return data


def load_bitcoin_data(path: str | Path) -> pd.DataFrame:
    return prepare_bitcoin_data(pd.read_csv(path))


def filter_bitcoin_data(
    data: pd.DataFrame,
    start_date: date,
    end_date: date,
    years: Iterable[int] | None = None,
    months: Iterable[int] | None = None,
) -> pd.DataFrame:
    start = pd.Timestamp(start_date)
    end = pd.Timestamp(end_date)
    filtered = data[(data["Date"] >= start) & (data["Date"] <= end)]

    selected_years = list(years or [])
    if selected_years:
        filtered = filtered[filtered["Year"].isin(selected_years)]

    selected_months = list(months or [])
    if selected_months:
        filtered = filtered[filtered["Month"].isin(selected_months)]

    return filtered.sort_values("Date").reset_index(drop=True)


def summarize_bitcoin_data(data: pd.DataFrame) -> dict[str, float | int]:
    if data.empty:
        return {
            "days": 0,
            "latest_close": 0,
            "max_close": 0,
            "average_return": 0,
            "volatility": 0,
            "total_volume": 0,
        }

    return {
        "days": int(len(data)),
        "latest_close": round(float(data.iloc[-1]["Close"]), 2),
        "max_close": round(float(data["Close"].max()), 2),
        "average_return": round(float(data["Daily_Return"].mean()), 3),
        "volatility": round(float(data["Daily_Return"].std()), 3),
        "total_volume": round(float(data["Volume"].sum()), 2),
    }
