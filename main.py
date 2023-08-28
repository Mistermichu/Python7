# Previous Code Version available: https://github.com/Mistermichu/Python6

import requests
import json
from functions import select_location, get_date

URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"


class WeatherForecaster:
    def __init__(self) -> None:
        pass

    def request(self, latitude, longitude, searched_date, url):
        api_data = requests.get(url.format(
            latitude=latitude, longitude=longitude, searched_date=searched_date))
        if api_data.status_code == 200:
            api_data = json.loads(api_data.text)
        else:
            print("Bład wczytywania danych.")
            return False
        if not api_data:
            pass
        else:
            rain_sum = api_data["daily"].get("rain_sum")[0]
            try:
                rain_sum = float(rain_sum)
                if rain_sum > 0:
                    print("Będzie padać")
                elif rain_sum == 0:
                    print("Nie będzie padać")
                else:
                    print("Nie wiem")
            except ValueError:
                print("Nie wiem")

    def __setitem__():
        pass

    def __getitem__():
        pass

    def __iter__():
        pass


# Run App
latitude, longitude = select_location()
searched_date = get_date()
weather_forecaste = WeatherForecaster()
weather_forecaste.request(latitude, longitude, searched_date, URL)
