import discord
import random
from config.error_handling.getError import *

boostDie = {1:"0.0",2:"0.0",3:"1.0",4:"1.1",5:"0.2",6:"0.1"}
setbackDie = {1:"0.0",2:"0.0",3:"1.0",4:"1.0",5:"0.1",6:"0.1"}
abilityDie = {1:"0.0",2:"1.0",3:"1.0",4:"2.0",5:"0.1",6:"0.1",7:"1.1",8:"0.2"}
difficultyDie = {1:"0.0",2:"1.0",3:"2.0",4:"0.1",5:"0.1",6:"0.1",7:"0.2",8:"1.1"}
proficiencyDie = {1:"0.0.0",2:"0.1.0",3:"0.1.0",4:"0.2.0",5:"0.2.0",6:"0.0.1",7:"0.1.1",8:"0.1.1",9:"0.1.1",10:"0.0.2",11:"0.0.2",12:"1.1.0"}
challengeDie = {1:"0.0.0",2:"0.1.0",3:"0.1.0",4:"0.2.0",5:"0.2.0",6:"0.0.1",7:"0.0.1",8:"0.1.1",9:"0.1.1",10:"0.0.2",11:"0.0.2",12:"1.1.0"}
forceDie = {1:"1.0",2:"1.0",3:"1.0",4:"1.0",5:"1.0",6:"1.0",7:"2.0",8:"0.1",9:"0.1",10:"0.2",11:"0.2",12:"0.2"}

def rollSWRPG(cmd):
    b = 0
    s = 0
    a = 0
    d = 0
    p = 0
    c = 0
    f = 0

    succ = 0
    adv = 0
    fail = 0
    threat = 0
    tri = 0
    desp = 0
    dark = 0
    light = 0

    swSplit = cmd.split(' ')

    i = 0
    while i < 3:
        swSplit.pop(0)
        i += 1
    
    for j in swSplit:
        toAdd = j
        if 'bk' in j:
            toAdd = int(j.replace('bk',''))
            s = toAdd
        elif 'b' in j:
            toAdd = int(j.replace('b',''))
            b = toAdd
        elif 'g' in j:
            toAdd = int(j.replace('g',''))
            a = toAdd
        elif 'p' in j:
            toAdd = int(j.replace('p',''))
            d = toAdd
        elif 'y' in j:
            toAdd = int(j.replace('y',''))
            p = toAdd
        elif 'r' in j:
            toAdd = int(j.replace('r',''))
            c = toAdd
        elif 'f' in j:
            toAdd = int(j.replace('f',''))
            f = toAdd
        elif 'w' in j:
            toAdd = int(j.replace('w',''))
            f = toAdd

    for k in range(0,b):
        bresult = boostDie[random.randint(1,6)]
        bresult = bresult.split('.')
        succ += int(bresult[0])
        adv += int(bresult[1])

    for l in range(0,s):
        sresult = setbackDie[random.randint(1,6)]
        sresult = sresult.split('.')
        fail += int(sresult[0])
        threat += int(sresult[1])

    for m in range(0,a):
        aresult = abilityDie[random.randint(1,8)]
        aresult = aresult.split('.')
        succ += int(aresult[0])
        adv += int(aresult[1])

    for n in range(0,d):
        dresult = difficultyDie[random.randint(1,8)]
        dresult = dresult.split('.')
        fail += int(dresult[0])
        threat += int(dresult[1])

    for o in range(0,p):
        presult = proficiencyDie[random.randint(1,12)]
        presult = presult.split('.')
        tri += int(presult[0])
        succ += int(presult[1])
        adv += int(presult[2])

    for q in range(0,c):
        cresult = challengeDie[random.randint(1,12)]
        cresult = cresult.split('.')
        desp += int(cresult[0])
        fail += int(cresult[1])
        threat += int(cresult[2])

    for r in range(0,f):
        fresult = forceDie[random.randint(1,12)]
        fresult = fresult.split('.')
        dark += int(fresult[0])
        light += int(fresult[1])
    
    swembed = discord.Embed(title='SWRPG Dice Roll',color=0x176087)
    swRetStr = f'Success: {succ} - Failure: {fail}\nAdvantage: {adv} - Threat: {threat}\nTriumph: {tri} - Despair: {desp}\nLight: {light} - Dark: {dark}'
    swembed.add_field(name="Raw Results",value=swRetStr,inline=False)
    
    swRetStrCanc = ''

    if succ > fail:
        succ -= fail
        fail = 0
        swRetStrCanc += f"Successes: {succ}\n"
    elif fail > succ:
        fail -= succ
        succ = 0
        swRetStrCanc += f"Failures: {fail}\n"
    elif succ == fail:
        succ = 0
        fail = 0
    
    if adv > threat:
        adv -= threat
        threat = 0
        swRetStrCanc += f"Advantages: {adv}\n"
    elif threat > adv:
        threat -= adv
        adv = 0
        swRetStrCanc += f"Threats: {threat}\n"
    elif adv == threat:
        adv = 0
        threat = 0

    if tri > 0:
        swRetStrCanc += f"Triumphs: {tri}\n"
    if desp > 0:
        swRetStrCanc += f"Despairs: {desp}\n"
    if light > 0:
        swRetStrCanc += f"Light Force Points: {light}"
    if dark > 0:
        swRetStrCanc += f"Dark Force Points: {dark}"

    if swRetStrCanc == '':
        swRetStrCanc = "All results have cancelled out!"

    swembed.add_field(name="Cancelled Out Results",value=swRetStrCanc,inline=False)

    return(swembed)

def rollDie(amt,diesize,bonus,mod,raw):
    """
    rolls a die
    """
    rollsFor = "Results for: "
    rollsFor += str(amt) + f'd{str(diesize)}'
    if bonus != 0:
        rollsFor += f' {bonus}'
    if mod != 'None':
        rollsFor += f' {mod}'
    rollEmbed = discord.Embed(title="Dice Roll",description=rollsFor,color=0xB1DDF1)

    if amt == 0:
        amt = 1

    rollMsg = f''
    bonusSign = '+'

    if bonus != 0:
        if '+' in bonus:
            bonus = bonus.replace('+','')
        elif '-' in bonus:
            bonusSign = '-'
    bonus = int(bonus)

    rolls = []
    rollsString = ''
    for i in range(0,amt):
        roll = random.randint(1,diesize)
        rollMod = roll + bonus
        rolls.append(rollMod)
        if bonus != 0:
            rollsString += f'#{i}: {rollMod} ({roll}{bonusSign}{bonus})\n'
        elif bonus == 0:
            rollsString += f'#{i}: {rollMod}\n'

    if 'kh' in mod:
        rollsString = ''
        keep = mod.split('kh')
        numKeep = int(keep[1])
        sort = sorted(rolls, reverse=True)
        rolls = sort[:numKeep]
        for i in range(0,len(rolls)):
            if bonus != 0:
                rollsString += f'#{i}: {rolls[i]} ({(rolls[i])-bonus}{bonusSign}{bonus})\n'
            elif bonus == 0:
                rollsString += f'#{i}: {rolls[i]}\n'
    else:
        pass
    
    rollMsg += f'\n{rollsString}'

    if raw:
        rolls = str(rolls)
        if len(rolls) <= 1024:
            rollEmbed.add_field(name="Raw Results",value=rolls,inline=False)
            return(rollEmbed)
        else:
            errEmbed = discord.Embed(title="Error",description='I\'m sorry, but that roll generates a message longer than 1024 characters, which is longer than Discord\'s max embed message length. Please try again and reduce your roll amount.',color=0xFF0000)
            return(errEmbed)
    elif len(rollMsg) <= 1024:
        rollEmbed.add_field(name="Results",value=rollMsg,inline=False)
        return(rollEmbed)
    else:
        errEmbed = discord.Embed(title="Error",description='I\'m sorry, but that roll generates a message longer than 1024 characters, which is longer than Discord\'s max embed message length. Please try again and reduce your roll amount.',color=0xFF0000)
        return(errEmbed)

def rollRig():
    ...

def isbonus(bonus):
    if bonus.isdigit():
        return True
    elif '+' in bonus:
        return True
    elif '-' in bonus:
        return True
    else:
        return False

def commandParseRoller(cmd,rig):
    retCol = 0xB1DDF1
    split = cmd.split(' ')
    if split[2].lower() == 'sw':
        retCol = 0x176087
        return(rollSWRPG(cmd))
    #split[0] will be 'DAC-', split[1] will be 'roll'
    diesize = split[2].split('d')
    if diesize[0] == '':
        diesize[0] = 0
    rawroll = False
    if split[-1] == 'raw':
        rawroll = True
        split.pop(-1)
    try:
        if len(split) == 5:
            if rig:
                return(rollDie(int(diesize[0])*2,int(diesize[1]),split[3],f'kh{int(diesize[0])}',rawroll))
            else:
                return(rollDie(int(diesize[0]),int(diesize[1]),split[3],split[4],rawroll))
        elif len(split) == 4:
            if isbonus(split[3]):
                if rig:
                    return(rollDie(int(diesize[0])*2,int(diesize[1]),split[3],f'kh{int(diesize[0])}',rawroll))
                else:
                    return(rollDie(int(diesize[0]),int(diesize[1]),split[3],'None',rawroll))
            else:
                if rig:
                    return(rollDie(int(diesize[0])*2,int(diesize[1]),0,f'kh{int(diesize[0])}',rawroll))
                else:
                    return(rollDie(int(diesize[0]),int(diesize[1]),0,split[3],rawroll))
        elif len(split) == 3:
            if rig:
                return(rollDie(int(diesize[0])*2,int(diesize[1]),0,f'kh{int(diesize[0])}',rawroll))
            else:
                return(rollDie(int(diesize[0]),int(diesize[1]),0,'None',rawroll))
    except:
        return(getErrMsg())