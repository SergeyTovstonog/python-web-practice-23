from http.server import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Environment, FileSystemLoader, select_autoescape
from urllib.parse import parse_qs

# Set up Jinja environment
env = Environment(
    loader=FileSystemLoader('templates'),  # Directory where your HTML templates are stored
    autoescape=select_autoescape(['html', 'xml'])
)

# Define the handler for HTTP requests
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':  # Root URL
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Load template and render it with Jinja
            template = env.get_template('post_form.html')
            rendered_template = template.render(name="World")  # Passing 'name' variable to the template

            self.wfile.write(rendered_template.encode())
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        if self.path == '/post':  # Handle POST request
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')

            # Parse POST data
            data_dict = parse_qs(post_data)
            arguments = data_dict.get('arguments', [])

            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Load template and render it with Jinja
            template = env.get_template('post.html')
            rendered_template = template.render(arguments=arguments)

            self.wfile.write(rendered_template.encode())
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

# Define main function to start the server
def main():
    try:
        # Create server object
        server = HTTPServer(('localhost', 8000), RequestHandler)
        print('Server started on http://localhost:8000')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the server')
        server.socket.close()

if __name__ == '__main__':
    main()
