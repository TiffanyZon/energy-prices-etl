import requests
from datetime import datetime

today = datetime.now().strftime("%Y/%m-%d")
url = f"https://www.elprisetjustnu.se/api/v1/prices/{today}_SE4.json"


def extract_data(url):
    response = requests.get(url)
    response.raise_for_status()
    print(response.status_code)
    return response.json()


data = extract_data(url)
print(data)


def format_time(time_str):
    dt = datetime.fromisoformat(time_str)
    return dt.strftime("%Y-%m-%d %H:%M")


for record in data:
    start = format_time(record["time_start"])
    end = format_time(record["time_end"])
    print(f"From {start} to {end}, the price is {record['SEK_per_kWh']} SEK/kWh")
