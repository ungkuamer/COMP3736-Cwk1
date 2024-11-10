from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'rickrolled'

app.app_context().push()

from app import views