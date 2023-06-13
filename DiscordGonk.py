import discord
from discord.ext import commands
import random as r
import time
from pytube import YouTube
from subprocess import check_output
import os
from subprocess import run
from PIL import Image
from file_editor import *
from discord.ext import commands
from MYsql import *
from moviepy.editor import VideoFileClip
import asyncio
from Scraper1 import search
import Converter

description = '''Pretty epic bot.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.all()
intents.members = True
intents.message_content = True


help_command = commands.DefaultHelpCommand(no_category = "Commands"
                    ,default_argument_description = " ->  INPUT",sorted=True)
bot = commands.Bot(command_prefix='?', description=description
                   , intents=intents,help_command=help_command)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Life"))
    await bot.tree.sync()



@bot.hybrid_command(name="slash")
async def slash(ctx): 
   await ctx.send("You executed the slash command!")
   
@bot.command()
async def stop(ctx):
    if ctx.author.id == 710758283408834612:
        await ctx.channel.send('Closing')
        await bot.close()


@bot.command(description="Gonk's Introduction")
async def intro(ctx):
    await ctx.send(f"My name is <@{bot.user.id}>")
    await ctx.send(f"Hi <@{ctx.author.id}>")
    
@bot.command(description = "Embeds anything")
async def embed(ctx,Title,description,thumbnail = None):
    embed=discord.Embed(title=Title, description=description, color=0x00ff00)
    embed.set_image(url= thumbnail)
    await ctx.send(embed = embed)
    await ctx.message.delete()


@bot.command(name = "yt", description = "Downloads YT videos and sends it") 
async def youtube(ctx,link):
    await ctx.channel.send("Working on it...")
    name = str(r.randint(0,999)) + ".mp4" 
    try:
        run(f"youtube-dl --output {name} --max-filesize 25m -f mp4 {link}")
        await ctx.channel.send(file=discord.File(fp = f"{name}"))
        os.remove(path=name)
    except:
        await ctx.reply("Error \n *maybe because of a too large file/video?*")

            

@bot.command(name = 'yts',description = "Download Mp3 songs from YT")
async def song(ctx,link):
    await ctx.channel.send("Working on it...")
    name = str(r.randint(0,999)) + ".m4a"
    try:
        run(f'youtube-dl -x --output {name} --max-filesize 25m -f m4a {link}')
        await ctx.channel.send(file=discord.File(fp = f"{name}"))
        os.remove(path=name)
    except:
        await ctx.reply("Error \n *-maybe because of a too large file/video?*")
                       
@bot.command(description = "Encodes any Big sentence")
async def encode(ctx,*,Sentence):
    G = ""
    if len(Sentence) not in [1,2,3,4,5,6]:
        L = {'a':'z','b':'y','c':'x','d':'w','e':'v',
                'f':'u','g':'t','h':'s','i':'r','j':'q',
                'k':'p','l':'o','m':'n','n':'m','o':'l',
                'p':'k','q':'j','r':'i','s':'h','t':'g',
                'u':'f','v':'e','w':'d','x':'c','y':'b',
                'z':'a',' ':' '}
        for i in Sentence:
            if i in L:
                G += L[i]
        await ctx.send(G)
    else:
        await ctx.send("Only few letters given *[ATLEAST 7]*")
        
@bot.command(description = "Paste any encoded sentence from this bot to decode")
async def decode(ctx,*,Sentence):
    G = ""
    L = {'a':'z','b':'y','c':'x','d':'w','e':'v',
            'f':'u','g':'t','h':'s','i':'r','j':'q',
            'k':'p','l':'o','m':'n','n':'m','o':'l',
            'p':'k','q':'j','r':'i','s':'h','t':'g',
            'u':'f','v':'e','w':'d','x':'c','y':'b',
            'z':'a',' ':' '}
    for i in Sentence:
        if i in L:
            G += L[i]
    await ctx.send(G)

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
        
    embed2.set_image(url=c)
    thumbnail = "https://media.tenor.com/a2fp2WK79dEAAAAi/one-pound.gif"
    embed.set_image(url = thumbnail)
    
    msg = await ctx.send(embed=embed)
    time.sleep(3)
    await msg.edit(embed=embed2)
    
@bot.command(description = "Use Magik ball to answer your question")
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


@bot.command(description = "Guess the number fom 1 to 20")
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

@bot.command(description = 'Pong')
async def ping(ctx):
    await ctx.channel.send(f'Ping is {bot.latency}')

@bot.command(description = "play Rock Paper Scissor with bot or someone else \n No input is for singleplayer")
async def rps(ctx, user : discord.User=None):
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
                    if int(msg2.content) <= B and int(msg2.content) >= int(msg1.content):
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
    
    
    reaction1,user1 = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    
    if user.id == 710758283408834612:
        await user.send(f'{user1} took {reaction1}')
    
    if user == None:
        reaction2 = r.choice(["🪨","📄","✂️"])
        user2 = bot.user
        b = f"<@{bot.user.id}>"
        c = "https://cdn.discordapp.com/avatars/1033979511873744916/7a2a32db1f88fbf81993a55cea0dcf54.png"
    else:
        msg2 = await user.send(embed = embed1)
        await msg2.add_reaction("🪨")
        await msg2.add_reaction("📄")
        await msg2.add_reaction("✂️")
        
        reaction2,user2 = await bot.wait_for('reaction_add', timeout=60.0, check=check)
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
            
@bot.command(description = "play Tic Tac Toe with bot or someone else \n No input is for singleplayer \n Type 'stop' to stop game")
async def tictactoe(ctx,user : discord.User):
    s = sql()
    count = 0
    def check(g):
        return g.author == a and g.content in D or g.content == "stop"
    D = {'a1':(0,0),'a2':(339,0),'a3':(695,0)
         ,'b1':(0,339),'b2':(339,339),'b3':(695,339)
         ,'c1':(0,695),'c2':(339,695),'c3':(695,695)}
    img = Image.open("base.png")
    img1 = img.copy()
    R = str(r.randrange(1,100))
    file2 = fr'C:\Users\callm\Dropbox\My PC (AniruddhPC1001)\Desktop\Python Files\{R}.png'
    img1.save(file2)
    s = {ctx.author:r"C:\Users\callm\Dropbox\My PC (AniruddhPC1001)\Desktop\Python Files\cross.png",
                  user: r"C:\Users\callm\Dropbox\My PC (AniruddhPC1001)\Desktop\Python Files\circle.png"}
    L1 = []   #ctx.author
    L2 = []   #user
    win = [["a1","a2","a3"],["a1","a3","a2"],["a2","a1","a3"],["a2","a3","a1"],["a3","a1","a2"],["a3","a2","a1"]
           ,["b1","b2","b3"],["b1","b3","b2"],["b2","b1","b3"],["b2","b3","b1"],["b3","b1","b2"],["b3","b2","b1"]
           ,["c1","c2","c3"],["c1","c3","c2"],["c2","c1","c3"],["c2","c3","c1"],["c3","c1","c2"],["c3","c2","c1"]
           ,["a1","b1","c1"],["a1","c1","b1"],["b1","a1","c1"],["b1","c1","a1"],["c1","a1","b1"],["c1","b1","a1"]
           ,["a2","b2","c2"],["a2","c2","b2"],["b2","a2","c2"],["b2","c2","a2"],["c2","a2","b2"],["c2","b2","a2"],
           ["a3","b3","c3"],["a3","c3","b3"],["b3","a3","c3"],["b3","c3","a3"],["c3","a3","b3"],["c3","b3","a3"],
           ["a1","b2","c3"],["a1","c3","b2"],["b2","a1","c3"],["b2","c3","a1"],["c3","a1","b2"],["c3","b2","a1"],
           ["a3","b2","c1"],["a3","c1","b2"],["b2","a3","c1"],["b2","c1","a3"],["c1","a3","b2"],["c1","b2","a3"]]
    while True:
        for a in s:
            count = 0
            g = await ctx.channel.send(f"{a.mention}'s turn.",file = discord.File(file2))
            msg = await bot.wait_for('message',check = check)
            if msg.content == "stop":
                await ctx.channel.send("🛑 Stopped game 🛑")
                return
            if msg:
                edit(file2,msg.content,s[a],R)
                if a == ctx.author:
                    L1.append(str(msg.content))
                elif a == user:
                    L2.append(str(msg.content))
            for over in L1:
                count +=1
                if count == 5:
                    await ctx.channel.send(f"**Its a tie between {user.mention} and {ctx.author.mention}!!**")
                    return
            for c in win:
                count = 0
                for b in c:
                    if b in L1:        
                        count += 1
                        if count == 3:
                            e = discord.Embed(description="They win $500!",colour=0x008000)
                            s = sql()
                            s.add(ctx.guild.name,ctx.author.id,500)
                            await ctx.channel.send(f"{ctx.author.mention} is the winner!",embed = e)
                            await ctx.channel.send(file = discord.File(file2))
                            await g.delete()
                            await msg.delete()
                            return
            for c in win:
                count = 0 
                for b in c:       
                    if b in L2:        
                        count += 1
                        if count == 3:
                            e = discord.Embed(description="They win $500!",colour=0x008000)
                            s = sql()
                            s.add(ctx.guild.name,user.id,500)
                            await ctx.channel.send(f"{user.mention} is the winner!",embed = e)
                            await ctx.channel.send(file = discord.File(file2))
                            await g.delete()
                            await msg.delete()
                            return
            await g.delete()            
            await msg.delete()

@bot.command(description = "Registers the server")
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

@bot.command(description = "Registers the User")
async def uregister(ctx):
    s = sql()
    g = s.register_user(str(ctx.guild.name),int(ctx.author.id),ctx.author.name)
    if g:
        a,b = "Error  ❌","Please check if the server is registered \n OR you already have registered"
    else:
        a,b = "Registered ☑️","Now you can check balance and gain/lose money" 
    embed = discord.Embed(title=a,description=b,colour=0xffff00)   
    await ctx.channel.send(embed=embed)

@bot.command(description = "Shows your balance")
async def balance(ctx):
    s = sql()
    g = s.balance(ctx.guild.name,ctx.author.id)
    if g == None:
        await ctx.channel.send(f"{ctx.author.mention} or the server is not registered")
    else:
        embed = discord.Embed(title=f"{ctx.author.name}'s Balance",description=f"${g}",colour=0xffff00)
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
    
        
@bot.command()
async def upload(ctx, attachment: discord.Attachment):
    await ctx.send(f'<{attachment.url}>') 
    
    
@bot.command(name = "gif",description="Converts provided Video (.MP4) to GIF format")
async def convert(ctx,attachment:discord.Attachment):
    name = attachment.filename
    print(name)
    await attachment.save(fp = fr"C:\Users\callm\Dropbox\My PC (AniruddhPC1001)\Desktop\Python Files\{name}")    
    IntName = Converter.convert(name)
    await ctx.channel.send(file = discord.File(fp = fr"C:\Users\callm\Dropbox\My PC (AniruddhPC1001)\Desktop\Python Files\{IntName}.gif"))
    os.remove(f"{IntName}.gif")
    
@bot.command(description = "Bet with users")
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
    time.sleep(1)
    
    await mssg.edit(embed=embed_start.set_thumbnail(url=choicer()))
    time.sleep(1)
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


@bot.command(description="Searches given word's meanings")
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
    
#ir3Hhsla6EWPD_vvpD_bmSNsr7W1f_bu             CLIENT SECRET                
bot.run('MTAzMzk3OTUxMTg3Mzc0NDkxNg.GtDGD6.fit5-gX0L8pI-w7r0b9wJJisd95FCflDGdRx_k')
