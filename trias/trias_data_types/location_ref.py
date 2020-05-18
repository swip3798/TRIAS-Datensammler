class LocationRef():

    def __init__(self, stop_point = None, stop_place = None, geo_position = None, location_name = None):
        self.stop_point = stop_point
        self.stop_place = stop_place
        self.geo_position = geo_position
        self.location_name = location_name

    @staticmethod
    def _clear_dict(dic):
        return {k: v for k, v in dic.items() if v is not None}

    def get_dict(self):
        d = {
            "StopPointRef": self.stop_point,
            "StopPlaceRef": self.stop_place,
            "GeoPosition": self.geo_position,
            "LocationName": self.location_name
        }
        return self._clear_dict(d)
        

if __name__ == "__main__":
    loc = LocationRef(stop_point="de:08215:1554:1:1")
    print(loc.get_dict())