import json
import os

from flask import Flask, request, send_file

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def testpost():
    if len(request.args) == 1:
        with open('test.json') as f:
            data = json.load(f)
            for i in request.args:
                data['history'].append(request.args[i])
        os.remove('test.json')
        with open('test.json', 'w') as f:
            json.dump(data, f, indent=4)
    return send_file('test.json')


if __name__ == "__main__":
    app.run(port=80)
