# manage.py

import sys

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

# creating a new FlaskGroup instance to extend the normal CLI with commands related to the Flask App.
app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    
if __name__ == '__main__':
    cli()

