from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from inukit import rand
from . import lang
matcher_random = on_command('random', priority=5)

def is_int(i: object) -> bool:
    try:
        int(i)
        return True
    except ValueError:
        return False

def is_all_int(t: tuple) -> bool:
    return all([is_int(i) for i in t])

@matcher_random.handle()
async def main_random(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().split()

    if len(args) == 0:
        msg = str(rand.rand_a_int(0, 100))
    elif len(args) == 1 and is_all_int(args):
        ints = rand.rand_some_int(0, 100, int(args[0]))
        tmp = [str(i) for i in ints]
        msg = ' '.join(tmp)
    elif len(args) == 2 and is_all_int(args):
        msg = str(rand.rand_a_int(int(args[0]), int(args[1])))
    elif len(args) == 3 and is_all_int(args):
        ints = rand.rand_some_int(int(args[0]), int(args[1]), int(args[2]))
        tmp = [str(i) for i in ints]
        msg = ' '.join(tmp)
    elif len(args) == 1 and args[0] == 'bool':
        msg = str(rand.rand_bool())
    else:
        msg = lang.help_guide

    await matcher_random.finish(msg)