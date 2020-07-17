# dependency
from flask import Flask

#Instance
app = Flask(__name__)

# Root-starting point
@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == "__main__":
    app.run()

