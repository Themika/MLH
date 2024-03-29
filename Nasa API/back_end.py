from datetime import date, datetime
import json
import requests

class Data:
    def __init__(self, id: int, n: str, estDMinKm: float, estDMaxKm: float, 
                 estDMinM: float, estDMaxM: float
                 ,mag: float, potDanLevel: bool, date: str, jpgURL: str) -> None:
        
        #estimated diameter in kilometers
        self.id = id
        self.name = n
        self.est_dia_min_km = estDMinKm
        self.est_dia_max_km = estDMaxKm

        #estimated diameter in meters
        self.est_dia_min_m = estDMinM
        self.est_dia_max_m = estDMaxM

        #magnitude
        self.magnitude = mag

        #potential danger level
        self.pot_danger_level = potDanLevel

        #date of nearest approach to Earth
        self.date = date

        #The url to more information
        self.nasa_jpl_url = jpgURL

        def __str__(self) -> str: #not working
            return f"id={self.id}, est_dia_min_km={self.est_dia_min_km}, est_dia_max_km={self.est_dia_max_km}, est_dia_min_m={self.est_dia_min_m}, est_dia_max_m={self.est_dia_max_m}, magnitude={self.magnitude}, pot_danger_level={self.pot_danger_level}, date={self.date}, nasa_jpl_url={self.nasa_jpl_url}"
    

class Data_Extraction:
    def __init__(self, start, end) -> None:
        startDate = start
        endDate = end

        self.current_date = start

        self.parameters = {
            "start_date": startDate,
            "end_date": endDate,
            "api_key": "" #insert your own API key
        } 

        self.asteriods = []
        self.asteriod_names = []
        self.asteriod_Ids = []

    def load_data(self):
        response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?", params=self.parameters)
        self.data = json.loads(response.text)

        self.element_count = self.data["element_count"]
    
    def get_asteriods(self):
        index = 0
        count = 0
        while(self.element_count != count):
            try:
                tmp = self.data["near_earth_objects"][f"{self.current_date}"][index]
                self.asteriod_names.append(tmp["name"])
                self.asteriod_Ids.append(tmp["id"])
                self.asteriods.append(Data(tmp["id"], tmp["name"], tmp["estimated_diameter"]["kilometers"]["estimated_diameter_min"], tmp["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                                             tmp["estimated_diameter"]["meters"]["estimated_diameter_min"], tmp["estimated_diameter"]["meters"]["estimated_diameter_max"],
                                             tmp["absolute_magnitude_h"], tmp["is_potentially_hazardous_asteroid"], tmp["close_approach_data"][0]["close_approach_date"], tmp["nasa_jpl_url"]))
                
                index += 1
                count += 1
            except:
                index = 0
                
                self.current_date = self.current_date.replace(day = self.current_date.day + 1)