import discord
import os
from roller.roller import *
from cart.cart import *
from config.getError import *
from datetime import datetime
# from lenny import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

savedir = './saves'
pastaDir = './pasta'
global LMAO
LMAO = False
global toAnnoy
toAnnoy = 0
global rigDice
rigDice = False

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global LMAO
    global toAnnoy
    global rigDice
    if message.author == client.user:
        return

    if message.content.startswith('DAC-'):
        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f'{message.author} requested DAC! Time: {now}, Command: {message.content}')
        mesg = message.content.split(' ')
        
        if mesg[1] == 'roll':
            await message.reply(embed=commandParseRoller(message.content,rigDice))
        elif mesg[1] == 'rigrolls':
            if message.author.id == 368922517374763009:
                if rigDice:
                    rigDice = False
                else:
                    rigDice = True
        
        elif mesg[1] == 'help':
            f = open("help.txt", "r")
            await message.channel.send(f.read())
            f.close()

        elif mesg[1] == 'load':
            new()
            load(mesg[2])
        elif mesg[1] == 'list':
            await message.reply(embed=printItems())
        elif mesg[1] == 'show':
            listOcarts = ''
            for file in os.listdir(savedir):
                if '.items' in file:
                    strFile = str(file)
                    fName = strFile.split('.items')
                    listOcarts += f'{fName[0]}\n'
            listOcarts = listOcarts.rstrip('\n')
            listCartEmbed = discord.Embed(title="Carts that can be loaded:",description=listOcarts,color=0x7A306C)
            await message.reply(embed=listCartEmbed)
        elif mesg[1] == 'add':
            if mesg[2] == 'item':
                await message.channel.send(addItem(mesg[3],mesg[4],mesg[5]))
            elif mesg[2] == 'carry':
                await message.channel.send(addCarry(mesg[3],mesg[4]))
        elif mesg[1] == 'del':
            if mesg[2] == 'item':
                await message.channel.send(delItem(mesg[3]))
            elif mesg[2] == 'carry':
                await message.channel.send(delCarry(mesg[3]))
        elif mesg[1] == 'save':
            await message.channel.send(save(mesg[2]))
        
        elif mesg[1] == 'pasta':
            pastas = []
            for file in os.listdir(pastaDir):
                pastas.append(file)
            randPast = random.randint(0,len(pastas)-1)
            f = open(f'./pasta/{pastas[randPast]}','r')
            pastaEmbed = discord.Embed(description=f.read(),color=0x523249)
            await message.reply(embed=pastaEmbed)
            f.close()
        elif mesg[1] == 'error':
            if message.author.id == 368922517374763009:
                await message.channel.send(adminError(mesg[2]))
                await message.channel.send(f'<@{368922517374763009}> father, why must you make me error?')
        
        elif mesg[1] == 'annoy':
            if message.author.id == 368922517374763009:
                toAnnoy = int(mesg[2])
                LMAO = True
            else:
                await message.channel.send(f'<@{message.author.id}> sorry bud, but you don\'t get to do that')
        elif mesg[1] == 'annoyStop':
            if message.author.id == 368922517374763009:
                LMAO = False
            else:
                await message.channel.send(f'<@{message.author.id}> sorry bud, but you don\'t get to do that')
        elif mesg[1] == 'say':
            if message.author.id == 368922517374763009:
                chan = client.get_channel(int(mesg[2]))
                send = ''
                for i in mesg[3:]:
                    send += i + ' '
                await chan.send(send)
            else:
                await message.channel.send(f'<@{message.author.id}> sorry bud, but you don\'t get to do that')
        
        # elif mesg[1] == 'lenny':
        #     await message.channel.send(lenny_face)
        # elif mesg[1] == 'randlenny':
        #     await message.channel.send(lenny())
        else:
            await message.reply(embed=getErrMsg())
    
    if LMAO == True:
        eef = await client.fetch_user(toAnnoy)
        await eef.send('Lmao get DM\'d on')


token = open('tokenfile','r').readline()
client.run(token)

        #if message.author.id == 237448487187251201:
        #    await message.channel.send(f'<@{message.author.id}> fuk u ya bitch')

# to run DAC, open windows terminal, type 'd:', then make sure in JERT, then run 'py -3 example_bot.py'
# on UNIX, navigate to the directory this file is in and run 'python3 ./dac_main.py'