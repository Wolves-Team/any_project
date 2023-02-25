from flask import Flask, render_template

from src.routes.index import index_bp

def create_app():
  app = Flask(__name__ , instance_relative_config=True)

  app.register_blueprint(index_bp)

  return app
