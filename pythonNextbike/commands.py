from api import *
from geopy.geocoders import Nominatim

def find_nearest_station(apiKey, loginKey, *args):
    city = args[0]
    street = args[1]
    number = args[2]

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(street + " " + number + " " + city)

    print(location)

    placeID, placeLatitude, placeLongitude, placeName, placeAvailableBikes = getClosestStation(apiKey, location.latitude, location.longitude)
    print.ln(placeID)
    print.ln(placeLatitude)
    print.ln(placeLongitude)
    print.ln(placeName)
    print.ln(placeAvailableBikes)


def exit_program():
    print("Exiting program...")
    exit()