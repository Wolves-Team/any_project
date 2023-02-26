from flask import Blueprint
from werkzeug import NotFound

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(NotFound)
def handle_not_found():
  return "404 Error"

@error_bp.app_errorhandler(Exception)
def handle_generic_exception():
  return "500 Error"