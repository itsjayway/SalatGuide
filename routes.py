from datetime import datetime
import requests

from Times import Times


def request_helper(url: str) -> dict:
    response = requests.get(url)
    data = response.json()
    return data


def get_prayer_times(city: str, country: str) -> Times:
    selection = 2
    today_formatted = datetime.now().strftime("%d-%m-%Y")

    url = f"http://api.aladhan.com/v1/timingsByAddress/{today_formatted}?address={city}, {country}?method={selection}"

    data = request_helper(url)

    return Times(data["data"])


if __name__ == "__main__":
    city = input("Enter city: ") or "Atlanta"
    country = input("Enter country: ") or "US"
    print(get_prayer_times(city, country))
