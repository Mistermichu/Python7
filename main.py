# Previous Code Version available: https://github.com/Mistermichu/Python6

import requests
import json
from datetime import datetime, timedelta
from functions import select_location


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
TODAY = datetime.now().date()
TOMORROW = TODAY + timedelta(days=1)
latitude, longitude = select_location()
