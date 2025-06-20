from datetime import datetime

def convert_time(time):
    t_obj= datetime.strptime(time,"%Y-%m-%d %H:%M:%S")
    return (int(t_obj.timestamp()*1000))