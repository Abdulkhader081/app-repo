from app import app

def test_healthz():
    with app.test_client() as c:
        rv = c.get('/healthz')
        assert rv.status_code == 200
        # Check for key content in the HTML response
        assert b"Md Abdul Khader" in rv.data
        assert b"DevOps Engineer" in rv.data
        assert b"abdulkhadermd13@gmail.com" in rv.data
        assert b"GitHub" in rv.data
        assert b"Professional Summary" in rv.data
        assert b"Education" in rv.data
