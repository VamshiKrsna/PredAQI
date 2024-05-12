import requests
import config

api_key = config.AQI_API_KEY

def aqi_extractor(city_name):
    aqi_url = f"https://api.waqi.info/feed/{city_name}/?token={api_key}"
    
    response = requests.get(aqi_url)
    json_data = response.json()
    
    aqi = json_data['data']['aqi']
    pm25 = json_data['data']['iaqi'].get('pm25', {}).get('v')
    pm10 = json_data['data']['iaqi'].get('pm10', {}).get('v')
    no2 = json_data['data']['iaqi'].get('no2', {}).get('v')
    co = json_data['data']['iaqi'].get('co', {}).get('v')
    so2 = json_data['data']['iaqi'].get('so2', {}).get('v')
    ozone = json_data['data']['iaqi'].get('o3', {}).get('v')
    
    data = {
        "City": city_name,
        "AQI": aqi,
        "PM2.5": pm25,
        "PM10": pm10,
        "NO2": no2,
        "CO": co,
        "SO2": so2,
        "Ozone": ozone
    }
    
    return data

print(aqi_extractor("Hyderabad"))
print(aqi_extractor("Delhi"))
print(aqi_extractor("Kolkata"))