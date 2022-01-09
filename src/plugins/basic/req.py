from nonebot.plugin import plugins
from . import lang

def handle_plugins():
    msg = lang.plugins_1 + '\n'
    for each in plugins:
        msg += each + '\n'
    msg += lang.plugins_2
    return msg