from flask import Flask
from flask_cors import CORS
from database import db
import models
from routes.especes_routes import especes_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///especes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
CORS(app)
app.register_blueprint(especes_bp)

@app.route("/")
def home():
    return {"test":"API OK"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)