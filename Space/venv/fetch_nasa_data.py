import requests
import pandas as pd
import json

# NASA API Key
API_KEY = "tULWHmGH4ipnKPcL3AF8H1t9tVFn7y1nbh8F1X3y"
BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"

# Function to fetch asteroid data
def fetch_asteroid_data(start_date, end_date):
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["near_earth_objects"]
    else:
        print("Error fetching data:", response.status_code)
        return None

# Example: Fetch data for the past 7 days
if __name__ == "__main__":
    from datetime import datetime, timedelta
    
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

    asteroid_data = fetch_asteroid_data(start_date, end_date)

    if asteroid_data:
        # Convert to DataFrame
        asteroid_list = []
        for date, asteroids in asteroid_data.items():
            for asteroid in asteroids:
                asteroid_list.append({
                    "id": asteroid["id"],
                    "name": asteroid["name"],
                    "close_approach_date": date,
                    "diameter_km": asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                    "velocity_kmh": asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"],
                    "miss_distance_km": asteroid["close_approach_data"][0]["miss_distance"]["kilometers"],
                    "is_hazardous": asteroid["is_potentially_hazardous_asteroid"]
                })

        df = pd.DataFrame(asteroid_list)
        
        # Save data as CSV
        df.to_csv("asteroid_data.csv", index=False)
        print("Data saved to asteroid_data.csv")
