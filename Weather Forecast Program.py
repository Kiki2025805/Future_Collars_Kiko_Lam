import json
import os


class WeatherForecast:
    def __init__(self, filename="weather_data.json"):
        self.filename = filename
        self._data = {}

        # Load existing data from file
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    self._data = json.load(f)
                except json.JSONDecodeError:
                    self._data = {}

    def _save(self):
        """Save data to file"""
        with open(self.filename, "w") as f:
            json.dump(self._data, f)

    def _fetch_from_api(self, date):
        """
        Simulate an API request (replace with real API if needed)
        """
        print(f"Fetching data from API for {date}...")
        return "rainy"

    # Allow setting values using weather_forecast[date] = weather
    def __setitem__(self, date, weather):
        self._data[date] = weather
        self._save()

    # Allow getting values using weather_forecast[date]
    def __getitem__(self, date):
        if date not in self._data:
            weather = self._fetch_from_api(date)
            self._data[date] = weather
            self._save()
        return self._data[date]

    # Allow iteration over dates
    def __iter__(self):
        return iter(self._data)

    # Return a generator of (date, weather)
    def items(self):
        for date, weather in self._data.items():
            yield (date, weather)