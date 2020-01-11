# project/tests/conftest.py

#Fixtures are reusable objects for tests. They have a scope which indicates how often the fixture is invoked. 
import pytest

from project import app, db

@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        yield app # testing takes place here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db # testing takes place here
    db.session.remove()
    db.drop_all()

