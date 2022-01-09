from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from . import req, lang

matcher_plugins = on_command('plugins', aliases={'help', '插件', '帮助'}, priority=1)
@matcher_plugins.handle()
async def main_plugins(bot: Bot, event: Event, state: T_State):
    msg = req.handle_plugins()
    await matcher_plugins.finish(msg)
    
matcher_basic = on_command('basic', priority=4)
@matcher_basic.handle()
async def main_basic(bot: Bot, event: Event, state: T_State):
    await matcher_basic.finish(lang.help_guide)