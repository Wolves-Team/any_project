from src import create_app

app = create_app()

@app.route("/", methods=["GET"])
def index():
  return "index"

if __name__ == "__main__":
  app.run(host="127.0.0.1")