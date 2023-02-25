from flask import Blueprint

index_bp = Blueprint("/", __name__)

@index_bp.route("/", methods=["GET"])
def index():
  return "index"
