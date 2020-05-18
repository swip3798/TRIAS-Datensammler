import trias
import isodate
from datetime import date
import datetime

class Visit():
    def __init__(self, visit_dict):
        self.stop_point_ref = visit_dict["StopPointRef"]
        self.stop_point_name = visit_dict["StopPointName"]["Text"]
        self.timetabled_time = visit_dict["ServiceDeparture"]["TimetabledTime"]
        self.estimated_time = visit_dict["ServiceDeparture"]["EstimatedTime"]
        self.stop_sequence_number = visit_dict["StopSeqNumber"]
        self.estimated_datetime = isodate.parse_datetime(self.estimated_time)


class LocatorService():
    def __init__(self, journey_id):
        self.journey_id = journey_id
    
    def locate(self):
        operating_day = isodate.date_isoformat(date.today())
        journey = trias.TripInfoRequest(self.journey_id, operating_day).execute()
        visits = journey["TripInfoResponse"]["TripInfoResult"]["PreviousCall"] + journey["TripInfoResponse"]["TripInfoResult"]["OnwardCall"]
        visits = [Visit(visit) for visit in visits]
        


