import isodate

class StopEvent:
	'''
	Represents a StopEvent
	WARNING: Currently for the submode it currently will only get bus, tram and rail submodes
	'''
	def __init__(self, stop_point_ref, stop_point_name, timetabled_time, estimated_time, stop_sequence_number, operating_day_ref, journey_ref, line_ref, direction_ref, pt_mode, submode, line_name, route_description, origin_stop_point_ref, destination_text):
		self.stop_point_ref = stop_point_ref
		self.stop_point_name = stop_point_name
		self.timetabled_time = timetabled_time
		self.estimated_time = estimated_time
		self.stop_sequence_number = stop_sequence_number
		self.operating_day_ref = operating_day_ref
		self.journey_ref = journey_ref
		self.line_ref = line_ref
		self.direction_ref = direction_ref
		self.pt_mode = pt_mode
		self.submode = submode
		self.line_name = line_name
		self.route_description = route_description
		self.origin_stop_point_ref = origin_stop_point_ref
		self.destination_text = destination_text
		
	def get_stop_point_ref(self):
		return self.stop_point_ref

	def get_stop_point_name(self):
		return self.stop_point_name

	def get_timetabled_time(self):
		return self.timetabled_time

	def get_estimated_time(self):
		return self.estimated_time

	def get_stop_sequence_number(self):
		return self.stop_sequence_number

	def get_operating_day_ref(self):
		return self.operating_day_ref

	def get_journey_ref(self):
		return self.journey_ref

	def get_line_ref(self):
		return self.line_ref

	def get_direction_ref(self):
		return self.direction_ref

	def get_pt_mode(self):
		return self.pt_mode

	def get_submode(self):
		return self.submode

	def get_line_name(self):
		return self.line_name

	def get_route_decription(self):
		return self.route_description

	def get_origin_stop_point_ref(self):
		return self.origin_stop_point_ref

	def get_destination_text(self):
		return self.destination_text


	def __str__(self):
 		return "stop_point_ref: " + self.stop_point_ref + " , " + "stop_point_name: " + self.stop_point_name + " , " + "timetabled_time: " + str(self.timetabled_time) + " , " + "estimated_time: " + str(self.estimated_time) + " , " + "stop_sequence_number: " + self.stop_sequence_number + " , " + "operating_day_ref: " + self.operating_day_ref + " , " + "journey_ref: " + self.journey_ref + " , " + "line_ref: " + self.line_ref + " , " + "direction_ref: " + self.direction_ref + " , " + "pt_mode: " + self.pt_mode + " , " + "submode: " + self.submode + " , " + "line_name: " + self.line_name + " , " + "route_decription: " + self.route_description + " , " + "origin_stop_point_ref: " + self.origin_stop_point_ref + " , " + "destination_text: " + self.destination_text
		
	@staticmethod
	def from_json(json_dict):
		try:
			stop_point_ref = json_dict["StopEvent"]["ThisCall"]["CallAtStop"]["StopPointRef"]
		except:
			print(json_dict)
		stop_point_name = json_dict["StopEvent"]["ThisCall"]["CallAtStop"]["StopPointName"]["Text"]
		timetabled_time = isodate.parse_datetime(json_dict["StopEvent"]["ThisCall"]["CallAtStop"]["ServiceDeparture"]["TimetabledTime"])
		try:
			estimated_time = isodate.parse_datetime(json_dict["StopEvent"]["ThisCall"]["CallAtStop"]["ServiceDeparture"]["EstimatedTime"])
		except:
			estimated_time = timetabled_time
		stop_sequence_number = json_dict["StopEvent"]["ThisCall"]["CallAtStop"]["StopSeqNumber"]
		operating_day_ref = json_dict["StopEvent"]["Service"]["OperatingDayRef"]
		journey_ref = json_dict["StopEvent"]["Service"]["JourneyRef"]
		line_ref = json_dict["StopEvent"]["Service"]["LineRef"]
		direction_ref = json_dict["StopEvent"]["Service"]["DirectionRef"]
		pt_mode = json_dict["StopEvent"]["Service"]["Mode"]["PtMode"]
		if pt_mode == "tram":
			submode = json_dict["StopEvent"]["Service"]["Mode"]["TramSubmode"]
		elif pt_mode == "rail":
			submode = json_dict["StopEvent"]["Service"]["Mode"]["RailSubmode"]
		elif pt_mode == "bus":
			submode = json_dict["StopEvent"]["Service"]["Mode"]["BusSubmode"]
		else:
			submode = ""
		line_name = json_dict["StopEvent"]["Service"]["PublishedLineName"]["Text"]
		try:
			route_description = json_dict["StopEvent"]["Service"]["RouteDescription"]["Text"]
		except:
			route_description = ""
		destination_text = json_dict["StopEvent"]["Service"]["DestinationText"]["Text"]
		origin_stop_point_ref = json_dict["StopEvent"]["Service"]["OriginStopPointRef"]

		return StopEvent(stop_point_ref, stop_point_name, timetabled_time, estimated_time, stop_sequence_number, operating_day_ref, journey_ref, line_ref, direction_ref, pt_mode, submode, line_name, route_description, origin_stop_point_ref, destination_text)
