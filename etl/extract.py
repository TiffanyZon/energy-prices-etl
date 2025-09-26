import requests


def extract_data(url):
    response = requests.get(url)
    response.raise_for_status()
    print(response.status_code)
    return response.json()
