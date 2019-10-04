import sys
import os
sys.path.append(os.path.expandvars("$ALG_PY3_LIBS"))
from random import randint
from flask import Flask, render_template, json, request
import process

app = Flask(__name__)

proc = process.Process()


@app.route('/')
def index():
    proc.start()
    return render_template('index.html')

@app.route('/getSize', methods=['GET', 'POST'])
def getSize():
    ans = request.form['letters']
    return json.dumps({'len': len(ans)})

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    numbers = request.form['numbers'].replace(" ", "").split(',')
    problem = "Ошибка ввода.. Введи числа положительные раздлённые запятой, к примеру \"1,5\""
    try:
        ans = randint(int(numbers[0]), int(numbers[1]))
    except:
        ans = problem
    return json.dumps({'number': ans})


@app.route('/checking', methods=['GET', 'POST'])
def checking():
    q = proc.queue
    if q.qsize() > 0:
        return json.dumps({'atMoment': q.get()})
    else:
        return json.dumps({'atMoment': 'nope'})


if __name__ == '__main__':
    app.run(debug=True, port=8080)