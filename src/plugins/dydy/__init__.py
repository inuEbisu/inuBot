from nonebot.matcher import Matcher
from . import req, lang
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from . import req

matcher = on_command('dydy', priority=5)

@matcher.handle()
async def main_sign(bot: Bot, event: Event, state: T_State):
    qq = event.get_user_id()
    args = str(event.get_message()).strip().split()
    if len(args) == 0:
        msg = req.handle_random()
    else:
        if args[0] == 'help' and len(args) == 1:
            msg = lang.help_guide
        elif args[0] == 'old' and len(args) == 1:
            msg = req.handle_random(new=False)
        else:
            value = ' '.join(args)
            msg = req.handle_add(value)
    await matcher.finish(msg)