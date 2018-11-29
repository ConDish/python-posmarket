from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
PORT = 5000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
    return "Not Found."

@app.route('/', methods=['GET'])
def index():
    return "Hola desde main.py"

@app.route('/recaptcha', methods=['GET'])
def recaptcha():
    return render_template('recaptcha.html')

if __name__ == "__main__":
    app.run(port = PORT, debug = DEBUG)