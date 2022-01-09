from os import stat_result
import requests
import json
import time
from . import conf, data, lang

def natural_date(timestamp):
    res = time.localtime(int(timestamp) / 1000)
    return time.strftime("%Y-%m-%d %H:%M:%S", res)

def diff(d):
    return ("Past", "Present", "Future", "Beyond")[d]

def score_format(score) -> str:
    if not score['rank']:
        score['rank'] = 0
    if not score['date'] and score['time_played']:
        score['date'] = score['time_played']
    return lang.score % (
        score['rank'],
        score['song_id'], diff(score['difficulty']),
        score['score'], score['perfect_count'], score['shiny_perfect_count'],
        score['near_count'], score['miss_count'],
        score['rating'] / 100,
        natural_date(score['date'])
    )

def gen_url(path : str) -> str:
    return conf.url_base + path

def get(path):
    url = gen_url(path)
    req = requests.get(url)
    res = json.loads(req.text)
    if res['success']:
        return res['value']
    else:
        return -1

def get_id_by_username(username):
    return get(f'/api/get_id_by_username/{username}')

def get_info(user_id):
    return get(f'/api/get_user_base/{user_id}')

def get_scores(user_id):
    return get(f'/api/get_scores/{user_id}')

def handle_info(qq):
    user_id = data.get(qq, 'user_id')
    if user_id == -1:
        return lang.no_bind
    info = get_info(user_id)
    msg = lang.user_info % (
        info['name'],
        info['user_code'],
        info['rating'] / 100
    )
    return msg

def handle_recent(qq):
    user_id = data.get(qq, 'user_id')
    if user_id == -1:
        return lang.no_bind
    info = get_info(user_id)
    recent = json.loads(info['recent_score'])
    msg = score_format(recent)
    return msg

def handle_scores(qq) -> tuple:
    user_id = data.get(qq, 'user_id')
    if user_id == -1:
        return lang.no_bind

    scores = get_scores(user_id)
    msg_b30 = lang.scores_b30
    msg_r10 = lang.scores_r10
    for each in scores['b30']:
        msg_b30 += score_format(each)
    for each in scores['r10']:
        msg_r10 += score_format(each)
    
    return msg_b30 + '\n' + msg_r10

def handle_bind(qq, username):
    user_id = data.get(qq, 'user_id')
    if user_id != -1:
        return lang.already_bind

    user_id = get_id_by_username(username)
    if user_id == -1:
        return lang.user_not_found
    data.set(qq, 'user_id', user_id)
    return lang.success

def handle_unbind(qq):
    user_id = data.get(qq, 'user_id')
    if user_id == -1:
        return lang.no_bind
        
    data.set(qq, 'user_id', -1)
    return lang.success
