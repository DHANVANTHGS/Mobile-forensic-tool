from datetime import datetime

def convert_time(time):
     return datetime.fromtimestamp(int(time) / 1000).strftime("%Y-%m-%d %H:%M:%S")

def to_millis(dt_str):
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    return int(dt.timestamp() * 1000)

def convert_hrs (sec):
     hr = sec//3600
     sec%=3600
     minu =sec//60
     sec%=60
     duriation = f"{hr:02}:{minu:02}:{sec:02}"
     return duriation 