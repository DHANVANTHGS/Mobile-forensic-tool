from logics.sms import get_sms
from logics.info import get_info

def sms(address='',s_time='',e_time='',status='') :
    return get_sms(address,s_time,e_time,status)

def properties():
    return get_info()