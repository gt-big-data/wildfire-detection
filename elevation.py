import requests
import urllib

# USGS Elevation Point Query Service
url = r'https://nationalmap.gov/epqs/pqs.php?'


#test case
#latitude = 33.770837
#longitude = -84.403632

latitude = input("enter latitude")
longitude = input("enter longitude")


def elevation_function(latitude, longitude):
    
    params = {
        'output': 'json',
        'x': longitude,
        'y': latitude,
        'units': 'Meters'
    }
    result = requests.get((url + urllib.parse.urlencode(params)))
    return (result.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation'])


print(elevation_function(latitude, longitude))
