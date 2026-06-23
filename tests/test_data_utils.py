from datetime import date
from pathlib import Path

import pandas as pd
import pytest

from src.streamlit_course.data_utils import filter_bitcoin_data, load_bitcoin_data, summarize_bitcoin_data


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "btc_diario_limpio.csv"


def test_load_bitcoin_data_reads_expected_columns():
    data = load_bitcoin_data(DATA_PATH)

    assert "Close" in data.columns
    assert "Daily_Return" in data.columns
    assert "Month_Name" in data.columns
    assert len(data) == 5285


def test_load_bitcoin_data_rejects_missing_columns(tmp_path):
    path = tmp_path / "bad.csv"
    pd.DataFrame({"Date": ["2024-01-01"]}).to_csv(path, index=False)

    with pytest.raises(ValueError, match="Faltan columnas requeridas"):
        load_bitcoin_data(path)


def test_load_bitcoin_data_parses_dates_and_sorts():
    data = load_bitcoin_data(DATA_PATH)

    assert pd.api.types.is_datetime64_any_dtype(data["Date"])
    assert data["Date"].is_monotonic_increasing


def test_load_bitcoin_data_accepts_first_missing_daily_return():
    data = load_bitcoin_data(DATA_PATH)

    assert data["Daily_Return"].isna().sum() == 1
    assert pd.isna(data.iloc[0]["Daily_Return"])


def test_filter_bitcoin_data_applies_date_year_and_month():
    data = load_bitcoin_data(DATA_PATH)

    filtered = filter_bitcoin_data(
        data,
        start_date=date(2020, 1, 1),
        end_date=date(2021, 12, 31),
        years=[2021],
        months=[1, 2],
    )

    assert set(filtered["Year"].unique()) == {2021}
    assert set(filtered["Month"].unique()).issubset({1, 2})
    assert filtered["Date"].min() >= pd.Timestamp("2021-01-01")
    assert filtered["Date"].max() <= pd.Timestamp("2021-02-28")


def test_summarize_bitcoin_data_handles_empty_data():
    data = load_bitcoin_data(DATA_PATH)
    summary = summarize_bitcoin_data(data.iloc[0:0])

    assert summary == {
        "days": 0,
        "latest_close": 0,
        "max_close": 0,
        "average_return": 0,
        "volatility": 0,
        "total_volume": 0,
    }
