from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import random as r
from . import lang
matcher_random = on_command('random', aliases={'r'}, priority=5)

def is_int(i: object) -> bool:
    try:
        int(i)
        return True
    except ValueError:
        return False

def is_all_int(t: tuple) -> bool:
    return all([is_int(i) for i in t])

def a_split(s: str) -> list:
    tmp = s.split(',')
    if len(tmp) == 1:
        tmp = list(s)
    return tmp

@matcher_random.handle()
async def main_random(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().split()

    try:
        if len(args) == 0:
            msg = str(r.randint(0, 100))
        elif len(args) == 1 and is_all_int(args):
            ints = [str(r.randint(0, 100)) for _ in range(0, int(args[0]))]
            msg = ' '.join(ints)
        elif len(args) == 2 and is_all_int(args):
            msg = str(r.randint(int(args[0]), int(args[1])))
        elif len(args) == 3 and is_all_int(args):
            ints = [str(r.randint(int(args[0]), int(args[1]))) for _ in range(0, int(args[2]))]
            msg = ' '.join(ints)
        elif len(args) == 1 and (args[0] == 'bool' or args[0] == 'b'):
            msg = str(r.choice((True, False)))
        elif len(args) == 2 and (args[0] == 'shuffle' or args[0] == 's'):
            tmp = a_split(args[1])
            r.shuffle(tmp)
            msg = ','.join(tmp)
        elif len(args) == 2 and (args[0] == 'choice' or args[0] == 'c'):
            tmp = a_split(args[1])
            msg = r.choice(tmp)
        elif len(args) == 3 and (args[0] == 'choice' or args[0] == 'c') and is_int(args[2]):
            tmp = a_split(args[1])
            amount = int(args[2])
            msg = ','.join(r.sample(tmp, k=amount))
        else:
            msg = lang.help_guide
    except Exception as e:
        msg = lang.err % (str(e),)
    
    await matcher_random.finish(msg)