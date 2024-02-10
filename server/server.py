from flask import Flask, jsonify

#App instance
app = Flask(__name__)

@app.route("/")
def home():
    return "Working as intended"

#Driver
if __name__ == "__main__":
    #REMOVE in prod
    app.run(debug=True)