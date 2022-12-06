from flask import flask

app = flask(___name___)

@app.route("/")
def home():     
    return "hello Word"

if  ___name___ == "___main___":
    app.run()