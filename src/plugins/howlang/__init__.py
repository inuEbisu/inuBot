from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from inukit import howlang as hl
from . import lang

matcher_howlang = on_command('howlang', priority=5)

@matcher_howlang.handle()
async def main_howlang(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().split(maxsplit=1)

    if len(args) == 2 and args[0] == 'encode':
        try:
            msg = hl.enc(args[1])
        except:
            msg = lang.illegal_input
    elif len(args) == 2 and args[0] == 'decode':
        try:
            msg = hl.dec(args[1])
        except:
            msg = lang.illegal_input
    else:
        msg = lang.help_guide

    await matcher_howlang.finish(msg)