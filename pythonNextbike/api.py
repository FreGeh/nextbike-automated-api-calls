import requests
from xml.etree import ElementTree as ET

def getApiKey():
    getApiKeyURL = 'https://webview.nextbike.net/getAPIKey.json'
    response = requests.get(getApiKeyURL)
    data = response.json()
    return data['apiKey']

def getLoginKey(api_key, mobile, pin):
    url = "https://api.nextbike.net/api/login.xml"
    params = {
        'apikey': api_key,
        'mobile': mobile,
        'pin': pin
    }
    response = requests.get(url, params=params)
    root = ET.fromstring(response.text)
    
    # Find the 'user' element
    user = root.find('user')
    
    if user is None:
        raise ValueError("No 'user' element found in the response")
    
    # Get the 'loginkey' attribute from the 'user' element
    loginkey = user.get('loginkey')

    if loginkey is None:
        raise ValueError("No 'loginkey' attribute found in the 'user' element")

    return loginkey

def getClosestStation(api_key, latitude, longitude):
    url = "https://api.nextbike.net/api/getLocation.xml"
    params = {
        'apikey': api_key,
        'lat': latitude,
        'lng': longitude
    }
    response = requests.get(url, params=params)

    print(response)
    root = ET.fromstring(response.text)
    
    # Find the 'user' element
    country = root.find('country')
    
    if country is None:
        raise ValueError("No 'country' element found in the response")
    
    city = country.find('city')

    if city is None:
        raise ValueError("No 'city' element found in the response")
    
    place = city.find('place')

    if place is None:
        raise ValueError("No 'place' element found in the response")

    
    # Get the 'loginkey' attribute from the 'user' element
    placeID = place.get('uid')
    placeLatitude = place.get('lat')
    placeLongitude = place.get('lng')
    placeName = place.get('name')
    placeAvailableBikes = place.get('bikes')

    return placeID, placeLatitude, placeLongitude, placeName, placeAvailableBikes