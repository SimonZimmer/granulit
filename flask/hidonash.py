from app import db
from app.models import User, Content
from app import create_app

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Content': Content}
