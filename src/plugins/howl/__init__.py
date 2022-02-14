from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from . import lang
import random

def get_howl():
    char = ('嗷','呜','汪')
    length = random.randint(5,20)
    count = 0
    msg = ''
    while length != count:
        subscript = random.randint(0,2)
        msg += char[subscript]
        count += 1
    return msg

matcher_howl = on_command('howl', priority=5)

@matcher_howl.handle()
async def main_howl(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().split()
    
    if len(args) == 0:
        msg = get_howl()
    else:
        msg = lang.help_guide
    
    await matcher_howl.finish(msg)