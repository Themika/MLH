from datetime import datetime
import json
import requests

class Data:
    def __init__(self, estDMinKm, estDMaxKm, 
                 estDMinM, estDMaxM
                 ,mag, potDanLevel, date: datetime.now, jpgURL) -> None:
        
        #estimated diameter in kilometers
        _est_dia_min_km = estDMinKm
        _est_dia_max_km = estDMaxKm

        #estimated diameter in meters
        _est_dia_min_m = estDMinM
        _est_dia_max_km = estDMaxM

        #magnitude
        _magnitude = mag

        #potential danger level
        _pot_danger_level = potDanLevel

        #date of nearest approach to Earth
        _date = date

        #The url to more information
        _nasa_jpl_url = jpgURL

class Data_Extraction:
    def __init__(self) -> None:
        parameters = {
            "start_date": "2015-09-07",
            "end_date": "2015-09-08",
            "api_key": "UciPBat8ybi63BNgjcuVWih9gvwgRlayRiqLJ82g" #TODO remove API key
        }

        response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?", params=parameters)
        data = json.loads(response.text)

        asteriods: Data[data["element_count"]]

data = Data_Extraction()