import subprocess as tool
from result import convert_sms
from Time import to_millis

def call_log(number=' ',date=' ',dur=' ',Type=' ',conc=' '):
    cond=[]
    if number != ' ':
        cond.append(f"number ='{number}'")
    if date != ' ':
        date = to_millis(date)
        cond.append(f"date ={date}")
    if dur != ' ':
        cond.append( f"duration > {dur}")
    if conc !=' ':
        cond.append(f"name ='{conc}'")
    if type !=' ':
        cond.append(f"type ={type}")
    
    cmd = "adb shell content query --uri content://call_log/calls"
    if cond :
        condition = ' AND '.join(cond)
        cmd +=f' --where "{condition}"'
    print(cmd)
    console= tool.run(cmd,shell=True,capture_output=True,text=True)
    data = convert_sms(console.stdout)
    return data
