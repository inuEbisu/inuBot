from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from . import req, lang

matcher = on_command('arcana', aliases={'acn'}, priority=5)

@matcher.handle()
async def main(bot: Bot, event: Event, state: T_State):
    qq = event.get_user_id()
    args = str(event.get_message()).strip().split()
    msg = lang.connection_error
    if len(args) > 0:
        if args[0] == 'help' and len(args) == 1:
            msg = lang.help_guide
        elif args[0] == 'info' and len(args) == 1:
            msg = req.handle_info(qq)
        elif args[0] == 'bind' and len(args) == 2:
            username = args[1]
            msg = req.handle_bind(qq, username)
        elif args[0] == 'recent' and len(args) == 1:
            msg = req.handle_recent(qq)    
        elif args[0] == 'score' and len(args) == 1:
            msg = req.handle_scores(qq)
        elif args[0] == 'unbind' and len(args) == 1:
            msg = req.handle_unbind(qq) 
        else:
            msg = lang.args_error
    else:
        msg = lang.args_error
    await matcher.finish(msg)