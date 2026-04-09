import random
import discord

def getErrMsg():
    errorMsgs = []
    with open('errors.txt') as file:
        for line in file:
            errorMsgs.append(line.rstrip())
    file.close()
    retIdx = random.randint(0,len(errorMsgs))
    errEmbed = discord.Embed(title="Error",description=errorMsgs[retIdx],color=0xFF0000)
    return(errEmbed)

def adminError(errIdx):
    errorMsgs = []
    with open('errors.txt') as file:
        for line in file:
            errorMsgs.append(line.rstrip())
    file.close()
    return(errorMsgs[int(errIdx)])