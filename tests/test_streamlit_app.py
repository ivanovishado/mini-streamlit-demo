from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "streamlit_app.py"


def test_main_app_smoke():
    app = AppTest.from_file(str(APP_PATH))
    app.run(timeout=10)

    assert not app.exception


def test_main_app_does_not_include_ia_bonus():
    source = APP_PATH.read_text()

    assert "Bonus IA" not in source
    assert "render_bonus_ai" not in source
