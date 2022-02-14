from . import conf
from inukit.jsondata import JsonData

jdata = JsonData(conf.data_path)

def get(qq, key):
    tmp = jdata.gets((qq, key))
    if tmp == None:
        return -1
    else:
        return tmp

def set(qq, key, value):
    return jdata.sets((qq, key), value)