from extract import extract_data
from transform import format_time
from datetime import datetime

today = datetime.now().strftime("%Y/%m-%d")
url = f"https://www.elprisetjustnu.se/api/v1/prices/{today}_SE4.json"


def run_pipeline(url):
    raw_data = extract_data(url)
    for record in raw_data:
        start = format_time(record["time_start"])
        end = format_time(record["time_end"])
        print(f"From {start} to {end}, the price is {record['SEK_per_kWh']} SEK/kWh")


result = run_pipeline(url)
