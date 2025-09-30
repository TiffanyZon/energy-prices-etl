import requests
from datetime import datetime

today = datetime.now().strftime("%Y/%m-%d")

url = f"https://www.elprisetjustnu.se/api/v1/prices/{today}_SE4.json"


def extract_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def format_time(time_str):
    dt = datetime.fromisoformat(time_str)
    return dt.strftime("%Y-%m-%d %H:%M")


data = extract_data(url)
for record in data:
    start = format_time(record["time_start"])
    end = format_time(record["time_end"])
    print(f"From {start} to {end}, price: {record['SEK_per_kWh']} SEK/kWh")
