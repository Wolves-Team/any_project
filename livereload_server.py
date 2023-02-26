from livereload import Server
from src import create_app

app = create_app()
app.debug = True

def main():
  print("Start server with livereload")
  server = Server(app.wsgi_app)

  server.watch('src/templates/*.html.jinja', 'echo Template is changed.')
  server.watch('src/static/*.css', 'echo Style is changed.')

  server.serve()

if __name__ == "__main__":
  main()
