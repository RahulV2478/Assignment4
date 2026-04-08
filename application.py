from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    value = os.environ.get("MY_ENV_VAR", "")
    return value

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
