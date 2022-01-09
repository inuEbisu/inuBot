import json
from . import conf

def get(qq, key):
    try:
        with open(conf.data_path, 'r') as f:
            data_str = f.read()
        data = json.loads(data_str)
        res = data[qq][key]
        return res
    except Exception as e:
        print(e)
        return -1

def set(qq, key, value):
    try:
        with open(conf.data_path, 'r') as f:
            data_str = f.read()
        data = json.loads(data_str)

        # data[qq] = {}
        data[qq][key] = value

        data_str = json.dumps(data)
        with open(conf.data_path, 'w+') as f:
            f.write(data_str)
    
        return 0
    except Exception as e:
        print(e)
        return -1