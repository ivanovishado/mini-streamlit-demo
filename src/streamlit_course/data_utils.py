from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "student_id",
    "programa",
    "semestre",
    "horas_estudio",
    "asistencia_pct",
    "proyecto_ai",
    "calificacion",
    "uso_pandas",
    "estado",
}


def load_students(path: str | Path) -> pd.DataFrame:
    data = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        missing_columns = ", ".join(sorted(missing))
        raise ValueError(f"Faltan columnas requeridas: {missing_columns}")
    return data


def filter_students(
    data: pd.DataFrame,
    min_grade: int,
    program: str = "Todos",
    pandas_level: str = "Todos",
) -> pd.DataFrame:
    filtered = data[data["calificacion"] >= min_grade]

    if program != "Todos":
        filtered = filtered[filtered["programa"] == program]

    if pandas_level != "Todos":
        filtered = filtered[filtered["uso_pandas"] == pandas_level]

    return filtered.sort_values("calificacion", ascending=False)


def summarize_students(data: pd.DataFrame) -> dict[str, float | int]:
    return {
        "students": int(len(data)),
        "average_grade": round(float(data["calificacion"].mean()), 1) if len(data) else 0,
        "average_attendance": round(float(data["asistencia_pct"].mean()), 1) if len(data) else 0,
        "at_risk": int((data["estado"] == "En riesgo").sum()),
    }
