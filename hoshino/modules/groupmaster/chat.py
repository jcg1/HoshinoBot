import random
from datetime import timedelta

from nonebot import on_command
from hoshino import util
from hoshino.res import R
from hoshino.service import Service, Privilege as Priv

# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'))
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')

sv = Service('chat', manage_priv=Priv.SUPERUSER, visible=False)

@sv.on_command('沙雕机器人', aliases=('沙雕機器人',), only_to_me=False)
async def say_sorry(session):
    await session.send('ごめんなさい！嘤嘤嘤(〒︿〒)')

@sv.on_command('老婆', aliases=('waifu', 'laopo'), only_to_me=True)
async def chat_waifu(session):
    if not sv.check_priv(session.ctx, Priv.SUPERUSER):
        await session.send(R.img('laopo.jpg').cqcode)
    else:
        await session.send('mua~')

@sv.on_command('老公', only_to_me=True)
async def chat_laogong(session):
    await session.send('你给我滚！', at_sender=True)

@sv.on_command('mua', only_to_me=True)
async def chat_mua(session):
    await session.send('笨蛋~', at_sender=True)

@sv.on_command('来点星奏', only_to_me=False)
async def seina(session):
    await session.send(R.img('星奏.png').cqcode)

@sv.on_command('我有个朋友说他好了', aliases=('我朋友说他好了', ), only_to_me=False)
async def ddhaole(session):
    await session.send('那个朋友是不是你弟弟？')
    await util.silence(session.ctx, 30)

@sv.on_command('我好了', only_to_me=False)
async def nihaole(session):
    await session.send('不许好，憋回去！')
    await util.silence(session.ctx, 30)

@sv.on_command('对不起', aliases=('优衣对不起', 'ue对不起'), only_to_me= True)
async def chat_sorry(session):
    duibuqi = ['你给我滚！', '带你骨灰扬了！', '\n第一次,有了喜欢的人\n还得到了一生的挚友\n两份喜悦相互重叠\n这双重的喜悦又带来了更多更多的喜悦\n本应已经得到了梦幻一般的幸福时光\n然而,为什么,会变成这样？', '明明是我先来的~']
    await session.send(random.choice(duibuqi), at_sender=True)

@sv.on_command('骂我', aliases =('老婆骂我','找骂','凌辱','欺负','继续','大声点','没吃饭么'))
async def chat_sorry(session):
    zuanyulu = ['wdnmd，闸总','哦~','バカ','変態','无路赛','エロい犬','八嘎hen tai无路赛','我给你🐴一锤','你🐴买菜必超级加倍','你在想peach','你春田必井','滚！']
    await session.send(random.choice(zuanyulu), at_sender=True)

# ============================================ #

@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)

@sv.on_keyword(('会战', '刀'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.03:
        await bot.send(ctx, R.img('我的天啊你看看都几度了.jpg').cqcode)

@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

@sv.on_keyword(('迫害', '加害'))
async def chat_pohai(bot, ctx):
    if random.random() < 0.60:
        await bot.send(ctx, '算我一个！')