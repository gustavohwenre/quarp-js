from flask import Blueprint, jsonify
from .decorators import log_event

main_routes = Blueprint("main", __name__)

@main_routes.route("/")
@log_event("INFO")
def index():
    return jsonify({"message": "API da Pizzaria está rodando!"})
