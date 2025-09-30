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


def max_price(data):
    return max(record["SEK_per_kWh"] for record in data)


def min_price(data):
    return min(record["SEK_per_kWh"] for record in data)


def mean_price(data):
    prices = [record["SEK_per_kWh"] for record in data]
    return float(sum(prices) / len(prices))


data = extract_data(url)
max_price_value = max_price(data)
min_price_value = min_price(data)
mean_price_value = mean_price(data)
print(f"Day: {today} \nMax price: {max_price_value:.4f} SEK/kWh")
print(f"Min price: {min_price_value:.4f} SEK/kWh")

print(f"Mean price: {mean_price_value:.4f} SEK/kWh")
