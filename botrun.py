import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)
tamingpoint = []

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)
@bot.command()
async def 진돌아(ctx):
    await ctx.send('월월')
@bot.command()
async def 길들이기(ctx,*,text):
	#https://kr.piliapp.com/symbol/dice/
    taming0={1:'성공',2:'실패'}#딕셔너리
    embed = discord.Embed(title="길들이는중", color=0x4432a8)
    dice1=random.randrange(1,3)
    dice11=taming0[dice1]
    embed.add_field(name="1번째시도",value=f"{dice11}",inline=True)
    if dice11 == "성공":
        await ctx.send(f"{text}님 길들이기 포인트 1 획득")
        tamingpoint.append(f"{text}")
    if dice11 == "실패":
        if tamingpoint.count(text) != 0:
            tamingpoint.remove(text)
    await ctx.send(embed=embed)
@bot.command()
async def 길들이기포인트(ctx, *, text):
    await ctx.send(tamingpoint.count(text))
bot.run('MTA3OTIxMzI3MzE4ODEzOTA1OQ.Ga6s_-.W7MrS58VXuZhPGJcbJ56h4HphOvjG_ofmSPgMU')