from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def result():
    print(request.data)


@app.route('/', methods=['GET'])
def something():
    print('something')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
