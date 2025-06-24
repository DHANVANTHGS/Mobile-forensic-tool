from result import convert_time
import subprocess as tool

def get_info() :
    cmd = "adb shell getprop "
    console=tool.run(cmd,capture_output=True,shell=True,text=True)
    data = console.stdout
    output = convert_time(data)
    return output