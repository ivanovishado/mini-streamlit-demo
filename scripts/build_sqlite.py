from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.streamlit_course.data_utils import load_bitcoin_data

CSV_PATH = ROOT / "data" / "btc_diario_limpio.csv"
DB_PATH = ROOT / "data" / "bitcoin.db"
TABLE_NAME = "bitcoin_daily"


def rebuild_database(csv_path: Path = CSV_PATH, db_path: Path = DB_PATH) -> int:
    data = load_bitcoin_data(csv_path).drop(columns=["Month_Name"])
    data = data.copy()
    data["Date"] = data["Date"].dt.strftime("%Y-%m-%d")

    with sqlite3.connect(db_path) as connection:
        data.to_sql(TABLE_NAME, connection, if_exists="replace", index=False)

    return len(data)


if __name__ == "__main__":
    rows = rebuild_database()
    print(f"Rebuilt {DB_PATH} with {rows:,} rows in {TABLE_NAME}.")
