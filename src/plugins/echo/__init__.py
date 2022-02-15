from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from . import lang

matcher_echo = on_command('echo', priority=5)

@matcher_echo.handle()
async def main_echo(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().rsplit(max=2)

    if len(args) == 1 and not args[0] == 'help':
        msg = args[0]
    elif len(args) == 2 and args[1].isdecimal():
        msg = args[0] * int(args[1])
    else:
        msg = lang.help_guide

    await matcher_echo.finish(msg)