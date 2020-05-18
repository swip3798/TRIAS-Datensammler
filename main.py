from model import Stop, Base, session
import logging
#logging.basicConfig(filename='detector.log',level=logging.ERROR)

import isodate
import json
import time
import sys
import threading
import datetime
import timeslot_service

from miner import DepartureDetector, station_ids
from trias import StopEventRequest
from trias.trias_data_types import LocationRef, PtMode, StopEventType, StopEvent


POLLINGINTERVAL = 30

detectors = []

print(station_ids)

for i in station_ids:
    detectors.append(DepartureDetector(i, POLLINGINTERVAL))

for detector in detectors:
    detector.start_observe()
    time.sleep(POLLINGINTERVAL / len(station_ids))

timeslot_service.monitor_timeslots()

for detector in detectors:
    detector.stop_observe()

