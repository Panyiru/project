import requests

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('google-geo.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)




GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

class Geohandler():
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY



    def getAddress(self, lat,lng):
        params = {'latlng' : str(lat)+','+str(lng), 'key' : self.API_KEY}
        # Do the request and get the response data
        try:
            req = requests.get(GOOGLE_MAPS_API_URL, params=params)

        except Exception as e:
            logger.exception("Problem getting address: " + str(e))

        return req.json() if req else None



    def getPostCode(self, json_data):
        try:
            # Add safety check
            if json_data['results']:
                address_components = json_data['results'][0]["address_components"]

                for element in address_components:
                    if element['types'] == [ "postal_code" ]:
                        return element['short_name']
        except Exception as e:
            logger.exception("Problem getting post-code: " + str(e))


