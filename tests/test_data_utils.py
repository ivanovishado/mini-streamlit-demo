from pathlib import Path

import pandas as pd
import pytest

from src.streamlit_course.data_utils import filter_students, load_students, summarize_students


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "estudiantes_ai.csv"


def test_load_students_reads_expected_columns():
    data = load_students(DATA_PATH)

    assert "calificacion" in data.columns
    assert "programa" in data.columns
    assert len(data) == 20


def test_load_students_rejects_missing_columns(tmp_path):
    path = tmp_path / "bad.csv"
    pd.DataFrame({"student_id": [1]}).to_csv(path, index=False)

    with pytest.raises(ValueError, match="Faltan columnas requeridas"):
        load_students(path)


def test_filter_students_applies_grade_program_and_pandas_level():
    data = load_students(DATA_PATH)

    filtered = filter_students(
        data,
        min_grade=90,
        program="Datos",
        pandas_level="Avanzado",
    )

    assert list(filtered["programa"].unique()) == ["Datos"]
    assert list(filtered["uso_pandas"].unique()) == ["Avanzado"]
    assert filtered["calificacion"].min() >= 90


def test_summarize_students_handles_empty_data():
    data = load_students(DATA_PATH)
    summary = summarize_students(data.iloc[0:0])

    assert summary == {
        "students": 0,
        "average_grade": 0,
        "average_attendance": 0,
        "at_risk": 0,
    }
