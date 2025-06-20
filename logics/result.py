def converter(s):
    messages=[]
    data_entry={}
    lines=s.strip().split('\n')

    for line in lines :
        if line.startswith('Row') :
            if data_entry :
                messages.append(data_entry)
                data_entry={}
        elif '=' in line :
            key,value=line.split('=',1)
            data_entry[key]=value
        
    if data_entry:
        messages.append(data_entry)
    
    return messages