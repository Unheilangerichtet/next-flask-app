from flask import Blueprint, request, jsonify
from services.user_service import create_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = create_user(data['name'])
    return jsonify(id=user.id, name=user.name)

@user_bp.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello from Flask!")