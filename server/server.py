from flask import Flask, jsonify
from basketballrefapi import sandbox

#App instance
app = Flask(__name__)

@app.route("/")
def home():
    #Displays JSON data to front end
    return sandbox.run()
    

#Driver
if __name__ == "__main__":
    #REMOVE in prod
    app.run(debug=True)