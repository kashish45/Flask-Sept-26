from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/ping')
def ping():
    return {"message":"Why are you pinging me?"}

@app.route('/hello')
def hello():
    return "Hello, User!"


if __name__ == '__main__':
    app.run(debug=True)