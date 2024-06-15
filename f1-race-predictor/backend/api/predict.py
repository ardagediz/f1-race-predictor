import json
import joblib
from http.server import BaseHTTPRequestHandler

# Load the trained model
model = joblib.load('api/model/random_forest_model.joblib')

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        feature1 = data.get('feature1')
        feature2 = data.get('feature2')
        feature3 = data.get('feature3')

        # Perform prediction
        prediction = model.predict([[feature1, feature2, feature3]])

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'prediction': prediction[0]}).encode())

def main():
    from http.server import HTTPServer
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, handler)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
