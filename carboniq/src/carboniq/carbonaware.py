import requests


CARBON_AWARE_URL = "http://localhost:5073"


def get_forecast(location: str, window_size: int = 30) -> dict:
    response = requests.get(
        f"{CARBON_AWARE_URL}/emissions/forecasts/current",
        params={
            "location": location,
            "windowSize": window_size,
        },
        timeout=30,
    )

    response.raise_for_status()

    return response.json()[0]