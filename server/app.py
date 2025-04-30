from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import the shared database instance
from db import db

def create_app():
    app = Flask(__name__)

    # configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)
    
    # Register Blueprints
    from routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    # create database tables
    with app.app_context():
        db.create_all()

    return app



# from flask import Flask, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# import os
# from dotenv import load_dotenv
# load_dotenv(dotenv_path="/app/.env")

# app = Flask(__name__)

# # Enable CORS (Cross-Origin Resource Sharing)
# CORS(app)

# # Set up the database configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#     "DATABASE_URL",
#     "postgresql://postgres:password@db:5432/mydatabase"
# )

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize SQLAlchemy
# db = SQLAlchemy(app)

# # Define a simple User model for the database
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))

# @app.route("/api/hello")
# def hello():
#     return jsonify(message="Hello from Flask!")

# @app.route('/create-user')
# def create_user():
#     # Create a new user and save to the database
#     user = User(name='Alice')
#     db.session.add(user)
#     db.session.commit()
#     return "User created!"

# # Create the tables in the database
# with app.app_context():
#   db.create_all()

# # Run the app on 0.0.0.0 to make it accessible externally
# app.run(debug=True, host="0.0.0.0", port=5000)
