# manage.py

from flask.cli import FlaskGroup
from project import app

# creating a new FlaskGroup instance to extend the normal CLI with commands related to the Flask App.
cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()

