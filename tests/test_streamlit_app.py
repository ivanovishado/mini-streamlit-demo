from streamlit.testing.v1 import AppTest


def test_main_app_smoke():
    app = AppTest.from_file("streamlit_app.py")
    app.run(timeout=10)

    assert not app.exception
