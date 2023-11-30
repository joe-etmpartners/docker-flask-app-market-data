from app import app
from flask import request

#  kosong

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/add')
def add():
    data = request.args.get('data', None)
    _list = list(map(int, data.split(',')))
    
    total = sum(_list)
    return 'Result= ' + str(total)

def sum(arg):
    total = 0
    try:
        for val in arg:
            total += val
    except Exception:
        return "Error occured!", 500
    return total


