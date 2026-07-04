"""
Lightweight CI smoke test that does NOT require MongoDB.
Verifies the Flask app object exists and the app is importable/configurable.
"""
import os

# Provide dummy env vars so app.py imports cleanly without a real DB..!
os.environ.setdefault("MONGO_URI", "mongodb://localhost:27017/ci_dummy")
os.environ.setdefault("SECRET_KEY", "ci-test-secret")


def test_app_imports():
    import app as application
    assert application.app is not None


def test_app_is_flask():
    from app import app
    assert app.name == "app"


def test_add_route_registered():
    from app import app
    rules = [r.rule for r in app.url_map.iter_rules()]
    assert "/" in rules
    assert "/add" in rules
