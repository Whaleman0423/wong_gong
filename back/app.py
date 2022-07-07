from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path="", static_folder="templates")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/ping', methods=["GET"])
def ping():
    return 'pong'

@app.route('/post', methods=["POST"])
@cross_origin()
def post_data():
    data = request.get_json()
    name = data["name"]
    phone = data["phone"]
    numOfTicket = data["numOfTicket"]
    email = data["email"]
    print("name" + name)
    print("phone" + phone)
    print("numOfTicket" + numOfTicket)
    print("email" + email)
    return f"got user data, name= {name},phone= {phone}, numOfTicket={numOfTicket}, email={email}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)