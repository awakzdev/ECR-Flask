from flask import jsonify, Flask
import socket
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    return jsonify({'IP Address': ip_addr})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
