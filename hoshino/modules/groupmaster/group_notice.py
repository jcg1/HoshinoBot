from nonebot import on_notice, NoticeSession
from hoshino import util, R


@on_notice('group_decrease.leave')
async def leave_notice(session:NoticeSession):
    cfg = util.load_config(__file__)
    no_leave_notice_group = cfg.get('no_leave_notice', [])
    if session.ctx['group_id'] not in no_leave_notice_group:
        await session.send(f"{session.ctx['user_id']}退群了。")


@on_notice('group_increase')
async def increace_notice(session:NoticeSession):
    pic = R.img(f"欢迎新人.jpg").cqcode
    await session.send(f"\n欢迎加入~"
                       f"\n萌新你好~我叫优衣 ≧▽≦"
                       f"\n是一只AI娘~请多多指教哟！"
                       f"\n{pic}", at_sender=True)


@on_notice('group_decrease.kick_me')
async def kick_me_alert(session:NoticeSession):
    group_id = session.event.group_id
    operator_id = session.event.operator_id
    coffee = session.bot.config.SUPERUSERS[0]
    await session.bot.send_private_msg(self_id=session.event.self_id, user_id=coffee, message=f'被Q{operator_id}踢出群{group_id}')
