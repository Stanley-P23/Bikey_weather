import requests







def get_hourly_forecast(api_key, location, future_jump):

    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={future_jump}&hourly=1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'forecast' in data and 'forecastday' in data['forecast'] and len(data['forecast']['forecastday']) > 1:
            hourly_forecast = data['forecast']['forecastday'][future_jump-1]['hour']
            return hourly_forecast
        else:
            print("Error: Forecast data for day after tomorrow is not available.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None



