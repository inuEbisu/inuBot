from . import req, lang
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

matcher_sign = on_command('sign', priority=4)
matcher_morning = on_command('morning', aliases={'早安'}, priority=5)
matcher_night = on_command('night', aliases={'晚安'}, priority=5)

@matcher_sign.handle()
async def main_sign(bot: Bot, event: Event, state: T_State):
    await matcher_morning.finish(lang.help)

@matcher_morning.handle()
async def main_morning(bot: Bot, event: Event, state: T_State):
    qq = event.get_user_id()
    msg = req.handle_morning(qq)
    await matcher_morning.finish(msg)

@matcher_night.handle()
async def main_night(bot: Bot, event: Event, state: T_State):
    qq = event.get_user_id()
    msg = req.handle_night(qq)
    await matcher_night.finish(msg)