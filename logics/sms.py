import subprocess as tool
from result import converter
from Time import convert_time


def sms_data(address='',s_time='',e_time='',status='') :
    conditions=[]
    starting_time=None
    ending_time=None
    if s_time!='' :
       starting_time=convert_time(s_time)
    if e_time!='' :
        ending_time=convert_time(e_time)
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
    result= tool.run(cmd,shell=True,capture_output=True,text=True)
    output = converter(result.stdout)
    return output