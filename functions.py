import json


class LoadLocations:
    def __init__(self, locations_file):
        self.locations = self.load_locations(locations_file)

    def load_locations(self, locations_file):
        with open(locations_file, "r") as locations_list:
            available_locations = json.load(locations_list)
            print(available_locations)
        return available_locations


available_locations = LoadLocations("locations.json")
available_locations = available_locations.locations


def try_float(message):
    input_check = False
    while not input_check:
        try:
            user_input = float(input(f"{message}").replace(",", "."))
            return user_input
        except ValueError:
            print("Błąd. Spróbuj ponownie")


def print_available_locations():
    location_name_list = []
    for location_name, data in available_locations.items():
        location_name_list.append(location_name)
    print(f"Dostępne lokacje: {location_name_list}")


def select_location():
    print_available_locations()
    location_name = None
    while not location_name:
        location_name = input("Podaj nazwę miasta: ").upper()
        if len(location_name) == 0:
            print("Błąd. Spróbuj ponownie")
            location_name = None
    if location_name not in available_locations:
        print("Nie wykryto miasta.")
        add_new_city(location_name)
    latitude = available_locations[location_name].get("latitude")
    longitude = available_locations[location_name].get("longitude")
    return latitude, longitude


def add_new_city(location_name):
    location_latitude = try_float("Podaj szerokość geograficzną: ")
    location_longitude = try_float("Podaj długość geograficzną: ")
    available_locations[location_name] = {
        "latitude": location_latitude,
        "longitude": location_longitude
    }
