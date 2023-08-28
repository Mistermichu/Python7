# Previous Code Version available: https://github.com/Mistermichu/Python6

import requests
import json
from functions import select_location, get_date


class WeatherForecaster:
    def __init__(self):
        self.load = self.load_data()
        self.save = self.save_data()
        self.request = self.api_request()

    def __setitem__():
        pass

    def __getitem__():
        pass

    def __iter__():
        pass


# Run App
latitude, longitude = select_location()
searched_date = get_date()
