from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, my name sherin mon biju i created a simple model application using python flask update now"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

