from flask import Flask
from flask.globals import app_ctx
from sqlalchemy.testing.config import db_url
from users.models import db
from blue_prints.bp_users import player_bp


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#init database
# with app.app_context():
#     db.create_all()

# initialize blueprints here
app.register_blueprint(player_bp)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
