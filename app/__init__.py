from flask import Flask

app = Flask(__name__)
app.secret_key = 'rickrolled'

app.app_context().push()

from app import views
