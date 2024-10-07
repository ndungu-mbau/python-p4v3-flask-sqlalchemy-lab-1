# server/app.py
#!/usr/bin/env python3
import os
from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)

db_path = os.path.join(os.path.dirname(__file__), 'instance', 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def earthquake(id):
    data = Earthquake.query.filter(Earthquake.id == id).first()
    if data:
        response = data.to_dict()
        status = 200
    else:
        response = {'message': f'Earthquake {id} not found.'}
        status = 404

    return make_response(response, status)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
