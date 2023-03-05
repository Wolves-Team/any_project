from livereload import Server
from flaskr import create_app

app = create_app()

def main():
  print("Start server with livereload")
  server = Server(app.wsgi_app)

  server.watch('flaskr/templates/*.html.jinja', 'echo Template is changed.')
  server.watch('flaskr/static/*.css', 'echo Style is changed.')

  server.serve()

if __name__ == "__main__":
  main()
