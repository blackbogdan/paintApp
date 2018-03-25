from flask import Flask
from flask import request, url_for
from flask import render_template
from flask import redirect, Response


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def indexpage():
    if request.method == 'GET':
        return render_template('test.html')
    if request.method == 'POST':
        data = request.json
        print(data)
        return data[-1][::-1]

if __name__ == '__main__':
    app.debug = True
    app.run()