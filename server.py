from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class CustomHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/':
      self.path = '/public/index.html'

    try:
      file_path = os.getcwd() + self.path
      if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
          self.send_response(200)
          self.send_header('Content-type','text/html')
          self.end_headers()
          self.wfile.write(file.read())  
      
      else :
        self.send_error(404,f"Not Found")

    except Exception as e:
      self.send_error(500,f"server Error: {str(e)}")

def run(server_class = HTTPServer, handler_class = CustomHandler, port = 8080):
  server_adress = ('',port)
  httpd = server_class(server_adress,handler_class)
  print(f"Starting server on port {port}")
  httpd.serve_forever()

if __name__ == "__main__":
  run()