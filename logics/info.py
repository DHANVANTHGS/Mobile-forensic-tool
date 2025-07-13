from result import convert_time
import subprocess as tool

def get_info() :
    cmd = "adb shell getprop "
    console=tool.run(cmd,capture_output=True,shell=True,text=True)
    data = console.stdout
    output = convert_time(data)
    return output


def list_dir(path) :
    process = tool.Popen(['adb','shell'], stdin=tool.PIPE,stdout=tool.PIPE,stderr=tool.PIPE,text=True)
    cmd=f"cd {path} \n ls"
    stdout,stderr = process.communicate(cmd)
    if stderr:
        return "sw"
    else :
        return stdout

    
# need to write a code to list the data of current directory