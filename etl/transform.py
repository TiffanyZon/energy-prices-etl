from datetime import datetime


def format_time(time_str):
    dt = datetime.fromisoformat(time_str)
    return dt.strftime("%Y-%m-%d %H:%M")
