from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_word():
    return "Hello to the word of Flask"
if __name__ == '_main_':
    app.run()