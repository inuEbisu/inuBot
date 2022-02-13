from . import conf
from inukit.jsondata import JsonData

jdata = JsonData(conf.data_path)

def get(qq, key):
    return jdata.gets((qq, key))

def set(qq, key, value):
    return jdata.sets((qq, key), value)