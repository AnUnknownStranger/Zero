from flask import Flask

app = Flask(__name__)

#@app.route("/")
#TODO: Landing Page

#@app.route("/register")
#TODO: Register

#@app.route("/login")
#TODO: Login

#Add in the CSS, JS, and Image Folder


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)