import time
import threading
import json
import datetime
from bottle import route, run

timeslots = {}
time_diff = (30 / 80) * 1000

problematic_station_ids = []

@route('/timeslots')
def get_timeslots():
    temp_time = timeslots.copy()
    temp_time = sorted(temp_time.keys())
    res = ""
    for idx, i in enumerate(temp_time):
        res += str(idx + 1) + ". &emsp;" + str(datetime.datetime.fromtimestamp(i / 1000)) + "<br/>"
    return res

@route('/problems')
def get_problematic_station_ids():
    temp_stations = problematic_station_ids.copy()
    res = ""
    for i in temp_stations:
        res += str(i) + "<br/>"
    return res

def garbage_collecting():
    for key in timeslots:
        if key < time.time() * 1000:
            del timeslots[key]

def _next_timeslot(timeslot):
    last_three = timeslot % 1000
    if last_three == 333:
        return timeslot + 334
    return timeslot + 333

def get_timeslot(wait_time = 0):
    now = int(time.time() * 1000)
    wanted_timeslot = now + int(wait_time) * 1000
    last_three = wanted_timeslot % 1000
    if last_three < 333:
        last_three = 333
    elif last_three < 667:
        last_three = 667
    else:
        last_three = 1000
    wanted_timeslot = int(wanted_timeslot / 1000) * 1000
    wanted_timeslot += last_three
    while wanted_timeslot in timeslots:
        wanted_timeslot = _next_timeslot(wanted_timeslot)
    timeslots[wanted_timeslot] = True
    return wanted_timeslot / 1000

def delete_timeslot(timeslot):
    del timeslots[timeslot]
    
def monitor_timeslots():
    run(host="localhost", port=7777)

if __name__ == "__main__":
    monitor_timeslots()