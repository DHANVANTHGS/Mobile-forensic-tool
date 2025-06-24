import subprocess as tool
from result import convert_sms
from Time import to_millis


def get_sms(address='',s_time='',e_time='',status='') :
    conditions=[]
    starting_time=None
    ending_time=None
    if s_time!='' :
       starting_time=to_millis(s_time)
    if e_time!='' :
        ending_time=to_millis(e_time)
    cmd = 'adb shell content query --uri content://sms '
    if starting_time :
        conditions.append(f"date >{starting_time}")
        if(ending_time):
            conditions.append(f"date < {ending_time}")
    if status =='sent' :
        conditions.append("type = 2")
    elif status =='received' :
        conditions.append("type = 1")
    if address!='':
        conditions.append(f"address='{address}'")
    if conditions:
        condition = ' AND '.join(conditions)
        cmd += f" --where {condition}"

    print(cmd)
    console= tool.run(cmd,shell=True,capture_output=True,text=True)
    data = convert_sms(console.stdout)
    return data
