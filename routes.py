from flask import Blueprint, request, jsonify, abort
from .services import create_user, authenticate_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        abort(400)
    create_user(username, password)
    return jsonify({'message': 'User created successfully'}), 201

@main_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = authenticate_user(username, password)
    if user:
        return jsonify({'message': 'Login successful'})
    else:
        abort(401)
