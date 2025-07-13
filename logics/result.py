from Time import convert_time
from Time import convert_hrs

def convert_sms(s):
    print(s)
    messages=[]
    data_entry={}
    lines=s.strip().split('\n')
    required_details=["type","address","person","date_sent","protocol","body","locked"]
    for line in lines :
        if line.startswith('Row') :
            if data_entry :
                value=data_entry.get("type")
                if value == "1":
                     data_entry["address"] = "sent by " + data_entry["address"]
                elif value == "2":
                     data_entry["address"] = " sent to "+ data_entry["address"]
                messages.append(data_entry)
                data_entry={}
        elif '=' in line :
            key,value=line.split('=',1)
            key=key.strip()
            value=value.strip()
            if(key in required_details):
               if key=="date_sent" :
                   value = convert_time(value)
               if key=="protocol" :
                   if value =="0" :
                       value = "SMS"
                   elif value =="1" :
                       value = "MMS"
               data_entry[key]=value
        
    if data_entry:
        value=data_entry.get("type")
        if value == "1":
            data_entry["address"] = "sent by" + data_entry["address"]
        elif value == "2":
             data_entry["address"] = " sent to "+ data_entry["address"]
        messages.append(data_entry)
    
    return messages

def convert_property(s):
    messages=[]
    data_entry={}
    lines=s.strip().split('\n')
    required_details = ["ro.serialno", "ro.boot.serialno", "ro.product.model", "ro.build.version.release", "ro.build.fingerprint", "ro.boot.flash.locked", "net.hostname"]
    for line in lines :
        if line.startswith('Row') :
            if data_entry :
                messages.append(data_entry)
                data_entry={}
        elif '=' in line :
            key,value=line.split('=',1)
            key=key.strip()
            value=value.strip()
            if key in required_details :
                if key == "ro.serialno" :
                    key="Serial number"
                elif key == "ro.boot.serialno" :
                    key = "Bootloader Serial number"
                elif key == "ro.product.model" :
                    key = "Device Model"
                elif key == "ro.build.version.release" :
                    key = " OS Version"
                elif key =="ro.build.fingerprint" :
                    key = "FingerPrint"
                elif key =="ro.boot.flash.locked":
                    key = "Bootloader state"
                    if value == "0" :
                        value ="Unlocked"
                    else :
                        value ="locked"
                elif key == "net.hostname":
                    key = "Network connected"
                data_entry[key]=value
        
    if data_entry:
        messages.append(data_entry)

    return messages

def convert_ph(s):
    messages=[]
    data_entry={}
    lines=s.strip().split('\n')
    for line in lines:
        if line.startswith('Row'):
            messages.append(data_entry)
            data_entry={}
        elif '=' in line:
            key,value=line.split('=',1)
            key=key.strip()
            value=value.strip()
            if key == "date":
                value=convert_time(value)
            if key == "type" :
                if value == "1":
                    value = "Incoming call"
                elif value =="2":
                    value = "Outgoing call"
                elif value =="3":
                    value = "Missed call"
                elif value =="4":
                    value = "Voice mail"
                elif value =="5":
                    value ="Rejected call"
                elif value =="6":
                    value = "Blocked Call"
                elif value =="7":
                    value ="Answered externally"
            if key =="duration" :
                value = convert_hrs(value)
            if key=="name" and value == "null":
                value = "Unknown Contact"
            data_entry[key]=value
        
    if data_entry:
        messages.append(data_entry)

    return messages