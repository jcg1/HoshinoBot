import random

from nonebot import on_command

from hoshino import R, Service, priv, util



# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')

sv = Service('chat', manage_priv=priv.SUPERUSER, visible=False)

@sv.on_fullmatch(('沙雕机器人', '沙雕機器人'))
async def say_sorry(bot, ev):
    await bot.send(ev, 'ごめんなさい！嘤嘤嘤(〒︿〒)')


@sv.on_fullmatch(('老婆', 'waifu', 'laopo'), only_to_me=True)
async def chat_waifu(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, R.img('laopo.jpg').cqcode)
    else:
        await bot.send(ev, 'mua~')


@sv.on_fullmatch('老公', only_to_me=True)
async def chat_laogong(bot, ev):
    await bot.send(ev, '你给我滚！', at_sender=True)


@sv.on_command('贴贴', aliases=('贴贴~', ), only_to_me=True)
async def chat_tietie(session):
    await session.send('贴贴~', at_sender=True)

@sv.on_command('对不起', aliases=('优衣对不起', 'ue对不起'), only_to_me=True)
async def chat_sorry(session):
    duibuqi = ['你给我滚！', '带你骨灰扬了！',
               '\n第一次,有了喜欢的人\n还得到了一生的挚友\n两份喜悦相互重叠\n这双重的喜悦又带来了更多更多的喜悦\n本应已经得到了梦幻一般的幸福时光\n然而,为什么,会变成这样？', '明明是我先来的~']
    await session.send(random.choice(duibuqi), at_sender=True)


@sv.on_command('骂我', aliases=('老婆骂我', '找骂', '凌辱', '欺负', '继续', '大声点', '没吃饭么', '你再骂'))
async def chat_sorry(session):
    zuanyulu = ['wdnmd，闸总', '哦~', 'バカ', '変態', '无路赛', 'エロい犬', '八嘎hen tai无路赛', '我给你🐴一锤', '你🐴买菜必超级加倍', '你在想peach',
                '你春田必井', '滚！']
    await session.send(random.choice(zuanyulu), at_sender=True)


@sv.on_command('合刀', aliases=('怎么合刀', '合刀图', '合刀方法'))
async def hedao(session):
    await session.send(R.img('合刀.jpg').cqcode)

@sv.on_fullmatch('mua', only_to_me=True)
async def chat_mua(bot, ev):
    await bot.send(ev, '笨蛋~', at_sender=True)


@sv.on_fullmatch('来点星奏')
async def seina(bot, ev):
    await bot.send(ev, R.img('星奏.png').cqcode)


@sv.on_fullmatch(('我有个朋友说他好了', '我朋友说他好了', ))
async def ddhaole(bot, ev):
    await bot.send(ev, '那个朋友是不是你弟弟？')
    # await util.silence(ev, 30)


@sv.on_fullmatch('我好了')
async def nihaole(bot, ev):
    await bot.send(ev, '不许好，憋回去！')
    # await util.silence(ev, 30)

# ============================================ #


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)



@sv.on_keyword(('会战'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.02:
        await bot.send(ctx, R.img('我的天啊你看看都几度了.jpg').cqcode)


@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('内鬼.png').cqcode)


@sv.on_keyword(('迫害', '加害'))
async def chat_pohai(bot, ctx):
    if random.random() < 0.60:
        await bot.send(ctx, '算我一个！')

nyb_player = f'''{R.img('newyearburst.jpg').cqcode}
正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()

@sv.on_keyword(('春黑', '新黑'))
async def new_year_burst(bot, ev):
    if random.random() < 0.02:
        await bot.send(ev, nyb_player)
