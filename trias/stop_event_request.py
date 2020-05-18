from .trias_request import TriasRequest
import isodate
from .trias_data_types import LocationRef, LineFilter, PtMode, LineDirection
from datetime import datetime


class StopEventRequest(TriasRequest):

    def __init__(self, location, pt_mode_filter = None, line = None, number_of_results = None, time_window = None, stop_event_type = None, include_previous_calls = None, include_onward_calls = None, include_operating_days = None, include_realtime_data = True):
        '''
        Request to get all stop events from a location. All parameters except location are optional. Chapter 10 in the documention.
        Params:

        location: LocationRef
        pt_mode_filter: PtMode (Enum)
        line: LineFilter
        number_of_results: int
        time_window: isodate.Duration|datetime.timedelta
        stop_event_type: StopEventType (Enum)
        include_previous_calls: boolean
        include_onward_calls: boolean
        include_operatiing_days: boolean
        include_realtime_data: boolean
        '''
        self.location = location
        self.pt_mode_filter = pt_mode_filter
        self.line = line
        self.number_of_results = number_of_results
        self.time_window = time_window
        self.stop_event_type = stop_event_type
        self.include_previous_calls = include_previous_calls
        self.include_onward_calls = include_onward_calls
        self.include_operatiing_days = include_operating_days
        self.include_realtime_data = include_realtime_data
        if self.pt_mode_filter != None:
            self.pt_mode_filter = self.pt_mode_filter.value
        if self.stop_event_type != None:
            self.stop_event_type = self.stop_event_type.value
        if self.time_window != None:
            self.time_window = isodate.duration_isoformat(self.time_window)
        super().__init__()
    
    @staticmethod
    def _clear_dict(dic):
        return {k: v for k, v in dic.items() if v is not None}

    def prepare_request_data(self):
        self.request_data = {
            "StopEventRequest":{
                "Location": {
                    "LocationRef": self.location.get_dict(),
                    "DepArrTime": isodate.datetime_isoformat(datetime.utcnow()) + "Z"
                }
            }
        }
        params = {
            "PtModeFilter": self.pt_mode_filter,
            "NumberOfResults": self.number_of_results,
            "TimeWindow": self.time_window,
            "StopEventType": self.stop_event_type,
            "IncludeOperatingDays": self.include_operatiing_days,
            "IncludeRealtimeData": self.include_realtime_data,
            "IncludeOnwardCalls": self.include_onward_calls,
            "IncludePreviousCalls": self.include_previous_calls
        }
        if self.line != None:
            if self.line.direction != None:
                self.line.direction = self.line.direction.value
            params["LineFilter"] = self._clear_dict({"Line": {
                "LineRef": self.line.line,
                "DirectionRef": self.line.direction
            }})
        params = self._clear_dict(params)
        if params != {}:
            self.request_data["StopEventRequest"]["Params"] = params