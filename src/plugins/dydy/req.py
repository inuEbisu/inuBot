from . import data, lang

def handle_random(new=True):
    res = data.get(new)
    if res == -1:
        return lang.error
    else:
        return res

def handle_add(value):
    res = data.add(value)
    if res:
        return lang.error
    else:
        return lang.succees