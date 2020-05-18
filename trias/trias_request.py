from requests import Request
import requests
import xmltodict
import vvar
import json


class TriasRequest():
    '''
    Represents and executes request to Trias API. Can be used for any Trias Request
    '''
    def __init__(self):
        self.request_data = None
        self.trias_request = {
                "Trias": {
                    "@version": "1.1",
                    "@xmlns": "http://www.vdv.de/trias",
                    "@xmlns:siri": "http://www.siri.org.uk/siri",
                    "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                    "@xsi:schemaLocation": "http://www.vdv.de/trias file:///C:/development/HEAD/extras/TRIAS/TRIAS_1.1/Trias.xsd",
                    "ServiceRequest": {
                        "siri:RequestTimeStamp": "2019-05-02T15:41:17",
                        "siri:RequestorRef": None,
                        "RequestPayload": None
                }
            }
        }
        self.response_data = None

    def prepare_request_data(self):
        pass

    def execute(self):
        '''
        Adds request_ref for authentication and the request payload to the trias_request dict. Then send request to Trias API
        '''
        self.prepare_request_data()
        self.trias_request["Trias"]["ServiceRequest"]["siri:RequestorRef"] = vvar.env.reqref
        self.trias_request["Trias"]["ServiceRequest"]["RequestPayload"] = self.request_data
        xml_req = xmltodict.unparse(self.trias_request, pretty=True)
        res = requests.post(vvar.env.baseurl, data = xml_req, headers={"Content-Type": "application/xml"})
        xml_res = res.content.decode("utf-8")
        self.response_data = xmltodict.parse(xml_res)["Trias"]["ServiceDelivery"]["DeliveryPayload"]
        return self.response_data

    def __getitem__(self, key):
        return self.response_data[key]
    
    def __repr__(self):
        return json.dumps(self.response_data, indent=2)