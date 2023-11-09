import discord
from discord.ext import commands
import random as r
import os
from subprocess import run
from PIL import Image
from img_editor import edit
from discord.ext import commands
from MYsql import *
import asyncio
from Scraper1 import search
import Converter
import Execution
from encrypter import func
from redvid import Downloader
from RedDownloader import RedDownloader

description = '''Pretty epic bot.
There are a number of utility commands being showcased here. \n
Please use ?help <command name> to know more about it.'''

intents = discord.Intents.all()
intents.members = True
intents.message_content = True


help_command = commands.DefaultHelpCommand(no_category = "Commands"
                    ,default_argument_description = " ->  <INPUT>",sorted=True,dm_help=True)
bot = commands.Bot(command_prefix='?', description=description
                   , intents=intents,help_command=help_command)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="?help"))
    await bot.tree.sync()
    os.chdir(path = r"C:\Users\callm\Desktop\Python Files")

@bot.hybrid_command(name="slash")
async def slash(ctx):                                    
   await ctx.send("You executed the slash command!")
   
@bot.command(name="KillSwitch")
async def stop(ctx):
    if ctx.author.id == 710758283408834612:
        await ctx.channel.send('Closing')
        await bot.close()


@bot.command(description="Gonk's Introduction")
async def intro(ctx):
    await ctx.send(f"My name is <@{bot.user.id}>")    # type: ignore
    await ctx.send(f"Hi <@{ctx.author.id}>")
    
@bot.command(description = "Embeds anything")
async def embed(ctx,Title,description,thumbnail = None):
    embed=discord.Embed(title=Title, description=description, color=0x00ff00)
    embed.set_image(url= thumbnail)
    await ctx.send(embed = embed)
    await ctx.message.delete()
    
@bot.command(description="Great command")
async def EpicCommand(ctx):
    await ctx.reply("https://media.discordapp.net/attachments/1067614171656622191/1147256605948252292/attachment.png")


@bot.command(name = "yt", description = "Downloads YT videos and sends it") 
@commands.cooldown(1,15,commands.BucketType.user)
async def youtube(ctx,link):
    await ctx.channel.send("Working on it...")
    name = str(r.randint(0,999)) + ".mp4" 
    try:
        run(f"youtube-dl --output {name} --max-filesize 25m -f mp4[width<1080] {link}")
        await ctx.channel.send(file=discord.File(fp = f"{name}"))
        os.remove(path=name)
    except:
        await ctx.reply("Error \n *maybe because of a too large file/video?*")
        
@youtube.error
async def youtube_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)


@bot.command(name = 'yts',description = "Download Mp3 songs from YT")
@commands.cooldown(1,15,commands.BucketType.user)
async def song(ctx,link):
    await ctx.channel.send("Working on it...")
    name = str(r.randint(0,999)) + ".m4a"
    try:
        run(f'youtube-dl -x --output {name} --max-filesize 25m -f m4a {link}')
        await ctx.channel.send(file=discord.File(fp = rf"C:\Users\callm\Desktop\Python Files\{name}"))
        os.remove(path=name)
    except:
        await ctx.reply("Error \n *-maybe because of a too large video?*")

@song.error
async def song_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)
                       
@bot.command(description = "Encodes any Big sentence \n ONLY letters and space")
async def encode(ctx,*,Sentence):
    try:
        string = func(Sentence,True)
        await ctx.reply(string)
    except:
        embed = discord.Embed(title="Error",description="Please check the written sentence for wrong characters \n *might wanna check ?help encode*",color=0xFFF000) 
        await ctx.reply(embed=embed)   
        
@bot.command(description = "Paste any encoded sentence from Gonk to decode \n For Errors, please check encoded message.")
async def decode(ctx,*,Sentence):
    try:
        string = func(Sentence,False)
        await ctx.reply(string)
    except:
        embed = discord.Embed(title="Error",description="Please check the written sentence for wrong characters \n *might wanna check ?help decode*",color=0xFFF000) 
        await ctx.reply(embed=embed) 

@bot.command(description = "Flips a coin")
async def flip(ctx):
    s = sql()
    a = ["Heads","Tails"]
    result = r.choice(a)
    L = {"Tails":"https://cdn.discordapp.com/attachments/822312548892147735/1071844398666612777/image.png"
         ,"Heads":"https://cdn.discordapp.com/attachments/879245507116019823/1074964894643912704/hvfgh.png"}
    if result in L:
        c = L[result]
        
    embed = discord.Embed(title = "Flipping Coin...",description= None, colour=0xffff00)
    embed2 = discord.Embed(title = result.upper() + "!!",colour=0xff0000)
    
    a = r.randint(0,3)
    print(a)
    if a == 1:
        g = r.randint(10,100)
        embed2.set_footer(text = f"{ctx.author.name} won ${g} coins!")
        s.add(ctx.guild.name,ctx.author.id,g)
        
    embed2.set_image(url=c)  # type: ignore
    thumbnail = "https://media.tenor.com/a2fp2WK79dEAAAAi/one-pound.gif"
    embed.set_image(url = thumbnail)
    
    msg = await ctx.send(embed=embed)
    await asyncio.sleep(3)
    await msg.edit(embed=embed2)
    
    s.Discon()
    
@bot.command(description = "Use Magik ball to answer your question")
@commands.cooldown(1,3,commands.BucketType.user)
async def magikball(ctx):
    
    start = ['Yes','No','I dont know',"I'm ignoring that",'You know the answer',
             'Wha..?','How do you even come up with this?','Go touch grass','haha no','Pardon me?','']
    mid = [' i think its better that way?...',' hehe',' think about it',
           ' think about your life',' maybe no actually'," i'm cringing af",' i cant care less',' actually ask your friend ',
           ' not my problem',' million dollar question',' you can become gay though',' definetly not lying','','','','','','']
    end = [' 👍',' 😃',' ✔️',' ❓','','','','',]
    
    x = ctx.message.content
    found = 0
    
    x = x.lower()
    x = x.split()
    for a in x:
        if a == 'fuck':
            found += 1
    g = ctx.message.content     
    if len(g) <= 15:
        await ctx.channel.send("Cringe.")
    elif found != 0:
        await ctx.channel.send('No lmao.')
    else:
        z = r.choice(start)
        z += r.choice(mid)
        z += r.choice(end)
        await ctx.channel.send(z)

@magikball.error
async def magikball_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)


@bot.command(description = "Guess the number fom 1 to 20")
@commands.cooldown(1,15,commands.BucketType.user)
async def guess(ctx):
    s = sql()
    await ctx.channel.send("First to guess from 1 to 20 WINS!")
    number = r.randint(1, 20)
    print(number)
    found = 0
    while found == 0:
        msg = await bot.wait_for('message')
        if (msg.content) == str(number):
            await ctx.channel.send(f'{msg.author.mention} guessed the number!')
            s.add(ctx.guild.name,ctx.author.id,500)
            found +=1
    
    s.Discon()
    
@guess.error
async def guess_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)

@bot.command(description = 'Pong')
async def ping(ctx):
    await ctx.channel.send(f'Ping is {bot.latency}')

@bot.command(description = "play Rock Paper Scissor with bot or someone else \n No input is for singleplayer")
@commands.cooldown(1,10,commands.BucketType.user)
async def rps(ctx, user : discord.User=None):   # type: ignore
    s = sql()
    # (ctx.message.author)
    # await ctx.author.send("hi")
    # await user.send(text) send user a message
    # await ctx.channel.send(f'{user} has won nothing!')
    # await ctx.channel.send(user.mention) pings user
   
    
    def check1(g):
        return g.author == ctx.author and g.content.isdigit() or g.content == "stop"
    def check2(g):
        return g.author == user and g.content.isdigit() or g.content == "stop"

    done = 0
    
    if user != None:
        A = s.balance(ctx.guild.name,ctx.author.id)
        B = s.balance(ctx.guild.name,user.id)
        if A <= 0:
            await ctx.channel.send(f"{ctx.author.mention} is TOO broke!")
            return
        elif B <= 0:
            await ctx.channel.send(f"{user.mention} is TOO broke!")
            return
        else:
            user1_cash = 0
            user2_cash = 0

            while done == 0:
                g = await ctx.channel.send(f"{ctx.author.mention} \n Please submit your wager money \n [enter number]")
                msg1 = await bot.wait_for('message',check=check1)
                
                if int(msg1.content) <= A:
                    user1_cash = int(msg1.content)
                    await g.delete()
                    done = 1
                elif msg1.content == "stop":
                    await ctx.channel.send("Stopping")
                    return
                else:
                    await ctx.channel.send("Not sufficient Coins")
                    await g.delete()
                    continue
                
            while done == 1:
                    h = await ctx.channel.send(f"{user.mention} \n Please submit your wager money \n [enter number]")
                    msg2 = await bot.wait_for('message',check=check2)
                    if int(msg2.content) <= B and int(msg2.content) >= int(msg1.content):  # type: ignore
                        user2_cash = int(msg2.content)
                        await h.delete()
                        done = 2
                    elif msg2.content == "stop":
                        await ctx.channel.send("stop")
                        return
                    else:
                        await ctx.channel.send("Not sufficient Coins")
                        await h.delete()
                        continue  
                
            await user.send(f'Waiting for <@{ctx.author.id}>')

    
    embed1 = discord.Embed(title = "Rock Paper Scissors!", description= "Please react to your choice",colour = 0xffff00)
    embed1.set_image(url = 'https://cdn.discordapp.com/attachments/822312548892147735/1075759285021188157/iu.png')
    
    msg = await ctx.author.send(embed = embed1)
    await msg.add_reaction("🪨")
    await msg.add_reaction("📄")
    await msg.add_reaction("✂️")
    
    def check(reaction,user):
        return reaction.emoji,user
    
    
    reaction1,user1 = await bot.wait_for('reaction_add', timeout=60.0, check=check)    # type: ignore
    
    if user.id == 710758283408834612:
        await user.send(f'{user1} took {reaction1}')
    
    if user == None:
        reaction2 = r.choice(["🪨","📄","✂️"])
        user2 = bot.user
        b = f"<@{bot.user.id}>"         # type: ignore
        c = "https://cdn.discordapp.com/avatars/1033979511873744916/7a2a32db1f88fbf81993a55cea0dcf54.png"
    else:
        msg2 = await user.send(embed = embed1)
        await msg2.add_reaction("🪨")
        await msg2.add_reaction("📄")
        await msg2.add_reaction("✂️")
        
        reaction2,user2 = await bot.wait_for('reaction_add', timeout=60.0, check=check)    # type: ignore
        b = user2.mention
        c = user2.avatar
    if user != None:
        embed2 = discord.Embed(title = f'{user2} beats {user1}',description= f"{b} wins with {reaction2}! \n They get ${user1_cash}!",colour = 0x00ff00)
        embed3 =  discord.Embed(title = f'{user1} beats {user2}',description= f"{user1.mention} wins with {reaction1}! \n They get ${user2_cash}!",colour = 0x00ff00)
    else:
        embed2 = discord.Embed(title = f'{user2} beats {user1}',description= f"{b} wins with {reaction2}!",colour = 0x00ff00)
        embed3 =  discord.Embed(title = f'{user1} beats {user2}',description= f"{user1.mention} wins with {reaction1}!",colour = 0x00ff00)
    embed4 = discord.Embed(title = "Its a Tie!",description = f'{user1.mention} and {b} both took {reaction1}',colour = 0xFF0000)
    
    if str(reaction1) == "🪨":
        if str(reaction2) == "📄":
            embed2.set_thumbnail(url= c)
            await ctx.channel.send(embed = embed2)
            s.subtract(ctx.guild.name,ctx.author.id,user1_cash)
            s.add(ctx.guild.name,user.id,user1_cash)
        elif str(reaction2) == "✂️":
            embed3.set_thumbnail(url = user1.avatar)
            await ctx.channel.send(embed = embed3)
            s.subtract(ctx.guild.name,user.id,user2_cash)
            s.add(ctx.guild.name,ctx.author.id,user2_cash)
        else:
            await ctx.channel.send(embed = embed4)
    if str(reaction1) == "📄":
        if str(reaction2) == "🪨":
            embed3.set_thumbnail(url = user1.avatar)
            await ctx.channel.send(embed = embed3)
            s.add(ctx.guild.name,ctx.author.id,user2_cash)
            s.subtract(ctx.guild.name,user.id,user2_cash)
        elif str(reaction2) == "✂️":
            embed2.set_thumbnail(url = c)
            await ctx.channel.send(embed = embed2)
            s.subtract(ctx.guild.name,ctx.author.id,user1_cash)
            s.add(ctx.guild.name,user.id,user1_cash)
        else:
            await ctx.channel.send(embed = embed4)
    if str(reaction1) == "✂️":
        if str(reaction2) == "📄":
            embed3.set_thumbnail(url = user1.avatar)
            await ctx.channel.send(embed = embed3)
            s.subtract(ctx.guild.name,user.id,user2_cash)
            s.add(ctx.guild.name,ctx.author.id,user2_cash)
        elif str(reaction2) == "🪨":
            embed2.set_thumbnail(url = c)
            await ctx.channel.send(embed = embed2)
            s.subtract(ctx.guild.name,ctx.author.id,user1_cash)
            s.add(ctx.guild.name,user.id,user1_cash)
        else:
            await ctx.channel.send(embed = embed4)
    
    s.Discon()
    
@rps.error
async def rps_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)
            
@bot.command(description = "Play Tic Tac Toe with bot or someone else \n No input is for singleplayer \n Type 'stop' to stop game")
@commands.cooldown(1,15,commands.BucketType.user)
async def tictactoe(ctx,user : discord.User):
    
    def check(g):
        return (g.author == dict[USER]["user"] and g.content in ValidInp and g.content not in TrackerList) or g.content == "stop"
    def Checkwinlist(list):
        
        win = [["a1","a2","a3"],["a1","a3","a2"],["a2","a1","a3"],["a2","a3","a1"],["a3","a1","a2"],["a3","a2","a1"]
            ,["b1","b2","b3"],["b1","b3","b2"],["b2","b1","b3"],["b2","b3","b1"],["b3","b1","b2"],["b3","b2","b1"]
            ,["c1","c2","c3"],["c1","c3","c2"],["c2","c1","c3"],["c2","c3","c1"],["c3","c1","c2"],["c3","c2","c1"]
            ,["a1","b1","c1"],["a1","c1","b1"],["b1","a1","c1"],["b1","c1","a1"],["c1","a1","b1"],["c1","b1","a1"]
            ,["a2","b2","c2"],["a2","c2","b2"],["b2","a2","c2"],["b2","c2","a2"],["c2","a2","b2"],["c2","b2","a2"],
            ["a3","b3","c3"],["a3","c3","b3"],["b3","a3","c3"],["b3","c3","a3"],["c3","a3","b3"],["c3","b3","a3"],
            ["a1","b2","c3"],["a1","c3","b2"],["b2","a1","c3"],["b2","c3","a1"],["c3","a1","b2"],["c3","b2","a1"],
            ["a3","b2","c1"],["a3","c1","b2"],["b2","a3","c1"],["b2","c1","a3"],["c1","a3","b2"],["c1","b2","a3"]]
        
        for a in win:
            if (a[0] in list and a[1] in list) and a[2] in list:
                return True
        
    img = Image.open("base.png")
    img1 = img.copy()
    R = str(r.randrange(1,100))
    img1.save(fr'C:\Users\callm\Desktop\Python Files\{R}.png')
    
    turn_count = 0 # max 9
    TrackerList = []
    ValidInp = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
    
    dict = {"user1":{"user":ctx.author,"symbol-image":r"C:\Users\callm\Desktop\Python Files\circle.png","UserTrack":[]},
            "user2":{"user":user,"symbol-image":r"C:\Users\callm\Desktop\Python Files\cross.png","UserTrack":[]}}
    
    while True:
        for USER in dict:
            if turn_count >= 9:
                await ctx.channel.send(f"**Its a tie between {user.mention} and {ctx.author.mention}!!**",file = discord.File(fr'C:\Users\callm\Desktop\Python Files\{R}.png'))
                os.remove(fr'C:\Users\callm\Desktop\Python Files\{R}.png')
                return
            
            g = await ctx.channel.send(f"{dict[USER]['user'].mention}'s turn.",file = discord.File(fr'C:\Users\callm\Desktop\Python Files\{R}.png'))
            msg = await bot.wait_for('message',check = check,timeout = 60)
            
            if 'stop' == msg.content.lower():
                await ctx.channel.send("🛑 Stopped game 🛑")
                os.remove(fr'C:\Users\callm\Desktop\Python Files\{R}.png')
                return
            
            elif msg.content in ValidInp and msg.content not in dict[USER]["UserTrack"]:
                edit(fr'C:\Users\callm\Desktop\Python Files\{R}.png',msg.content,dict[USER]["symbol-image"],R)
                dict[USER]["UserTrack"].append(msg.content)
                TrackerList.append(msg.content)
                turn_count += 1
                await g.delete()
                await msg.delete()
                
            
            if Checkwinlist(dict[USER]["UserTrack"]):
                await ctx.channel.send(f"{dict[USER]['user'].mention} is the winner!",file = discord.File(fr'C:\Users\callm\Desktop\Python Files\{R}.png'))
                os.remove(fr"C:\Users\callm\Desktop\Python Files\{R}.png")
                await g.delete()
                await msg.delete()
                return
            
@tictactoe.error
async def tictactoe_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)

@bot.command(description = "Registers the server")
@commands.cooldown(1,60,commands.BucketType.user)
async def register(ctx):
    s = sql()
    g = s.register(ctx.guild.name)
    if g:
        a = "Server Already Registered"
        colour = 0xFF0000
    else:
         a = "Server Registered"
         colour = 0x008000 
    embed = discord.Embed(title= a,colour=colour)
    await ctx.channel.send(embed=embed)
    
    s.Discon()
    
@register.error
async def register_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)

@bot.command(description = "Registers the User")
@commands.cooldown(1,60,commands.BucketType.user)
async def uregister(ctx):
    s = sql()
    g = s.register_user(str(ctx.guild.name),int(ctx.author.id),ctx.author.name)
    if g:
        a,b = "Error  ❌","Please check if the server is registered \n OR you already have registered"
    else:
        a,b = "Registered ☑️","Now you can check balance and gain/lose money" 
    embed = discord.Embed(title=a,description=b,colour=0xffff00)   
    await ctx.channel.send(embed=embed)
    
    s.Discon()

@uregister.error
async def uregister_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)

@bot.command(description = "Shows your balance")
@commands.cooldown(1,10,commands.BucketType.user)
async def balance(ctx):
    s = sql()
    g = s.balance(ctx.guild.name,ctx.author.id)
    if g == None:
        await ctx.channel.send(f"{ctx.author.mention} or the server is not registered")
    else:
        embed = discord.Embed(title=f"{ctx.author.name}'s Balance",description=f"${g}",colour=0xffff00)
        await ctx.reply(embed=embed)
        
    s.Discon()

@balance.error
async def balance_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)

@bot.command(description= "Shows Leaderboard for Coins in the server")
async def lb(ctx):
    string = ""
    d = {1:':one:',2:':two:',3:':three:',4:':four:',5:':five:',6:':six:',7:':seven:',8:':eight:',9:':nine:',10:':keycap_ten:'}
    s = sql()
    a = s.leaderboard(ctx.guild.name) 
    rang = len(a)
    for i in range(1,rang+1):
        if i in d:
            string += f"{d[i]} ```{a[i-1][0]} - ${a[i-1][2]}``` \n"
        else:
            string += f"{i}. ```{a[i-1][0]} - ${a[i-1][2]}` \n"
    embed = discord.Embed(title = f"{ctx.guild.name} Leaderboard",description=string,colour=0x00ffff)
    await ctx.reply(embed=embed)
    
    s.Discon()

@lb.error
async def lb_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)
    
        
@bot.command()
async def upload(ctx, attachment: discord.Attachment):
    await ctx.send(f'<{attachment.url}>') 
    
    
@bot.command(name = "gif",description="Converts provided Video (.MP4) to GIF format")
@commands.cooldown(1,15,commands.BucketType.user)
async def convert(ctx,attachment:discord.Attachment):
    name = attachment.filename
    await attachment.save(fp = fr"C:\Users\callm\Desktop\Python Files\{name}")       # type: ignore
    IntName = Converter.convert(name)
    await ctx.channel.send(file = discord.File(fp = fr"C:\Users\callm\Desktop\Python Files\{IntName}.gif"))
    os.remove(f"{IntName}.gif")
    os.remove(f'{name}')
    print('done')

@convert.error
async def convert_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)
    
@bot.command(description = "Bet with users")
@commands.cooldown(1,10,commands.BucketType.user)
async def bet(ctx,user:discord.User):
    s = sql()
    colour = r.choice([0xff0000,0xff9000,0xfff500,0x55ff00,0x00fffc,0x0091ff,0xaa00ff,0xff007e])

    balA = s.balance(ctx.guild.name,ctx.author.id)
    balB = s.balance(ctx.guild.name,user.id)
    val1 = 0
    val2 = 0
    
    def check1(msg):
        return msg.content.isdigit() and msg.author == ctx.author and int(msg.content) <= balA
    def check2(msg):
        return msg.content.isdigit() and msg.author == user and int(msg.content) <= balB
    

    embed = discord.Embed(title = f"{ctx.author.name} Enter money",description=f"**BALANCE ==> ${balA}**",colour=colour)
    embed2 = discord.Embed(title=f"{user.name} Enter money",description=f"**BALANCE ==> ${balB}**",colour=colour)
    
    await ctx.channel.send(f"{ctx.author.mention}",embed = embed)
    g = await bot.wait_for("message",check=check1,timeout=120.0)
    val1 = int(g.content)
    print(val1)

    await ctx.channel.send(f"{user.mention}",embed=embed2)
    g2 = await bot.wait_for("message",check=check2,timeout=120.0)
    val2 = int(g2.content)
    print(val2)
    
    def choicer():
        t = r.choice([
        'https://cdn.discordapp.com/attachments/795499856374267924/1093654821422239895/image.png',
        'https://cdn.discordapp.com/attachments/795499856374267924/1093655061911060480/image.png',
        'https://cdn.discordapp.com/attachments/795499856374267924/1093692564881813524/image.png',
        'https://cdn.discordapp.com/attachments/795499856374267924/1093692689830125678/image.png',
        'https://cdn.discordapp.com/attachments/795499856374267924/1093692850794934344/image.png',
        'https://cdn.discordapp.com/attachments/795499856374267924/1093692991291527239/image.png'])
        return t
    
    embed_start = discord.Embed(title="Rolling Dice...")
    embed_start.set_thumbnail(url=choicer())
    mssg = await ctx.channel.send(embed = embed_start)
    await asyncio.sleep(1)
    
    await mssg.edit(embed=embed_start.set_thumbnail(url=choicer()))
    await asyncio.sleep(1)
    await mssg.edit(embed=embed_start.set_thumbnail(url=choicer()))

        
    
    R1 = int(r.randint(2,20))
    R2 = int(r.randint(2,20))
    
    if R1 > R2:                 # CTX AUTHOR WIN
        g = s.add(ctx.guild.name,ctx.author.id,val2)
        s.subtract(ctx.guild.name,user.id,val2)
        embed_finish = discord.Embed(title=f"{ctx.author.name} VS {user.name}",description=f"**              {ctx.author.mention} WINS ${val2}** \n  \n {ctx.author.name} rolled {R1}      {user.name} rolled {R2}"
                                        ,colour = r.choice([0xff0000,0xff9000,0xfff500,0x55ff00,0x00fffc,0x0091ff,0xaa00ff,0xff007e]))
        await mssg.edit(embed=embed_finish)
        if g:
            print("FAIL")
        
    elif R2 > R1:                  # USER WIN
        g = s.add(ctx.guild.name,user.id,val1)
        s.subtract(ctx.guild.name,ctx.author.id,val1) 
        embed_finish = discord.Embed(title=f"{ctx.author.name} VS {user.name}",description=f"**              {user.mention} WINS ${val1}** \n \n {ctx.author.name} rolled {R1}      {user.name} rolled {R2}"
                                     ,colour = r.choice([0xff0000,0xff9000,0xfff500,0x55ff00,0x00fffc,0x0091ff,0xaa00ff,0xff007e]))
        await mssg.edit(embed=embed_finish)
        if g:
            print("FAIL")
        
    else:
        embed_finish = discord.Embed(title=f"{ctx.author.name} VS {user.name}",description=f"              **IT'S A TIE!** \n \n ```No one won anything. \n Both rolled {R1} and {R2}```")
        await mssg.edit(embed=embed_finish)  
        
    s.Discon()
    
@bet.error
async def bet_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)


@bot.command(description="Searches given word's meanings")
@commands.cooldown(1,10,commands.BucketType.user)
async def meaning(ctx,input):
    try:
        noun,verb,preposition,adverb,article = search(input)
        colour = r.choice([0xff0000,0xff9000,0xfff500,0x55ff00,0x00fffc,0x0091ff,0xaa00ff,0xff007e])
        noun_block = ""
        verb_block = ""
        preposition_block = ""
        adverb_block = ""
        article_block = ""
        if noun != []:
            noun_block = "***__Noun__*** \n \n"
            for i in noun:
                noun_block += "• " + i + "\n" 
        if verb != []:
            verb_block = "***__Verb__*** \n \n"
            for i in verb:
                verb_block += "• " + i + "\n" 
        if preposition != []:
            preposition_block = "***__Preposition__*** \n \n"
            for i in preposition:
                preposition_block += "• " + i + "\n"  
        if adverb != []:
            adverb_block = "***__Adverb__*** \n \n"
            for i in adverb:
                adverb_block += "• " + i + "\n" 
        if article != []:
            article_block = "***__Article__*** \n \n"
            for i in article:
                article_block += "• " + i + "\n" 
        
        text = noun_block +"\n" + verb_block +"\n"+ preposition_block +"\n"+ adverb_block +"\n"+ article_block

        if text.strip() == "":
            await ctx.reply("No Meaning Found.")
        else:
            embed = discord.Embed(title = f"Meaning of '{input}'",description=text,colour=colour)     
            await ctx.reply(embed=embed)
    except: 
        await ctx.reply("No Meaning Found.")

@meaning.error
async def meaning_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)
    
@bot.command(name = "py",description = 'Code python. \n No Inputs or Exception Cases displayed \n SIDE NOTE: you can also print your code using the command `?gpt`')
async def coder(ctx,*,msg):
    if ctx.author.id == 710758283408834612:
        bol,result = Execution.exec(msg)      # Command closed for security purposes
        
        if bol:
            await ctx.channel.send(result)
        else:
            await ctx.channel.send('error')
    else:
        ctx.reply("Permission denied")
        
@bot.command(name = "rd",description = "Downloads Reddit media")
@commands.cooldown(1,15,commands.BucketType.user)
async def download(ctx,url):
    Name = str(r.randint(0,1000))
    try:
        R = Downloader(filename = f"{Name}",max_q = True)
        R.url = url
        R.download()
    except:
        RedDownloader.Download(url,output = Name,quality=720)
    await ctx.message.delete()
    for i in ["mp4","gif","png","jpg","jpeg","m4a","mov"]:
        try:
            file = discord.File(fp = fr"C:\Users\callm\Desktop\Python Files\{Name}.{i}")
            await ctx.channel.send(file = file)
            os.remove(f"{Name}.{i}")
            return
        except:
            continue

@download.error
async def dnwld_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
        await ctx.reply(embed=embed)

# @bot.command(name = "gpt",description = "Talk with Chat GPT 3.5! \n \n ***Note:*** It takes ONE time questions only ")

# @commands.cooldown(1,10,commands.BucketType.user)
# async def gpt(ctx,*,text):
#     try:
#         async def GPT(text):
#             openai.api_key = "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" 

#             chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}])
#             for i in chat_completion:
#                 if i == "choices":
#                     for j in chat_completion[i]: 
#                         return j["message"]["content"]
            
#         ans = GPT(text)
#         embed = discord.Embed(title = "ChatGPT 3.5 Response",description=ans,colour = r.choice([0xff0000,0xff9000,0xfff500,0x55ff00,0x00fffc,0x0091ff,0xaa00ff,0xff007e]))
#         embed.set_thumbnail(url="https://media.discordapp.net/attachments/886281693156233277/1137767972107194418/th-1264273453.jpg") 
        
#     except:
#         embed = discord.Embed(title = "Error!",description="*Sorry for the error from the bot's end*",colour = 0xff0000)
#         embed.set_thumbnail(url="https://media.discordapp.net/attachments/886281693156233277/1137767972107194418/th-1264273453.jpg")
    
#         await ctx.reply(embed = embed)                NOTE : DEPRECIATED

        
# @gpt.error
# async def gpt_error(ctx,error):
    
#     if isinstance(error,commands.CommandOnCooldown):
#         embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
#         await ctx.reply(embed=embed)
        
        

# @bot.command(name="imgai",description="Generates image from ChatGPT's Image version, DALL E.")
# @commands.cooldown(1,10,commands.BucketType.user)
# async def img(ctx,*,prompt):
#     async def gen(prompt):
#         openai.api_key = "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"
#         res = openai.Image.create( prompt=prompt, n=1, size="1024x1024")
#         url = res["data"][0]["url"] #type:ignore
#         await ctx.reply(url)
    
#     await asyncio.create_task(gen(prompt))                    NOTE: DEPRECIATED

# @img.error
# async def img_error(ctx,error):
    
#     if isinstance(error,commands.CommandOnCooldown):
#         embed = discord.Embed(title = "Error!",description=error,colour = 0xff0000)
#         await ctx.reply(embed=embed)


    
#ir3Hhsla6EWPD_vvpD_bmSNsr7W1f_bu             CLIENT SECRET                
bot.run('MTAzMzk3OTUxMTg3Mzc0NDkxNg.G-alAu.Vf8BcYsUYJ4fTKfKATvgP7IHm42hLikk6j5LIg')
