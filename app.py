from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Wlcome to SamIG"

if __name__ == '__main__':
    app.run(debug=True)