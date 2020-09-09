from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(config.StagingConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def not_found(error):
    return '404', 404

from src.controllers import flaskpoc

app.register_blueprint(flaskpoc)
db.create_all()