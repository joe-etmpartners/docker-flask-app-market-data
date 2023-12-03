from app import app
from flask import request
from ETMProcessManager import ETMProcessManager
from ETMProcessManager import ETMProcess
import rds_skywalker
from time import sleep

#  kosong

def getLastDate(thisProcess):
    thisProcess.set_status('Running')
    thisProcess.set_progress(0)
    sleep(3)

    thisProcess.set_progress(10)
    rdsCalendar = rds_skywalker.RDSCalendar()
    thisProcess.set_progress(50)
    rtn = rdsCalendar.getLastDate()
    sleep(3)

    thisProcess.set_progress(100)

    thisProcess.set_status('Finishing')
    sleep(3)
    return rtn

@app.route('/')
@app.route('/index')
def index():
    pm = ETMProcessManager()
    rtn = pm.get_all_process_info()
    return rtn

@app.route('/run')
def run():
    pm = ETMProcessManager()
    process1 = ETMProcess('GetLastDate', 'Get last date from database', getLastDate)
    pm.register_process(process1)
    process1.run()
    rtn = pm.get_all_process_info()
    return rtn


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


