import json
import requests


class WeatherForecaster:
    def __init__(self, latitude, longitude, url):
        self.latitude = latitude
        self.longitude = longitude
        self.url = url
        self.rain_data = {}

    def request(self, searched_date):
        api_data = requests.get(self.url.format(
            latitude=self.latitude, longitude=self.longitude, searched_date=searched_date))
        if api_data.status_code == 200:
            api_data = json.loads(api_data.text)
        else:
            rain_info = "Błąd wczytywania danych"
            print(rain_info)
            return rain_info
        if not api_data:
            pass
        else:
            rain_sum = api_data["daily"].get("rain_sum")[0]
            try:
                rain_sum = float(rain_sum)
                if rain_sum > 0:
                    rain_info = "Będzie padać"
                    print(rain_info)
                    return rain_info
                elif rain_sum == 0:
                    rain_info = "Nie będzie padać"
                    print(rain_info)
                    return rain_info
                else:
                    rain_info = "Nie wiem"
                    print(rain_info)
                    return rain_info
            except ValueError:
                print("Nie wiem")

    def __setitem__(self, date, rain_info):
        self.rain_data[date] = rain_info

    def __getitem__(self, date):
        return self.rain_data[date]

    def __iter__(self):
        return iter(self.rain_data.items())
