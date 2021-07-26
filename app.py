from flask import Flask, render_template

# Lets create a webpage

app = Flask(__name__)

# This is the pattern of our URL
@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
