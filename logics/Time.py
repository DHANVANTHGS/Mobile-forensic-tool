from datetime import datetime

def convert_time(time):
     return datetime.fromtimestamp(int(time) / 1000).strftime("%Y-%m-%d %H:%M:%S")

def to_millis(dt_str):
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    return int(dt.timestamp() * 1000)