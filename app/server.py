from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello from kubernetes'

if __name__ == '__main__':
    app.run()