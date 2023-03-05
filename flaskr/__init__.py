from flask import Flask, render_template

from flaskr.routes.index import index_bp

import toml

def create_app():
  app = Flask(__name__ , instance_relative_config=True)
  app.config.from_file("defaultConfig.toml", load=toml.load)

  app.register_blueprint(index_bp)

  app.logger.info("APPLICATION => " + app.config["APP_NAME"])
  app.logger.info("ENVIRONMENT => " + app.config["ENV"])

  return app
