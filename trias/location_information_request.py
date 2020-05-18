from .trias_request import TriasRequest

class LocationInformationRequest(TriasRequest):
	def __init__(self, location_name):
		self.location_name = location_name
		self.executed = False
		super().__init__()

	def prepare_request_data(self):
		self.request_data = {
			"LocationInformationRequest": {
				"InitialInput": {
					"LocationName": self.location_name
				}
			}
		}
	def get_location_ids(self):
		locations = self.response_data["LocationInformationResponse"]["Location"]
		stop_point_refs = []
		if type(locations) is not list:
			locations = [locations]
		for i in locations:
			try:
				stop_point_refs.append(i["Location"]["StopPoint"]["StopPointRef"])
			except Exception as e:
				print(e)
		return stop_point_refs

	def __str__(self):
 		return "location_name: " + self.location_name
