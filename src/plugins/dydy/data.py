import random
from . import conf
from inukit.timestamp import timestamp_now as timestamp
from inukit.jsondata import JsonData

jdata = JsonData(conf.data_path)

def get(new=True):
    data = jdata.read()
    if new: # 去掉30天外的
        data = [each for each in data if timestamp() - each['time'] < 30*24*60*60]
    key = random.randint(0, len(data)-1)
    res = data[key]
    return res['value']

def add(value):
    data = jdata.read()
    res = {
        'time': timestamp(),
        'value': value
    }
    data.append(res)
    jdata.write(data)
    return 0