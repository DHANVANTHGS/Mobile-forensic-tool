from logics.sms import get_sms
from logics.info import get_info
from logics.calllog import call_log
from logics.install import check


if __name__ == "__main__":
    check()

def sms(address='',s_time='',e_time='',status='') :
    return get_sms(address,s_time,e_time,status)

def properties():
    return get_info()

def call(number=' ',date=' ',dur=' ',Type=' ',conc=' '):
    return call_log(number,date,Type,conc)