from nonebot import on_notice, NoticeSession
from hoshino import util, R

import hoshino
from hoshino import Service
from hoshino.typing import NoticeSession

sv1 = Service('group-leave-notice')

@sv1.on_notice('group_decrease.leave')
async def leave_notice(session: NoticeSession):
    await session.send(f"{session.ctx['user_id']}退群了。")

@sv2.on_notice('group_increase')
async def increace_notice(session:NoticeSession):
    pic = R.img(f"欢迎新人.jpg").cqcode
    await session.send(f"\n欢迎加入~"
                       f"\n萌新你好~我叫优衣 ≧▽≦"
                       f"\n是一只AI娘~请多多指教哟！"
                       f"\n{pic}", at_sender=True)

sv2 = Service('group-welcome')

# @sv2.on_notice('group_increase')
# async def increace_welcome(session: NoticeSession):
#
#     if session.event.user_id == session.event.self_id:
#         return  # ignore myself
#
#     welcomes = hoshino.config.groupmaster.increase_welcome
#     gid = session.event.group_id
#     if gid in welcomes:
#         await session.send(welcomes[gid], at_sender=True)
#     elif 'default' in welcomes:
#         await session.send(welcomes['default'], at_sender=True)
