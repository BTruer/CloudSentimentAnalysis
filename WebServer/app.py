from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "test"

#take in a string and return the twitter data
@app.route("/search", methods=['POST'])
def search():
    data = request.args
    return str(data)

if __name__ == '__main__':
    app.run(debug=True)
