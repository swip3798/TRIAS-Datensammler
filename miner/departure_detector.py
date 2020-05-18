import time
import threading
import isodate
import datetime
import logging

from trias import StopEventRequest
from trias.trias_data_types import PtMode, LocationRef, StopEventType, StopEvent
from sqlalchemy.orm import sessionmaker
from timeslot_service import get_timeslot, delete_timeslot, problematic_station_ids

from model import Stop, engine

class DepartureDetector():
    
    def __init__(self, station_id, polling_interval = 30, stop_test_fraction = 2):
        self.station_id = station_id
        self.polling_interval = polling_interval
        self.continue_running = False
        self.stop_test_fraction = stop_test_fraction
        self.stop_event_request = StopEventRequest(LocationRef(stop_place=self.station_id), include_previous_calls=False, include_onward_calls=False, time_window=isodate.Duration(hours = 1), stop_event_type=StopEventType.DEPARTURE, pt_mode_filter=PtMode.RAIL, number_of_results=10)
        self.current_stop_events = []
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.wait_time = 30

    def start_observe(self):
        print("Start observe thread for station: " + self.station_id)
        self.thread = threading.Thread(target=self._observe, args=())
        self.thread.start()
    
    def stop_observe(self):
        self.continue_running = False

    def _wait_for_timeslot(self, wait_time):
        timeslot = get_timeslot(wait_time)
        self.wait_time = timeslot - time.time()
        time.sleep(self.wait_time)
        delete_timeslot(timeslot * 1000)

    def _observe(self):
        self.continue_running = True
        self._wait_for_timeslot(0)
        while self.continue_running:
            self._get_stop_info()
            try:
                wait_time = self._look_for_departure()
            except:
                print("Look didn't work, station_id:", self.station_id)
                problematic_station_ids.append(self.station_id)
                time.sleep(7200)
            self._wait_for_timeslot(wait_time)
        print("Loop stopped")

    def _get_stop_info(self):
        self.stop_event_request.execute()

    def _look_for_departure(self):
        try:
            if self.stop_event_request["StopEventResponse"]["ErrorMessage"]["Code"] == "-4030":
                print(self.station_id, "Location UNSERVED")
        except:
            pass
        new_stop_events = self.stop_event_request["StopEventResponse"]["StopEventResult"]
        new_stop_events = [StopEvent.from_json(i) for i in new_stop_events]
        unfiltered_new_stop_events = new_stop_events.copy()
        new_stop_events = self._filter_stop_events(new_stop_events)
        
        if len(new_stop_events) == 0:
            print("Didn't found tram or train, maybe only bus check it, station_id:", self.station_id)
            next_stop = unfiltered_new_stop_events[0]
            for event in unfiltered_new_stop_events:
                if event.estimated_time > next_stop.estimated_time:
                    next_stop = event
        else:
            next_stop = new_stop_events[0]
            for event in new_stop_events:
                if event.estimated_time < next_stop.estimated_time:
                    next_stop = event
        now = datetime.datetime.now(datetime.timezone.utc)
        timedelta = next_stop.estimated_time - now
        timedelta = timedelta.total_seconds()
        timedelta -= 120
        if timedelta < 0:
            timedelta = self.polling_interval
        

        for event in self.current_stop_events:
            if event.journey_ref not in [i.journey_ref for i in new_stop_events]:
                self._save_departure(event)
                logging.info("Stop detected")
                print("Stop detected")

        self.current_stop_events = new_stop_events
        return timedelta


    def _filter_stop_events(self, stop_events):
        filtered = []
        for event in stop_events:
            if event.pt_mode in ["rail", "tram"]:
                filtered.append(event)
        return filtered
    
    def _save_departure(self, event):
        dt = datetime.datetime.now(datetime.timezone.utc)
        dt = dt - datetime.timedelta(seconds = dt.second, microseconds = dt.microsecond)
        stop = Stop(stop_point_ref = event.stop_point_ref,
            stop_point_name = event.stop_point_name,
            timetabled_time = event.timetabled_time,
            real_time = dt,
            stop_seq_number = event.stop_sequence_number,
            operating_day_ref = event.operating_day_ref,
            journey_ref = event.journey_ref,
            line_ref = event.line_ref,
            direction_ref = event.direction_ref,
            pt_mode = event.pt_mode,
            submode = event.submode,
            published_line_name = event.line_name,
            operator_ref = "kvv",
            route_description = event.route_description,
            origin_stop_point_ref = event.origin_stop_point_ref,
            destination_text = event.destination_text)
        self.session.add(stop)
        self.session.commit()

        
