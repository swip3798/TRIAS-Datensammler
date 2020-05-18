from .trias_request import TriasRequest

class TripInfoRequest(TriasRequest):
    def __init__(self, journey_id, operating_day):
        '''
        Gives realtime information of current journey. Is not a full representation of the TripInfoRequest
        journey_id: String 
        '''
        self.journey_id = journey_id
        self.operating_day = operating_day
        super().__init__()

    def prepare_request_data(self):
        self.request_data = {
            "TripInfoRequest": {
                "JourneyRef": self.journey_id,
                "OperatingDayRef": self.operating_day,
                "Params": {
                    "IncludePosition": True
                }
            }
        }

    