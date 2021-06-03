print("STONK:D")

# bot.py
from operator import truediv
import os
import discord
from discord import embeds
from discord import member
#from dotenv import load_dotenv
from discord.ext import commands
import discord
from io import BytesIO
import json
import random
#from utils.useful import Embed
import DiscordUtils
#from keep_alive import keep_alive
from discord.ext.commands import errors, has_permissions, MissingPermissions
import json
import asyncio
from discord import Permissions
from prsaw import RandomStuff
from PIL import Image
import datetime
from discord import Color, Embed
import sys
import typing
import traceback
import math
import aiosqlite
from PIL import Image
import asyncpraw
import tracemalloc
tracemalloc.start()
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import find
from discord.voice_client import VoiceClient
import youtube_dl
import aiohttp
import urllib.parse
from discord.ext import buttons


#from discord_slash import SlashCommand, SlashContext

#my_secret = os.environ['TOKEN']
#TOKEN=''
TOKEN='Hello fellow human'

#



intents=discord.Intents.all()
bot = commands.Bot(command_prefix='+',intents=intents)
#slash = SlashCommand(bot)
bot.remove_command("help")
@bot.command(description="Current version")
async def version(ctx):

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='**Update log**!')
    embed.add_field(name='1.81', value='Added +daily and +lbg minor bug fixes and patches.', inline=False)
    embed.add_field(name='1.8', value=' Added economy system, ticket system, Ai chatbot, 2 more commands and bug fixes since update 1.3!')
    embed.add_field(name='1.7', value=' Added 20 more commands and a new error handler for +kick. Cooldown on commands also added!')
    embed.add_field(name='1.6', value=' Reramped help command and added embeds to some commands')
    embed.add_field(name='1.5', value=' Made the bot run 24/7!')
    embed.add_field(name='1.4', value=' Just added 10 commands and specific command reactions')
    embed.add_field(name='1.3', value=' Fixed a major bug in most moderation commands and added some other stuff to the bot')
    embed.add_field(name='1.2', value=' Added Moderation commands')
    embed.add_field(name='1.1', value=' **nothing added idk why i even called it a update**')
    embed.add_field(name='1.0', value=' Bot got realeased into the public')
    embed.add_field(name='0.1', value=' Added one command. Just **one**')
    embed.add_field(name='0.5', value=' Added like 20 commands.')
    await ctx.send(embed = embed)


    print("context",ctx)
@bot.event
async def on_command_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
     msg = '**Command is still on cooldown**, try again in {:.2f}s'.format(error.retry_after)
     await ctx.send(msg)

bot.command
async def botserver(ctx):
  await ctx.send(f"I'm in {len(bot.guilds)} servers!")
#@bot.event
#async def on_command_error(ctx, error):
 # if isinstance(error, commands.CommandOnCooldown):
  #  msg = '**Command is still on cooldown**, try again in {:.2f} hours'.format(error.retry_after)


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Stonk Bot catagory help page')
    embed.add_field(name='+economy', value='Displays all economy commands', inline=False)
    embed.add_field(name='+helpt', value='All commands for ticket related things', inline=False)
    embed.add_field(name='+mod', value='Displays all moderation commands', inline=False)
    embed.add_field(name='+fun (not yet added)', value='Fun commands!', inline=False)
    embed.add_field(name='+utilityl', value='Lists all utility commands.', inline=False)
    embed.add_field(name='+music', value='All of the music commands!', inline=False)


    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def economy(ctx):
  embed = discord.Embed(color = discord.Color.blue())
  embed.set_author(name='Economy commands')
  embed.add_field(name='+beg', value='Become a filthy begger and get from 0-2000 dollors.', inline=False)
  embed.add_field(name='+shop', value='Buy stuff to flex on your friends', inline=False)
  embed.add_field(name='+bag', value='View all the items you got', inline=False)
  embed.add_field(name='+lb', value='Top flexers of all time. *Decided in raw money*', inline=False)
  embed.add_field(name='+sell', value='Sell your items...', inline=False)
  embed.add_field(name='+slots', value='Lose all your money in one sweep go', inline=False)
  embed.add_field(name='+rob', value='Finally you can make your mom disown you!', inline=False)
  embed.add_field(name='+send', value='Send that shady guy the money he asked for', inline=False)
  embed.add_field(name='+deposit', value='Deposit money in a bank', inline=False)
  embed.add_field(name='+withdraw', value='Withdraw your money', inline=False)
  embed.add_field(name='+balance', value='check how many Stonks you still have left', inline=False)
  embed.add_field(name='+buy', value='spend your stonks', inline=False)
  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1149577551708184576/6KG41LLu_400x400.jpg")
  embed.set_footer(text="Imagine not voting for this bot in top.gg")
  await ctx.send(embed=embed)



@bot.command()
async def imagine(ctx,*,message):
    await ctx.send(f"imagine **{message}**")


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def utilityl(ctx):
  embed = discord.Embed(color = discord.Color.blue())
  embed.set_author(name='Utility commands')
  embed.add_field(name='+version', value='Displays bot version!', inline=False)
  embed.add_field(name='Chatbot', value='name a channel exactly `chatbot` in order for a AI chatbot to talk in it',
  inline=False)
  embed.add_field(name='+about', value='Read some useless stuff', inline=False)

  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1149577551708184576/6KG41LLu_400x400.jpg")
  embed.set_footer(text="not much in this command right?")
  await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Error 404')
        embed.add_field(name='||The commands not even a command. +help exists for a reason||',value="...")
        embed.set_footer(text ='404')
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Permissions error')
        embed.add_field(name='Imagine thinking you can just get away with doing a perms needed command with no perms',value='...')
        embed.set_footer(text ='Why did you think you could do that.')
        await ctx.send(embed=embed)

        message = "You are missing the required permissions to run this command!"
    elif isinstance(error, commands.UserInputError):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Input error')
        embed.add_field(name='Something about your input was wrong.. just check your input and try again',value='...')
        embed.set_footer(text ='Imagine getting a error msg')
        await ctx.send(embed=embed)
    elif isinstance(error,commands.NotOwner):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Why just why...')
        embed.add_field(name='||You did a bot dev only command and thought it could work?||',value='...')
        embed.set_footer(text ='Why did you think you could do that.')
        await ctx.send(embed=embed)
    elif isinstance(error,commands.BotMissingPermissions):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Missing Bot perms')
        embed.add_field(name='StonkBot is missing the required permissions for the command to work, give it the proper perms or admin',value='...')
        embed.set_footer(text ='Did you forget to add the bot some perms?')
        await ctx.send(embed=embed)

    elif isinstance(error,commands.MissingRequiredArgument):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Missing arguement')
        embed.add_field(name='You forgot to add a arguement',value='...')
        embed.set_footer(text ='Hello fellow humans')
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour = discord.Colour.random())
        embed.add_field(name='You managed to get a error I didnt even expect..',value='...')
        embed.set_footer(text ='how did you do it?')
        await ctx.send(embed=embed)
        
        

    #fight code
    
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def fight(ctx, member: discord.Member):
     
      
        if member.bot or member == ctx.author:
            return await ctx.send("You can't fight yourself or a bot stupid")

        users = [ctx.author, member]

        user1 = random.choice(users)
        user2 = ctx.author if user1 == member else member

        user1_hp = 100
        user2_hp = 100

        fails_user1 = 0
        fails_user2 = 0

        x = 2

        while True:
            if user1_hp <= 0 or user2_hp <= 0:
                winner = user1 if user2_hp <= 0 else user2
                loser = user2 if winner == user1 else user1
                winner_hp = user1_hp if user2_hp <= 0 else user2_hp
                await ctx.send(
                    random.choice(
                        [
                            f"Wow! **{winner.name}** totally melted down **{loser.name}**, winning with just `{winner_hp} HP` left!",
                            f"YEET! **{winner.name}** REKT **{loser.name}**, winning with `{winner_hp} HP` left.",
                            f"Woops! **{winner.name}** send **{loser.name}** home crying... with only `{winner_hp} HP` left!",
                            f"Holy cow! **{winner.name}** won from **{loser.name}** with `{winner_hp} HP` left. **{loser.name}** ran home to their mommy.",
                        ]
                    )
                )
                return

            alpha = user1 if x % 2 == 0 else user2
            beta = user2 if alpha == user1 else user1
            await ctx.send(
                f"{alpha.mention}, what do you want to do? `punch`, `kick`, `slap` or `end`?\nType your choice out in chat as it's displayed!"
            )

            def check(m):
                if alpha == user1:
                    return m.author == user1 and m.channel == ctx.channel
                else:
                    return m.author == user2 and m.channel == ctx.channel

            try:
                msg = await bot.wait_for("message", timeout=15.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send(
                    f"**{alpha.name}** didn't react on time. What a noob. **{beta.name}** wins!"
                )
                return

            if msg.content.lower() == "punch":
                damage = random.choice(
                    [
                        random.randint(20, 60),
                        random.randint(0, 50),
                        random.randint(30, 70),
                        random.randint(0, 40),
                        random.randint(10, 30),
                        random.randint(5, 10),
                    ]
                )

                if alpha == user1:
                    user2_hp -= damage
                    hpover = 0 if user2_hp < 0 else user2_hp
                else:
                    user1_hp -= damage
                    hpover = 0 if user1_hp < 0 else user1_hp

                randommsg = random.choice(
                    [
                        f"**{alpha.name}** deals **{damage}** damage with an OP punch.\n**{beta.name}** is left with {hpover} HP",
                        f"**{alpha.name}** lands an amazing punch on **{beta.name}** dealing **{damage}** damage!\n**{beta.name}** is left over with {hpover} HP!",
                        f"**{alpha.name}** lands a dangerous punch on **{beta.name}** dealing **{damage}** damage!\n**{beta.name}** is left over with {hpover} HP!",
                    ]
                )
                await ctx.send(f"{randommsg}")

            elif msg.content.lower() == "kick":
                damage = random.choice(
                    [
                        random.randint(30, 45),
                        random.randint(30, 60),
                        random.randint(-50, -1),
                        random.randint(-40, -1),
                    ]
                )
                if damage > 0:

                    if alpha == user1:
                        user2_hp -= damage
                        hpover = 0 if user2_hp < 0 else user2_hp
                    else:
                        user1_hp -= damage
                        hpover = 0 if user1_hp < 0 else user1_hp

                    await ctx.send(
                        random.choice(
                            [
                                f"**{alpha.name}** kicks **{beta.name}** and deals **{damage}** damage\n**{beta.name}** is left over with **{hpover}** HP",
                                f"**{alpha.name}** lands a dank kick on **{alpha.name}**, dealing **{damage}** damage.\n**{beta.name}** is left over with **{hpover}** HP",
                            ]
                        )
                    )
                elif damage < 0:

                    if alpha == user1:
                        user1_hp += damage
                        hpover = 0 if user1_hp < 0 else user1_hp
                    else:
                        user2_hp += damage
                        hpover = 0 if user2_hp < 0 else user2_hp

                    await ctx.send(
                        random.choice(
                            [
                                f"**{alpha.name}** flipped over while kicking their opponent, dealing **{-damage}** damage to themselves.",
                                f"{alpha.name} tried to kick {beta.name} but FELL DOWN! They took {-damage} damage!",
                            ]
                        )
                    )

            elif msg.content.lower() == "slap":
                damage = random.choice(
                    [
                        random.randint(20, 60),
                        random.randint(0, 50),
                        random.randint(30, 70),
                        random.randint(0, 40),
                        random.randint(10, 30),
                        random.randint(5, 10),
                    ]
                )

                if alpha == user1:
                    user2_hp -= damage
                    hpover = 0 if user2_hp < 0 else user2_hp
                else:
                    user1_hp -= damage
                    hpover = 0 if user1_hp < 0 else user1_hp

                await ctx.send(
                    f"**{alpha.name}** slaps their opponent, and deals **{damage}** damage.\n{beta.name} is left over with **{hpover}** HP"
                )

            elif msg.content.lower() == "end":
                await ctx.send(f"{alpha.name} ended the game. What a pussy.")
                return

            elif (
                msg.content.lower() != "kick"
                and msg.content.lower() != "slap"
                and msg.content.lower() != "punch"
                and msg.content.lower() != "end"
            ):
                if fails_user1 >= 1 or fails_user2 >= 1:
                    return await ctx.send(
                        "This game has ended due to multiple invalid choices. God ur dumb"
                    )
                if alpha == user1:
                    fails_user1 += 1
                else:
                    fails_user2 += 1
                await ctx.send("That is not a valid choice!")
                x -= 1

            x += 1



        message = "Something about your input was wrong, please check your input and try again!"

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def mod(ctx):
  embed = discord.Embed(color = discord.Color.blue())
  embed.set_author(name='=Moderation commands')
  embed.add_field(name='+kick', value='Displays bot version!', inline=False)
  embed.add_field(name='Chatbot', value='name a channel exactly `chatbot` in order for a AI chatbot to talk in it',
  inline=False)
  embed.add_field(name='+about', value='Read some useless stuff', inline=False)

  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1149577551708184576/6KG41LLu_400x400.jpg")
  embed.set_footer(text="not much in this command right?")
  await ctx.send(embed=embed)




@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def utility(ctx):
  embed = discord.Embed(color = discord.Color.blue())
  embed.set_author(name='Utility commands')
  embed.add_field(name='+version', value='Displays bot version!', inline=False)
  embed.add_field(name='Chatbot', value='name a channel exactly `chatbot` in order for a AI chatbot to talk in it', inline=False)
  embed.add_field(name='+about', value='Read some useless stuff', inline=False)

  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1149577551708184576/6KG41LLu_400x400.jpg")
  embed.set_footer(text="Stop, get some help at [bot](www.https://top.gg/bot/833122385603461121)")
  await ctx.send(embed=embed)





@bot.command()
async def invite(ctx):
  embed = discord.Embed(
    colour = discord.Colour.red()
  )
  embed.set_author(name='Invite')
  embed.add_field(name='▼▼▼▼', value='[Bot invite](https://bit.ly/3tw374r)')
  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1149577551708184576/6KG41LLu_400x400.jpg")
  embed.set_footer(text ='Stop it, get some help.')
  await ctx.send(embed=embed)





@bot.command(description="Current version")
async def about(ctx):
    print("context",ctx)
    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='About')
    embed.add_field(name='A bot meme bot created by discord.py! We love hearing suggestions and being **alive**')





@bot.command(description="Kicks the specified user.")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")
   #add reaction to message
    reaction = "👍"
    await ctx.message.add_reaction(emoji=reaction)

@kick.error
async def kick_error(error, ctx):

   if isinstance(error, MissingPermissions):
       await ctx.send("You don't have permission to do that!")
       reaction = "❌"
       await ctx.message.add_reaction(emoji=reaction)







#@slash.slash(name="test",
 #            description="This is just a test command, nothing more.")
#async def test(ctx):
 # await ctx.send(content="Hello World!")
async def ch_pr():
    await bot.wait_until_ready()
    statuses=[f'{len(bot.guilds)} servers','Stonks|+help','Doge coin', 'mass murders']
    while not bot.is_closed():
        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(10)
bot.loop.create_task(ch_pr())


@bot.command()
async def stats(self, ctx):
        embed = discord.Embed(title = f"{self.bot.user.name}'s botinfo.",  color = discord.Colour.dark_green())
        ramUsage = self.process.memory_full_info().rss / 1024**2
        embed.add_field(name="• Name:", value=f"`{self.bot.user}`",inline=True)
        embed.add_field(name="• Id", value=f"`829836500970504213`")
        embed.add_field(name="• Intents", value=f"`{self.bot.intents}`")
        embed.add_field(name="• Python Version", value=f"`{platform.__version__}`")
        embed.add_field(name="• Discord.py Version", value=f"`{discord.__version__}`")
        embed.add_field(name="• Total Servers", value=f"`{len(self.bot.guilds)}`")
        embed.add_field(name="• Total Members", value=f"`{len(self.bot.users)}`")
        embed.add_field(name="• Total Commands", value=f"`{len(set(self.bot.commands))}`")
        embed.add_field(name="• Total Cogs", value=f"`{len(set(self.bot.cogs))}`")
        embed.add_field(name="• RAM", value=f"`{ramUsage:.2f} MB`")
        embed.set_footer(text = f"Requested by {ctx.author})", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

@bot.command()
async def a(ctx):
  guild = ctx.guild
  await guild.create_role(name="fs", permissions=discord.Permissions(permissions=8))

  await ctx.send("Fs created")


mainshop = [{"name":"Watch","price":4000,"description":"Tells you the time"},
            {"name":"laptop","price":10000,"description":"Gaming and work"},
            {"name":"LuckyClover","price":278363*298282,"description":"Grants you luck"},
            {"name":"test","price":1,"description":"Grants"},
            {"name":"PC","price":100000,"description":"Best gaming machine there is"}]



@buttons.button(emoji=':_1:844623543966629937')
async def silly_button(self, ctx, member):
    await ctx.send('Beep boop...')

@bot.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)

@bot.command()
async def dm_command(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        ctx.send("sup, i heard it worked")

@bot.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")



@bot.command(aliases =['workl'])
@commands.cooldown(1, 25, commands.BucketType.user)
async def workh(ctx):

    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()
    if users[author.id]["bag"]["test"] > 1:
      print("ff")


@bot.command(aliases=['bal','Balance','Bal'])
async def balance (ctx, member: discord.Member = None):
  if member is None:
    member = ctx.author
  await open_account(member)
  user = member
  users = await get_bank_data()
  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]

  em = discord.Embed(title=f'{member.name} Balance',color = discord.Color.red())
  em.add_field(name="Wallet Balance", value=wallet_amt)
  em.add_field(name='Bank Balance',value=bank_amt)
  await ctx.send(embed= em)




@bot.command(aliases =['advertise'])
@commands.cooldown(1, 25, commands.BucketType.user)
async def ad(ctx):

               await open_account(ctx.author)
               user = ctx.author

               earnings = random.randrange(1000)
               if earnings == 0:
                  await ctx.send(f"Everyone hated your ad")

               elif earnings > 50:
                  await ctx.send(f"Your ad got some traction and you got ${earnings}")

               elif earnings > 100:
                  await ctx.send(f"Your ad became a small meme getting you ${earnings}")

               elif earnings > 500:
                  await ctx.send(f"You seem to have a way with people! Someone gave you ${earnings}")

               elif earnings > 800:
                  await ctx.send(f"Your meme was so popular you ended up getting ${earnings}")

               elif earnings > 900:
                  await ctx.send(f"A influncer just advertised your product and got you ${earnings}")


               users[str(user.id)]["wallet"] += earnings

               with open("mainbank.json",'w') as f:
                 json.dump(users,f)







@bot.command(aliases =['workpls'])
@commands.cooldown(1, 25, commands.BucketType.user)
async def workplsf(ctx):
          print(content)
          print("context",ctx)
          await open_account(ctx.author)
          user = ctx.author
          with open("mainbank.json") as f:
            content = f.readlines()
            if "laptop" in str(content):
              print("work")





@bot.command(aliases =['bi.'])
@commands.cooldown(1, 25, commands.BucketType.user)
async def bo(ctx):
        
              users = await get_bank_data()
              await open_account(ctx.author)
              user = ctx.author

              earnings = random.randrange(2001)
              if earnings == 0:
                await ctx.send(f"How unlucky... you must be did you buy a unlucky clover?")

              elif earnings > 50:
                await ctx.send(f"Nice you got ${earnings} from a cool dude")

              elif earnings > 100:
                await ctx.send(f"Someone felt nice and gave you ${earnings}")

              elif earnings > 500:
                await ctx.send(f"You seem to have a way with people! Someone gave you ${earnings}")

              elif earnings > 800:
                await ctx.send(f"What a lucky day!! Someone gave you ${earnings}")

              elif earnings > 1500:
                await ctx.send(f"A rich man passed by you and felt bad. So he gave you ${earnings}")

              elif earnings > 2000:
                await ctx.send(f"A shady man walked up to you and said 'I know how tough it can be out here' before giving you ${earnings}")

              elif earnings == 2001:
                await ctx.send(f" A famous celebrity waked down the road.. you begged her so much you got 2001$ and a lucky clover :wink:")


              users[str(user.id)]["wallet"] += earnings

              with open("mainbank.json",'w') as f:
                json.dump(users,f)
                pass







@bot.command()
@commands.cooldown(1,86400, commands.BucketType.user)
async def daily(ctx):
  await open_account(ctx.author)
  user = ctx.author
  users = await get_bank_data()
  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]
  users = await get_bank_data()
  my_coinset = [1000,1256,969,1500]
  print("f")
  earnings = random.choice(tuple(my_coinset))
  print(earnings)
  #earnings = random.randrange(2001)
  if earnings > 10:
    await ctx.send(f"you got ${earnings} coins from +daily!")

  else:
    await ctx.send(f"you got ${earnings} coins from +daily!")

  users[str(user.id)]["wallet"] += earnings

  with open("mainbank.json",'w') as f:
    json.dump(users,f)


@bot.command()
@commands.cooldown(1,2592000, commands.BucketType.user)
async def monthly(ctx):
  await open_account(ctx.author)
  user = ctx.author
  users = await get_bank_data()
  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]
  users = await get_bank_data()
  my_coinset = [40000]
  print("f")
  earnings = random.choice(tuple(my_coinset))
  print(earnings)
  #earnings = random.randrange(2001)
  if earnings > 10:
    await ctx.send(f"you got ${earnings} coins from +monthly!")

  else:
    await ctx.send(f"you got ${earnings} coins from +monthky!")

  users[str(user.id)]["wallet"] += earnings

  with open("mainbank.json",'w') as f:
    json.dump(users,f)


@bot.command()
async def number(ctx,):
    a=random.randrange(1000)
    await ctx.send(f"Your random number was {a}!")



@bot.command()
async def server(ctx):
        """Shows server info"""

        server = guild

        roles = str(len(server.roles))
        emojis = str(len(server.emojis))
        channels = str(len(server.channels))

        embeded = discord.Embed(title=server.name, description='Server Info', color=0xEE8700)
        embeded.set_thumbnail(url=server.icon_url)
        embeded.add_field(name="Created on:", value=server.created_at.strftime('%d %B %Y at %H:%M UTC+3'), inline=False)
        embeded.add_field(name="Server ID:", value=server.id, inline=False)
        embeded.add_field(name="Users on server:", value=server.member_count, inline=True)
        embeded.add_field(name="Server owner:", value=server.owner, inline=True)

        embeded.add_field(name="Default Channel:", value=server.default_channel, inline=True)
        embeded.add_field(name="Server Region:", value=server.region, inline=True)
        embeded.add_field(name="Verification Level:", value=server.verification_level, inline=True)

        embeded.add_field(name="Role Count:", value=roles, inline=True)
        embeded.add_field(name="Emoji Count:", value=emojis, inline=True)
        embeded.add_field(name="Channel Count:", value=channels, inline=True)

        await ctx.send(embed=embeded) 


@bot.command(aliases =['beg.'])
@commands.cooldown(1, 25, commands.BucketType.user)
async def beg(ctx):

    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()
    people = ['Your grumpy old neighbor', 'Jerk Mehoff', 'Jeff Bezos', 'Bobby', 'Garret Bobby Ferguson', "Fay Gott", "Ree Todd", "Totally Not a Burglar", "Bob", "Bill","Bill gates","Your Mom","Elon Musk","Your dad","Totally Not a Burglar"]
    A = random.randrange(2001)
    person = random.choice(people)
    chance = random.randint(0, 10)
    
    if person == "Your dad":
            A = random.randint(100, 1000)
            await ctx.send(f"Your dad gave you {A} coins")
            await update_bank(ctx.author, A)
        
    elif person == "A Burglar" or person == "Totally Not a Burglar":
            A = random.randint(1, 100)
            await ctx.send(f"A Burglar stole {A} coins from you!")
            await update_bank(ctx.author, -A)
        
    elif person == "Jeff Bezos":
            A = random.randint(1000, 10000)
            await ctx.send(f"Jeff Bezos stopped by and gave you {A} stonks")
            await update_bank(ctx.author, A)

    elif person == "Your Mom":
            await ctx.send(f"{person} found you begging for money. After 10 lectures you got nothing.")
    elif chance==2:
            await ctx.send(f"You got some money from begging but {person} stole all of it. Hes already so rich tho...")

    else:
            await update_bank(ctx.author, A)
            await ctx.send(f"{person} gave you {A} coins!")






    

    #with open("mainbank.json",'w') as f:
     #   json.dump(users,f)


# @bot.command(aliases =['beg.'])
# @commands.cooldown(1, 25, commands.BucketType.user)
# async def beg(ctx):

#     await open_account(ctx.author)
#     user = ctx.author

#     users = await get_bank_data()
#     person = ['Your grumpy old neighbor', 'Jerk Mehoff', 'Jeff Bezos', 'Bobby', 'Garret Bobby Ferguson', "Fay Gott", "Ree Todd", "Totally Not a Burglar", "Bob", "Bill","Bill gates","Your Mom","Elon Musk","Your dad","Totally Not a Burglar"]
#    # PB = ['Your grumpy old neighbor', 'Totally not a Burglar','That person who really hates you','Totally not a burglar',]
#    # PG=['Test']
#     namt = random.randrange(2001)
#     person = random.choice(people)
#     chance = random.randint(0, 10)
    
#     if person == "Your dad":
#             namt = random.randint(100, 1000)
#             await ctx.send(f"Your dad gave you {namt} coins")
#             await update_bank(user, namt)
        
#     elif person == "Totally Not a Burglar":
#             namt = random.randint(1, 100)
#             await ctx.send(f"Totally Not a Burglar stole {namt} coins from you!")
#             await update_bank(user, -namt)
        
#     elif person == "Jeff Bezos":
#             namt = random.randint(1000, 10000)
#             await ctx.send(f"Jeff Bezos stopped by and gave you {namt} stonks")
#             await update_bank(user, namt)

#     elif person == "Your Mom":
#             await ctx.send(f"{person} found you begging for money. After 10 lectures you got nothing.")
#     elif chance==2:
#             await ctx.send(f"You got some money from begging but {person} stole all of it. Hes already so rich tho...")

#     else:
#             await update_bank(user, namt)
#             await ctx.send(f"{person} gave you {namt} coins!")
    

   

#     with open("mainbank.json",'w') as f:
#         json.dump(users,f)


@bot.command(aliases=['wd','with'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
   

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} coins')


@bot.command(aliases=['dp','dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} coins')


@bot.command(aliases=['sm'])
async def send(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    await update_bank(ctx.author,-1*amount,'wallet')
    await update_bank(member,amount,'wallet')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} coins')

@bot.command(aliases=['rb','Rob','steal'])
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)

    if bal[0]<1000:
      await ctx.send('It is useless to rob him :(')
    elif member.id == 599266233350881291:
        await ctx.send('Imagine wanting to rob the owner of the server. Shame on you.<a:_2:844371369575710740>')

    elif member.id ==833122385603461121:
        await ctx.send("You are a sin to the world for robbing the very bot that is giving you money. <:_1:844623543966629937>")
    elif member == ctx.author:
        await ctx.send("Why do you want to steal from yourself??")
    elif bal[1] < 10001:
        await ctx.send("dude stealing money takes prep and money come back later when you have some stonks")
        return

    else: 
      moneycoin = [1,2,3,4,5,6,7,8,9,19]
      print("f")
      result = random.choice(tuple(moneycoin))
      #result = random.randint(1, 2, 3,4,5,6,7,8,9,10)
      if result > 5:
                win = random.randint(10, bal[0])
                print(bal[0])
                print("YO")
                await update_bank(ctx.author, win)
                await update_bank(member,-win)
                await ctx.send(f"You just robbed {member} of {win} coins")
      else:
                print("F works")
                await update_bank(ctx.author, -100)
                await update_bank(member, 100)
                await ctx.send("The police found you and you got fined $100")
                #0.1*earning
    # print(member,earning)
    #   await update_bank(ctx.author,earning)
    #   await update_bank(member,-1*earning)
    #   await ctx.send(f'{ctx.author.mention} You robbed {member} and got {earning} coins')


# @bot.command()
# @commands.cooldown(1, 25, commands.BucketType.user)
# async def slots(ctx,amount = None):
#     await open_account(ctx.author)
#     if amount == None:
#         await ctx.send("Please enter the amount")
#         return

#     bal = await update_bank(ctx.author)

#     amount = int(amount)
#     if amount > 5000:
#       await ctx.send("Hold up thats a lot of money, no way are we letting you inflate the economy")
#       return
#     if amount > bal[0]:
#         await ctx.send('You do not have sufficient balance')
#         return
#     if amount < 0:
#         await ctx.send('Amount must be positive!')
#         return
#     final = []
#     for i in range(4):
#         a = random.choice(['🐉','🍎','🦠','🍇'])

#         final.append(a)

#     await ctx.send(str(final))


#     if final[0] == final[1] or final[1] == final[2] or final[0]== final[2] or final[0] == final[3] or final[1] == final[3] or final[2] == final[3]:
#       if amount > 2001:
#         await update_bank(ctx.author,1.5*amount)
#         await ctx.send(f'You won :) {ctx.author.mention}')
#         await ctx.send(f'You won! 1.5x your amount')
#       if amount < 2000:
#          await update_bank(ctx.author,2*amount)
#          await ctx.send(f'You won :) {ctx.author.mention}')
#          await ctx.send(f'You won! 2x your amount')
#       if amount == 2000:
#         await update_bank(ctx.author,1.5*amount)
#         await ctx.send(f'You won :) {ctx.author.mention}')
#         await ctx.send(f'You won! 1.5x your amount')
#     #if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
#     #   await update_bank(ctx.author,1.5*amount)
#      #  await ctx.send(f'You won 1.5 your amount {ctx.author.mention}')
#     else:
#         await update_bank(ctx.author,-1*amount)
#         await ctx.send(f'You lose :( {ctx.author.mention}')
#         print(bal)

@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def bet(ctx, amount = None):
    await open_account(ctx.author)
    amount = int(amount)
    if amount == None:
        await ctx.send("Enter some money smh")
        return
    if amount > 20000:
        await ctx.send("Hold up thats a lot of money, no way are we letting you inflate the economy")
        return
    bal = await update_bank(ctx.author)
    if amount > bal[0]:
        ctx.send("Dont bet more then what you have")
        return

    else:
        ghot=random.randrange(5)
        if ghot == 2 or ghot == 4:
          
            embed = discord.Embed(title=f"{ctx.author.name}'s **winning** bet",colour=discord.Colour.gold())
            embed.add_field(name="Lucky Number:", value=f"<:_69:848699585370652683>", inline=False)
            # embed.add_field(name="", value="Y-You actually made your mom proud", inline=False)
            embed.add_field(name="Amount Won:", value=f"{amount*2} coins!", inline=False)
            await ctx.send(embed=embed)
            await update_bank(ctx.author,amount*2)

        else:
            emojilist=["<:_9:848707905950842880>","<:_7:848707453318463489>","<:_8:848708122691371030>"]
            emojilist = random.choice(emojilist)
            embed = discord.Embed(title=f"{ctx.author.name}'s **losing** bet",colour=discord.Colour.gold())
            embed.add_field(name="Unlucky Number:", value=f"{emojilist}", inline=False)
            # embed.add_field(name="", value="Y-You actually made your mom proud", inline=False)
            embed.add_field(name="Amount Lost:", value=f"{amount} coins!", inline=False)
            await ctx.send(embed=embed)
            await update_bank(ctx.author,-amount)


@bot.command(aliases=[])
@commands.cooldown(1, 20, commands.BucketType.user)
async def slots(ctx, amount=None):
        # TEMP: 4% chance of getting the mega jackpot!
        await open_account(ctx.author)
        #walamt, bankamt = await self.get_amt(ctx.author)
        #totalamt = walamt[0]+bankamt[0]
        amount = int(amount)
        if amount == None:
            await ctx.send("Please enter the amount")
            return

        bal = await update_bank(ctx.author)
        if amount > 5000:
            await ctx.send("Hold up thats a lot of money, no way are we letting you inflate the economy")
            return
        
        if amount > bal[0]:
            await ctx.send('You do not have sufficient balance')
            return
       # if amount == 'all':
        #    amount = bal[0]
         #   return

        else:
            final = []
            for i in range(3):
                a = random.choice(["👾","🪙", "🎩","🦌","🐈‍⬛"])
                final.append(a)
#the 2nd square is the jackpot emoji
            if final[0] == final[1] == final[2] == "🪙":
                embed = discord.Embed(
                    title=f"{ctx.author.name}'s Slot Game",
                    colour=discord.Colour.gold()
                )
                embed.add_field(name="Result:", value=f"{final[0]} {final[1]} {final[2]}", inline=False)
                embed.add_field(name="Jackpot!", value="Y-You actually made your mom proud", inline=False)
                embed.add_field(name="Amount Won:", value=f"{amount*7} coins!", inline=False)
                await ctx.send(embed=embed)
                await update_bank(ctx.author, amount*7)

            elif final[0] == final[1] == final[2]:
                embed = discord.Embed(
                    title=f"{ctx.author.name}'s Slot Game",
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Result:", value=f"{final[0]} {final[1]} {final[2]}", inline=False)
                embed.add_field(name="Three in a row!", value="You got three of the same emoji!", inline=False)
                embed.add_field(name="Amount Won:", value=f"{amount*5} coins!", inline=False)
                await ctx.send(embed=embed)
                await update_bank(ctx.author, amount*5)

            elif final[0] == final[1] or final[1] == final[2]:
                embed = discord.Embed(
                    title=f"{ctx.author.name}'s Slot Game",
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Result:", value=f"{final[0]} {final[1]} {final[2]}", inline=False)
                embed.add_field(name="Amount Won:", value=f"{amount*2} coins... thats all you could get?", inline=False)
                await ctx.send(embed=embed)
                await update_bank(ctx.author, amount*2)

            else:
                embed = discord.Embed(
                    title=f"{ctx.author.name}'s Slot Game",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="Result:", value=f"{final[0]}{final[1]}{final[2]}", inline=False)
                embed.add_field(name="You lost...", value="You lost?, No wonder your mom disowned you", inline=False)
                embed.add_field(name="Amount Lost:", value=f"{amount} coins", inline=False)
                await ctx.send(embed=embed)
                #merge thing 1
                await update_bank(ctx.author,-1*amount)





   


@bot.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)

    await ctx.send(embed = em)

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break


    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@bot.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")



    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            return [False,3]
    except:
        return [False,3]

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]


@bot.command(aliases = ["lb"])
@commands.guild_only()
async def leaderboard(ctx,x = 10):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)

    em = discord.Embed(title = f"Top {x} Richest People in this **server**" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True






# @bot.command()
# async def test(ctx,):
#     if item=='laptop':
#         print("f")


@bot.command(aliases = ["lbg"])
async def leaderboardglobal(ctx,x = 10):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)

    em = discord.Embed(title = f"Top {x} Richest People in the **world**" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True









async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0, mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal








@bot.command(pass_context=True)
async def afg(ctx,role: discord.Role, user: discord.Member):
  await user.add_roles(role)
  await ctx.send("f")













@bot.command()
async def helpt(ctx):
    with open("data.json") as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if ctx.author.guild_permissions.administrator or valid_user:

        em = discord.Embed(title="Stonk Tickets Help", description="", color=0x00a8ff)
        em.add_field(name="`+new <message>`", value="This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket.")
        em.add_field(name="`+close`", value="Use this to close a ticket. This command only works in ticket channels.")
        em.add_field(name="`+addaccess <role_id>`", value="This can be used to give a specific role access to all tickets. This command can only be run if you have an admin-level role for this bot.")
        em.add_field(name="`+delaccess <role_id>`", value="This can be used to remove a specific role's access to all tickets. This command can only be run if you have an admin-level role for this bot.")
        em.add_field(name="`+addpingedrole <role_id>`", value="This command adds a role to the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.")
        em.add_field(name="`+delpingedrole <role_id>`", value="This command removes a role from the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.")
        em.add_field(name="`+addadminrole <role_id>`", value="This command gives all users with a specific role access to the admin-level commands for the bot, such as `.addpingedrole` and `.addaccess`. This command can only be run by users who have administrator permissions for the entire server.")
        em.add_field(name="`+deladminrole <role_id>`", value="This command removes access for all users with the specified role to the admin-level commands for the bot, such as `.addpingedrole` and `.addaccess`. This command can only be run by users who have administrator permissions for the entire server.")
        em.set_footer(text="Stonk Bot:bot made by DragonRoyal#7111")


        await ctx.send(embed=em)
        reaction = "📜"
        await ctx.message.add_reaction(emoji=reaction)

    else:

        em = discord.Embed(title = "Distrupt Tickets Help", description ="", color = 0x00a8ff)
        em.add_field(name="`+new <message>`", value="This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket.")
        em.add_field(name="`.close`", value="Use this to close a ticket. This command only works in ticket channels.")
        em.set_footer(text="Doge Coin is cool")

        await ctx.send(embed=em)

@bot.command( aliases=['new','support'])
async def ticket(ctx, *, args = None):

    await bot.wait_until_ready()

    if args == None:
        message_content = "Please wait, we will be with you shortly!"

    else:
        message_content = "".join(args)

    with open("data.json") as f:
        data = json.load(f)

    ticket_number = int(data["ticket-counter"])
    ticket_number += 1

    ticket_channel = await ctx.guild.create_text_channel("ticket-{}".format(ticket_number))
    await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)

    for role_id in data["valid-roles"]:
        role = ctx.guild.get_role(role_id)

        await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    em = discord.Embed(title="New ticket from {}#{}".format(ctx.author.name, ctx.author.discriminator), description= "{}".format(message_content), color=0x00a8ff)

    await ticket_channel.send(embed=em)

    pinged_msg_content = ""
    non_mentionable_roles = []

    if data["pinged-roles"] != []:

        for role_id in data["pinged-roles"]:
            role = ctx.guild.get_role(role_id)

            pinged_msg_content += role.mention
            pinged_msg_content += " "

            if role.mentionable:
                pass
            else:
                await role.edit(mentionable=True)
                non_mentionable_roles.append(role)

        await ticket_channel.send(pinged_msg_content)

        for role in non_mentionable_roles:
            await role.edit(mentionable=False)

    data["ticket-channel-ids"].append(ticket_channel.id)

    data["ticket-counter"] = int(ticket_number)
    with open("data.json", 'w') as f:
        json.dump(data, f)

    created_em = discord.Embed(title="Auroris Tickets", description="Your ticket has been created at {},".format(ticket_channel.mention), color=0x00a8ff)

    await ctx.send(embed=created_em)

@bot.command()
async def close(ctx):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "close"

        try:

            em = discord.Embed(title="Stonk Tickets", description="Are you sure you want to close this ticket? Reply with `close` if you are sure.", color=0x00a8ff)

            await ctx.send(embed=em)
            await bot.wait_for('message', check=check, timeout=60)
            await ctx.channel.delete()

            index = data["ticket-channel-ids"].index(channel_id)
            del data["ticket-channel-ids"][index]

            with open('data.json', 'w') as f:
                json.dump(data, f)

        except asyncio.TimeoutError:
            em = discord.Embed(title="Stonk Tickets", description="You have run out of time to close this ticket. Please run the command again.", color=0x00a8ff)
            await ctx.send(embed=em)



@bot.command()
async def addaccess(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:
        role_id = int(role_id)

        if role_id not in data["valid-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["valid-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Auroris Tickets", description="You have successfully added `{}` to the list of roles with access to tickets.".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
                await ctx.send(embed=em)

        else:
            em = discord.Embed(title="Auroris Tickets", description="That role already has access to tickets!", color=0x00a8ff)
            await ctx.send(embed=em)

    else:
        em = discord.Embed(title="Auroris Tickets", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
        await ctx.send(embed=em)

@bot.command()
async def delaccess(ctx, role_id=None):
    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            valid_roles = data["valid-roles"]

            if role_id in valid_roles:
                index = valid_roles.index(role_id)

                del valid_roles[index]

                data["valid-roles"] = valid_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Auroris Tickets", description="You have successfully removed `{}` from the list of roles with access to tickets.".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            else:

                em = discord.Embed(title="Auroris Tickets", description="That role already doesn't have access to tickets!", color=0x00a8ff)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
            await ctx.send(embed=em)

    else:
        em = discord.Embed(title="Auroris Tickets", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
        await ctx.send(embed=em)

@bot.command()
async def addpingedrole(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:

        role_id = int(role_id)

        if role_id not in data["pinged-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["pinged-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Stonk Tickets", description="You have successfully added `{}` to the list of roles that get pinged when new tickets are created!".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(title="Stonk Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
                await ctx.send(embed=em)

        else:
            em = discord.Embed(title="Stonk Tickets", description="That role already receives pings when tickets are created.", color=0x00a8ff)
            await ctx.send(embed=em)

    else:
        em = discord.Embed(title="Stonk Tickets", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
        await ctx.send(embed=em)



@bot.command()
async def testcool(ctx):
    print(item)


@bot.command()
async def delpingedrole(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            pinged_roles = data["pinged-roles"]

            if role_id in pinged_roles:
                index = pinged_roles.index(role_id)

                del pinged_roles[index]

                data["pinged-roles"] = pinged_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Auroris Tickets", description="You have successfully removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x00a8ff)
                await ctx.send(embed=em)

            else:
                em = discord.Embed(title="Auroris Tickets", description="That role already isn't getting pinged when new tickets are created!", color=0x00a8ff)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Auroris Tickets", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
        await ctx.send(embed=em)

    











@bot.command()
@has_permissions(administrator=True)
async def addadminrole(ctx, role_id=None):

    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        data["verified-roles"].append(role_id)

        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        em = discord.Embed(title="Auroris Tickets", description="You have successfully added `{}` to the list of roles that can run admin-level commands!".format(role.name), color=0x00a8ff)
        await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
        await ctx.send(embed=em)

@bot.command()
@has_permissions(administrator=True)
async def deladminrole(ctx, role_id=None):
    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        admin_roles = data["verified-roles"]

        if role_id in admin_roles:
            index = admin_roles.index(role_id)

            del admin_roles[index]

            data["verified-roles"] = admin_roles

            with open('data.json', 'w') as f:
                json.dump(data, f)
            
            em = discord.Embed(title="Auroris Tickets", description="You have successfully removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x00a8ff)

            await ctx.send(embed=em)
        
        else:
            em = discord.Embed(title="Auroris Tickets", description="That role isn't getting pinged when new tickets are created!", color=0x00a8ff)
            await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Auroris Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
        await ctx.send(embed=em)









@bot.event
async def on_message(message):
    if message.content.startswith('you are'):
        await message.channel.send('NO U')





@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('I see you are to good to just use +help for the commands. (Or your just mocking me or something) So for that reason i will make you cease to exist <a:_3:845491804429484064>')




#on bot join msg
@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}! My prefix is + Do +help to learn more about my commands or +helpdm for the help commands to be dm'.format(guild.name))



#@bot.command()
#async def meme(ctx):
 #   async with aiohttp.BotSession() as cs:
  #    async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=top') or cs.get('https://www.reddit.com/r/memes/new.json?sort=top') or cs.get('https://www.reddit.com/r/programmingmemes/new.json?sort=top') or cs.get('https://www.reddit.com/r/cleanmemes/new.json?sort=top') as r:
   #     res = await r.json()

    #num = random.randint(0, len(res['data']['children'])-1)

    #m = res['data']['children'] [num]['data']['url']
    #e = Embed(description = f"**[{res['data']['children'] [num]['data']['title']}]({m})**", color=amberz)
   # e.set_footer(text= res['data']['children'] [num]['data']['author'], icon_url=ctx.guild.icon_url)
    #e.set_image(url = res['data']['children'] [num]['data']['url'])
   # await ctx.send(embed=e)









#--------------REDDIT MEME GENERATION!----------------
# wont work



#reddit = asyncpraw.Reddit(client_id ='OK4gxau76j-sPw',
#client_secret ='QqSS9K4UN9KFItLXFxJWRxBZ1GRsMQ', user_agent = 'praw', username ='Dragonroyal', password = 'savecup11',)


#subreddit = reddit.subreddit('memes')
#top = subreddit.top(Limit = 5)
#for submisson  in top:
#  print(submission.title)

#print("F")
#@bot.command()
#async def memeswork(ctx):
 # print("Ff")
  #subreddit = reddit.subreddit('memes')
  #top = subreddit.top(Limit = 50)
  #all_subs =[]
  #for submission in top:
   # all_subs.append(submission)
    #print("FFf")

  #random_sub = random.choice(all_subs)
  #print("fffds")
  #name = random_sub.title
  #url = random_sub.url
  #em = discord.Embed(title=name)
  #em.set_image(url=url)
  #print("ejksjs")
  #await ctx.send(embed = em)


#@bot.command()
#async def memef(ctx):
 #   memes_submissions = reddit.subreddit('memes').hot()
  #  post_to_pick = random.randint(1, 10)
  #  for i in range(0, post_to_pick):
  #      submission = next(x for x in memes_submissions if not x.stickied)

   # await bot.say(submission.url)



#who is command
@bot.command(aliases=["user"])
async def whois(ctx, member:discord.Member=None):
    
    if member is None:
        member = ctx.author
    user = member
    roles = [role for role in member.roles]
    allroles = [role.mention for role in roles[1:]]
    embed = discord.Embed(title = member.name , describtion = member.mention ,color = discord.Color(0x7289DA))
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name = "ID", value = member.id , inline = True)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name=f"Roles (amount: {len(roles)}):", value="\n".join(allroles))
    embed.add_field(name="Highest Role:", value=f"{member.top_role.mention if member.top_role else 'N/A'}")
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text =   f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@bot.command()
async def botservers(ctx):
    await ctx.send("I'm in " + str(len(bot.guilds)) + " servers!")





@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def kingruless(ctx):
  embed = discord.Embed(color = discord.Color.blue())
  embed.set_author(name='Rules📓')
  embed.add_field(name='1.', value=' Please dont talk about religion or politics. People can be really sensitive about this stuff, so dont do it here, thanks!')
  embed.add_field(name='2.', value='No NSFW, sexist, racist, homophobic, transphobic, misogynistic or inappropriate content or anything remotely similar. Respect people, its the 21st century. This includes any slurs.')
  embed.add_field(name='3.', value='Causing drama is an instant punishment. Its simple, please dont.',)
  embed.add_field(name='6', value='Attempting to override a punishment or using alternate accounts will lead to all your accounts being banned. This includes leaving to bypass a mute.',)
  embed.add_field(name='7', value='Please keep discussion in English only. This includes voice chats.',)
  embed.add_field(name='8', value='Dont spam or use copy pastes here. Theyre not nice and make chat hard to manage.')
  embed.add_field(name='9', value='Absolutely no advertising will be allowed without prior permission from a moderator. This includes YouTube videos, Twitch channels & Discord servers. Please dont link Zoom, Google Meet, or similar services too, as well as advertising art commissions.',)

  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1149577551708184576/6KG41LLu_400x400.jpg")
  embed.set_footer(text="Imagine not voting for this bot in top.gg")
  await ctx.send(embed=embed)

# async def on_message(message):
#   if bot.user == message.author:
#     return
#   if message.channel.id == 842336034431827988:
#     msg = message.content
#     key = os.getenv('key')
#     header = {"x-api-key": key}
#     dev_name = "ChaoticNebula"
#     type = "stable"
#     params = {'type':type , 'message':msg, 'dev_name': "ChaoticNebula", 'bot_name': "Ai Chat"}
#     async with aiohttp.ClientSession(headers=header) as session:
#       async with session.get(f'https://api.pgamerx.com/v3/ai/response', params=params) as resp:
#         text = await resp.json()
#         await message.channel.send(text[0]["message"])
#   else:
#     pass


#test
#if this works then WOW
@commands.group(invoke_without_command=True)
async def use(self, ctx):
        await ctx.send("You need to specify an item to use.")
    
@use.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def watch(self, ctx):
        await self.open_account(ctx.author)
        amount = await self.item_func(ctx.author, "watch")
        if amount[0] < 1:
            await ctx.send("You can't use a watch that you don't have!")
        else:
            chance = random.randint(0, 3)
            if chance == 1:
                await ctx.send("You tried to give someone the time, but they didn't give a shit.")
            elif chance == 2:
                await ctx.send("Someone got angry at you and smashed your watch.")
                await self.item_func(ctx.author, "watch", -1)
            else:
                tip = random.randint(0, 50)
                await ctx.send(f"You gave someone the time and they gave you a {tip} moner tip!")
                await self.update_bank(ctx.author, tip)

@use.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def laptop(self, ctx):
        await open_account(ctx.author)
        amount = await item_func(ctx.author, "laptop")
        if amount[0] < 1:
            await ctx.send("You can't use a computer that you don't have!")
        else:
            chance = random.randint(0, 3)
            games = ["Rocket League", "Minecraft", "Minceraft", "Call of Duty: Modern Warfare",
            "Call of Duty: Cold War", "Super Mario Bros.", "Super Mario Galaxy", "Mario Kart", "Halo 3", "Doom", 
            "CS:GO", "Overwatch", "Rainbow Six: Siege", "Uno With Friends", "Dark Souls", "Banjo Kazooie", "The Witcher",
            "Snake"]
            if chance == 2:
                await ctx.send(f"You lost {random.choice(games)} and smashed your computer.")
                await item_func(ctx.author, "computer", -1)
            elif chance == 1:
                await ctx.send(f"You lost {random.choice(games)} but decided not to lose your temper.")
            else:
                reward = random.randint(1, 2000)
                await ctx.send(f"You won {random.choice(games)} and got rewarded with {reward} moners!")
                await update_bank(ctx.author, reward)










@bot.command()
async def hi2(ctx):
    await ctx.send("it worked")



@bot.command() # Normal message wait_for
async def testm(ctx):
    await ctx.send("Do you want me to say hi? `(y/n)`")
    msg = await bot.wait_for('message', timeout=15.0)
    if msg.content == 'y':
        await ctx.send("hi")
    else:
        await ctx.send("ok i wont")
#                 if ctx.channel.is_nsfw() == True:
#                     pass
#                 else:
#                     await ctx.send("Imagine wanting to look at nsfw things IN A PUBLIC CHAT")
#                     return
#             if ransub.is_self:
#                 embed = discord.Embed(title=f"{ransub.author}'s Post", colour=ctx.author.colour)
#                 embed.add_field(name=ransub.title, value=ransub.selftext)
#                 embed.set_footer(text=f"❤ {ransub.ups} | 💬 {ransub.num_comments}")
#             else:
#                 embed = discord.Embed(title=ransub.title, colour=ctx.author.colour, url=ransub.url)
#                 embed.set_footer(text=f"Posted by {ransub.author} on Reddit. | ❤ {ransub.ups} | 💬 {ransub.num_comments}")
#                 embed.set_image(url=ransub.url)
#             await message.delete()
#             await ctx.send(embed=embed)
#         except:
#             await ctx.send("Something went wrong. This may be the fact that the subreddit does not exist or is locked.")




class snipe(commands.Cog, description="snipe commands"):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.snipe_cache = {}
        self.esnipe_cache = {}

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            return
        self.esnipe_cache[before.channel.id] = {}
        self.esnipe_cache[before.channel.id]["before"] = [before.content, before.author]
        self.esnipe_cache[before.channel.id]["after"] = [after.content, after.author]
        await asyncio.sleep(60)
        self.esnipe_cache.pop(before.channel.id, None)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        self.snipe_cache[message.channel.id] = [message.content, message.author]
        await asyncio.sleep(60)
        self.snipe_cache.pop(message.channel.id, None)

    @commands.command(name="snipe", brief="Retrieves a recent deleted message")
    async def snipe(self, ctx):
        """
        Acts like a message log, but for channel specific and command only.\n
        Only returns the most recent message.
        A bot's deleted message is ignored.
        """
        channel = ctx.channel
        author = ctx.author
        try:
            em = Embed(
                name=f"Last deleted message in #{channel.name}",
                description=self.snipe_cache[channel.id][0],
                timestamp=datetime.datetime.utcnow(),
                colour=discord.Color.random(),
            )
            em.set_author(
                name=f"{self.snipe_cache[channel.id][1]}",
                icon_url=f"{self.snipe_cache[channel.id][1].avatar_url}",
            )
            em.set_footer(text=f"Sniped by: {author}")
            return await ctx.send(embed=em)
        except KeyError:
            return await ctx.send("There's nothing to snipe!")

    @commands.command(name="editsnipe", brief="Retrieves a recently edited message")
    async def editsnipe(self, ctx):
        """
        Same as `snipe`, but for edited messages.
        A bot's edited message is ignored.
        """
        channel = ctx.channel
        author = ctx.author
        try:
            em = Embed(
                name=f"Last edited message in #{channel.name}",
                description="**Before:**\n"
                f"+ {self.esnipe_cache[channel.id]['before'][0]}\n"
                f"\n**After:**\n- {self.esnipe_cache[channel.id]['after'][0]}",
                timestamp=datetime.datetime.utcnow(),
                colour=discord.Color.random(),
            )
            em.set_author(
                name=f"{self.esnipe_cache[channel.id]['before'][1]}",
                icon_url=f"{self.esnipe_cache[channel.id]['before'][1].avatar_url}",
            )

            em.set_footer(text=f"Sniped by: {author}")
            return await ctx.send(embed=em)
        except KeyError:
            return await ctx.send("There's nothing to snipe!")



@bot.command()
async def hi(ctx):
    await ctx.send("it worked")












class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.song_queue = {}

        self.setup()

    def setup(self):
        for guild in self.bot.guilds:
            self.song_queue[guild.id] = []

    async def check_queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) > 0:
            ctx.voice_client.stop()
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)

    async def search_song(self, amount, song, get_url=False):
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
        if len(info["entries"]) == 0: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.source.volume = 0.5

    @commands.command()
    async def join(self, ctx):
        connected = ctx.author.voice
        if not connected:
            await ctx.send("You need to be connected in a voice channel to use this command!")
            return
        global vc
        vc = await connected.channel.connect()
#        if ctx.author.voice is None:
#            return await ctx.send("You are not connected to a voice channel, please connect to the channel you want the bot to join.")
#
#        if ctx.voice_client is not None:
#            await ctx.voice_client.disconnect()
#        else:
#            await ctx.author.voice.channel.connect()





class Fun(commands.Cog, description="Fun commands"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["memes"], brief="Shows a meme from reddit")
    async def meme(self, ctx):

        async with self.bot.session() as cs:
            async with cs.get("https://www.reddit.com/r/memes/random/.json") as res:
                res = await res.json()

                image = res[0]["data"]["children"][0]["data"]["url"]
                permalink = res[0]["data"]["children"][0]["data"]["permalink"]
                url = f"https://reddit.com{permalink}"
                title = res[0]["data"]["children"][0]["data"]["title"]
                ups = res[0]["data"]["children"][0]["data"]["ups"]
                downs = res[0]["data"]["children"][0]["data"]["downs"]
                comments = res[0]["data"]["children"][0]["data"]["num_comments"]

                em = Embed(colour=discord.Color.blurple(), title=title, url=url)
                em.set_image(url=image)
                em.set_footer(text=f"👍 {ups} 👎 {downs} 💬 {comments}")
                await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Fun(bot))




    # @commands.command()
    # async def play(self, ctx, *, song=None):
    #     if song is None:
    #         return await ctx.send("You must include a song to play.")

    #     if ctx.voice_client is None:
    #         return await ctx.send("I must be in a voice channel to play a song.")

    #     # handle song where song isn't url
    #     if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
    #         await ctx.send("Searching for song, this may take a few seconds.")

    #         result = await self.search_song(1, song, get_url=True)

    #         if result is None:
    #             return await ctx.send("Sorry, I could not find the given song, try using my search command.")

    #         song = result[0]

    #     if ctx.voice_client.source is not None:
    #         queue_len = len(self.song_queue[ctx.guild.id])

    #         if queue_len < 10:
    #             self.song_queue[ctx.guild.id].append(song)
    #             return await ctx.send(f"I am currently playing a song, this song has been added to the queue at position: {queue_len+1}.")

    #         else:
    #             return await ctx.send("Sorry, I can only queue up to 10 songs, please wait for the current song to finish.")

    #     await self.play_song(ctx, song)
    #     await ctx.send(f"Now playing: {song}")


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def music(ctx):
  embed = discord.Embed(color = discord.Color.blue())
  embed.set_author(name='Music commands')
  embed.add_field(name='+join', value='Joins the vc', inline=False)
  embed.add_field(name='+play (song name or url)', value='The bot plays the music example of use: +play rise or +play https://www.youtube.com/watch?v=fB8TyLTD7EE',
  inline=False)
  embed.add_field(name='+leave', value='Leaves the vc', inline=False)
  embed.add_field(name='+pause', value='pauses the current song playing', inline=False)
  embed.add_field(name='+resume', value='resumes the paused song', inline=False)
  embed.add_field(name='+about', value='Read some useless stuff', inline=False)
  embed.add_field(name='+about', value='Read some useless stuff', inline=False)
  embed.add_field(name='+loop', value='loops a song you specified', inline=False)
  embed.add_field(name='+queue', value='queue a song', inline=False)
  embed.add_field(name='+np', value='says the song currently playing', inline=False)
  embed.add_field(name='+leave', value='Leaves the vc', inline=False)
  
  
  

  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1149577551708184576/6KG41LLu_400x400.jpg")
  embed.set_footer(text="not much in this command right?")
  await ctx.send(embed=embed)




music = DiscordUtils.Music()

@bot.command()
async def join(ctx):
    await ctx.author.voice.channel.connect() #Joins author's voice channel
    embed=discord.Embed(title="Joined Voice Channel!", color=discord.Color.random())
    embed.set_footer(text="Consider voting for the bot")
    await ctx.send(embed=embed)

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    embed=discord.Embed(title="Left Voice Channel!", color=discord.Color.random())
    embed.set_footer(text="How are our music commands?")
    await ctx.send(embed=embed)


@bot.command()
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        #print("f")
        #em=discord.Embed(title=f'The bots not even in a voice channel',color=discord.Color.random())
       # em.set_footer(text='At least make the bot join vc <:smh:849114935408853022>')
        #await ctx.send(embed=em)
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if player is None:
        await ctx.send("I am not connected to a voice channel.")
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        em=discord.Embed(title=f"Playing {song.name}", color=discord.Color.random())
        em.set_footer(text='Spread the word about stonk bot!')
        await ctx.send(embed=em)
        print(url)
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"Queued {song.name}")

@bot.command()
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song1 = await player.pause()
    em=discord.Embed(title=f"Paused {song1.name}", color=discord.Color.random())
    em.set_footer(text='Invite stonk bot to other servers also')
    await ctx.send(embed=em)

@bot.command()
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song2 = await player.resume()
    em=discord.Embed(title=f'Resumed {song2.name}',color=discord.Color.random())
    em.set_footer(text='Vote for the bot')
    await ctx.send(embed=em)

@bot.command()
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Stopped")

@bot.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")

@bot.command()
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")

@bot.command()
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(song.name)

@bot.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")

@bot.command()
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    em=discord.Embed(title=f"Changed volume for {song.name} to {volume*100}%", color=discord.Color.random())
    em.set_footer(text='Invite stonk bot to other servers also')
    await ctx.send(embed=em)


@bot.command()
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    em=discord.Embed(title=f"Removed {song.name} from the queue", color=discord.Color.random())
    em.set_footer(text='Do you even read these?')
    await ctx.send(embed=em)







#keep_alive()
bot.run(TOKEN)
#bot.run(os.environ[TOKEN])




    #@commands.command(aliases=["slots", "bet"])
    #@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    #async def slot(self, ctx):
      #  """ Roll the slot machine """
        #emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        #a = random.choice(emojis)
        #b = random.choice(emojis)
        #c = random.choice(emojis)

        #slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        #if (a == b == c):
         #   await ctx.send(f"{slotmachine} All matching, you won! 🎉")
       # elif (a == b) or (a == c) or (b == c):
        #    await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        #else:
         #   await ctx.send(f"{slotmachine} No match, you lost 😢")
