import requests
import json
import time
import random
from . import conf, data, lang

def natural_date(timestamp):
    if timestamp == -1:
        return '无记录'
    res = time.localtime(int(timestamp))
    return time.strftime('%Y-%m-%d %H:%M:%S', res)

def natural_time(timestamp):
    s = timestamp % 60
    m = (timestamp % 3600) // 60
    h = timestamp // 3600
    return f'{h} 时 {m} 分 {s} 秒'

def timestamp():
    return int(time.mktime(time.localtime()))

def is_same_day(ts1, ts2) -> bool:
    return ts1 // 86400 == ts2 // 86400

def handle_morning(qq):
    last_morning = data.get(qq, 'last_morning')
    last_night = data.get(qq, 'last_night')
    now = timestamp()
    if last_morning > last_night:
        msg = lang.no_sleep
    else:
        msg = lang.morning_success % (
            natural_time(now - last_night)
        )
        data.set(qq, 'last_morning', now)
    return msg

def handle_night(qq):
    last_morning = data.get(qq, 'last_morning')
    last_night = data.get(qq, 'last_night')
    now = timestamp()
    if last_night > last_morning:
        msg = lang.no_getup
    else:
        data.set(qq, 'last_night', now)
        msg = lang.night_success % (
            natural_time(now - last_morning)
        )
    return msg
    
def gen_sign_info():
    rp = random.randint(1,100)
    return {
        "rp": rp
    }

def handle_sign(qq):
    last_sign = data.get(qq, 'last_sign')
    now = timestamp()
    msg = ''
    if is_same_day(last_sign, now):
        info = data.get(qq, 'last_sign_info')
        msg = lang.already_sign
    else:
        msg = lang.sign_success
        info = gen_sign_info()
        data.set(qq, 'last_sign', now)
        data.set(qq, 'last_sign_info', info)
    msg += lang.sign % (
        natural_date(last_sign),
        info['rp']
    )
    return msg