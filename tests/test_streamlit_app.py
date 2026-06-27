from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "streamlit_app.py"


def test_main_app_smoke():
    app = AppTest.from_file(str(APP_PATH))
    app.run(timeout=10)

    assert not app.exception


def test_main_app_includes_advanced_pages():
    source = APP_PATH.read_text()

    assert "render_sqlite_dashboard" in source
    assert "render_openrouter_chat" in source
    assert "render_upload_state" in source
