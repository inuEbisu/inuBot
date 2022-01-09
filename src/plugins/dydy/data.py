import json
import random
import time
from . import conf

def timestamp():
    return int(time.mktime(time.localtime()))

def get(new=True):
    try:
        with open(conf.data_path, 'r', encoding='utf-8') as f:
            data_str = f.read()
        data = json.loads(data_str)

        # 去掉30天外的
        if new:
            data = [each for each in data if timestamp() - each['time'] < 30*24*60*60]
        
        key = random.randint(0, len(data)-1)
        res = data[key]
        return res['value']
    except Exception as e:
        raise e
        print(e)
        return -1

def add(value):
    try:
        with open(conf.data_path, 'r', encoding='utf-8') as f:
            data_str = f.read()
        data = json.loads(data_str)
        res = {
            'time': timestamp(),
            'value': value
        }
        data.append(res)
        data_str = json.dumps(data)
        with open(conf.data_path, 'w+', encoding='utf-8') as f:
            f.write(data_str)
    
        return 0
    except Exception as e:
        print(e)
        return -1