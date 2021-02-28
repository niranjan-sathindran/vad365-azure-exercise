from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Congratulations! You have completed the Azure Application Architecture and Deployment exercise!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
