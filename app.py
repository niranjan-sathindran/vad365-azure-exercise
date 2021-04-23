from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! This is a Github actoins demo."

@app.route("/bonus", methods = ['POST'])
def bonus():
    return "You have completed the bonus exercise as well!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
