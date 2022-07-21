# hello world app using flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return """
    <h1>Hello World</h1>
"""
@app.route('/template')
def hello_template():
    return render_template('hello.html')
    
@app.route('/message')
def message():
    return render_template('message.html', message="Hello! Hey! This is rendered into the template and passed to the user", 
                           messages=["Hello", "Hey", "This is rendered into the template and passed to the user"])

if __name__ == '__main__':
    app.debug=True
    app.run(
        host='0.0.0.0',
        port=8081
    )