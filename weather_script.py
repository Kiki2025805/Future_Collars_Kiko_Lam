import requests
import json
from datetime import datetime, timedelta

# Configuration
FILE_NAME = "weather_results.json"
LATITUDE = 51.5074   # London
LONGITUDE = -0.1278  # London

def check_weather():
    # 1. Load historical data from file (Requirement 5)
    try:
        with open(FILE_NAME, "r") as f:
            cache = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        cache = {}

    # 2. Ask user for a date (Requirement 1)
    print("=== Weather Checker Application ===")
    user_input = input("Enter date (YYYY-mm-dd) or press Enter for tomorrow: ").strip()

    # 3. Handle empty input for tomorrow's date (Requirement 2)
    if not user_input:
        target_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(user_input, '%Y-%m-%d')
            target_date = user_input
        except ValueError:
            print("Invalid date format. Please use YYYY-mm-dd.")
            return

    # 4. Return cached result if date exists (Requirement 5)
    if target_date in cache:
        print(f"\n[Status: Found in Local File]")
        display_result(target_date, cache[target_date])
        return

    # 5. Fetch from API if not in file (Requirement 3)
    api_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}&longitude={LONGITUDE}&"
        f"daily=precipitation_sum&timezone=Europe%2FLondon&"
        f"start_date={target_date}&end_date={target_date}"
    )

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # Extracting precipitation result
        precip_sum = data.get("daily", {}).get("precipitation_sum", [])
        
        if not precip_sum or precip_sum[0] is None:
            result_val = -1.0
        else:
            result_val = float(precip_sum[0])

        # 6. Save results to the file
        cache[target_date] = result_val
        with open(FILE_NAME, "w") as f:
            json.dump(cache, f, indent=4)

        print(f"\n[Status: Fetched from API]")
        display_result(target_date, result_val)

    except Exception as e:
        print(f"Error: Could not connect to API. {e}")

def display_result(date, value):
    # Determine rain state (Requirement 4)
    print(f"Date: {date}")
    if value > 0.0:
        print(f"Result: It will rain (Precipitation: {value} mm)")
    elif value == 0.0:
        print("Result: It will not rain")
    else:
        print("Result: I don't know")

if __name__ == "__main__":
    check_weather()