from flask import Flask, render_template, request, jsonify


#initiaze app
app = Flask(__name__)
#GET API
@app.route("/")
def home():
    # return "hello sanaan"
    users = [{'id': 1, 'username': 'Alice'}, {'id': 2, 'username': 'Bob'}]
    return jsonify({'result':users,'message':'fetched user data successfully'})


if __name__ == '__main__':
    app.run(debug=True, port=5005)
    