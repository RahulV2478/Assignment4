from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    env_var = os.environ.get("MY_ENV_VAR")
    return env_var

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
