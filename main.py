# Previous Code Version available: https://github.com/Mistermichu/Python6

from functions import select_location, get_date, continue_request
from WeatherForecaster import WeatherForecaster

URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"


# Run App

latitude, longitude, location_name = select_location()
searched_date = get_date()
weather_forecaste = WeatherForecaster(
    latitude, longitude, URL)
run_app = True
while run_app:
    if searched_date == None:
        searched_date = get_date()
    try:
        rain_info = weather_forecaste[searched_date]
        print(rain_info)
    except KeyError:
        rain_info = weather_forecaste.request(searched_date)
        weather_forecaste[searched_date] = rain_info
    print(f"Obecnie zapisane prognozy dla lokalizacji {location_name}: ")
    for date, forecast in weather_forecaste:
        print(f"{date}: {forecast}")
    user_input = continue_request()
    if not user_input:
        run_app = False
    else:
        searched_date = None
