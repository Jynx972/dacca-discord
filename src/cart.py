from item import *
from carrier import *
import pickle
import discord

items = []
carriers = []
global currentName
currentName = "placeholder"
global currentWeight
currentWeight = 0
global totalCap
totalCap = 0
global weightUnit
weightUnit = "lbs"
global cartActive
cartActive = False

'''
now handled by DAC
def addWhich():
    """
    Selects whether to add a carrier or item
    """
    sel = input("Would you like to add an item or carrier? ")
    if sel.lower() == 'item':
        addItem()
    elif sel.lower() == 'carrier':
        addCarry()
'''

def addItem(name, weight, amount):
    """
    Adds an item to the storage system
    """
    global currentWeight
     
    if weight.replace('.','',1).isdigit():
        weight = float(weight)
        if amount.replace('.','',1).isdigit():
            amount = float(amount)
            items.append(item(name, weight, amount))
            currentWeight += item.getTotWeight(items[-1])
        else:
            return('Amount is either missing or not a number')
    else:
        return('Weight is either missing or not a number')

    return('Succesfully added an item!')

def addCarry(ctype, capacity):
    """
    Adds a carrier to the storage system
    """
    global totalCap
    if capacity.replace('.','',1).isdigit():
        capacity = float(capacity)
        carriers.append(carrier(ctype, capacity))
        totalCap += capacity
    else:
        return('Carrying capacity either doesn\'t exist or is not a valid number')

    return('Added a carrier!')
        
'''
handled by DAC
def delWhich():
    """
    Selects whether to delete an item or carrier
    """
    sel = input("Would you like to delete an item or carrier? ")
    if sel.lower() == 'item':
        delItem()
    elif sel.lower() == 'carrier':
        delCarry()
'''

def delItem(delIdx):
    """
    Removes an item from the system
    """
    global currentWeight
    if delIdx.isdigit():
        delIdx = int(delIdx)
        try:
            currentWeight -= item.getTotWeight(items[delIdx-1])
            items.pop(delIdx-1)
        except:
            return("No item exists at that index")
    else:
        return("Not a valid index number")
    
    return('Deleted item')

def delCarry(delCIdx):
    """
    Removes a carrier from the system
    """
    global totalCap
    if delCIdx.isdigit():
        delCIdx = int(delCIdx)
        try:
            totalCap -= carrier.getCapacity(carriers[delCIdx-1])
            carriers.pop(delCIdx-1)
        except:
            return("No carrier exists at that index")
    else:
        return("Not a valid index number")
    
    return('Deleted carrier')

def updWhich():
    """
    Selects whether to update an item or carrier
    """
    sel = input("Would you like to update an item or carrier? ")
    if sel.lower() == 'item':
        updateItem()
    elif sel.lower() == 'carrier':
        updateCarrier()

def updateItem():
    """
    Updates an item
    """
    updIdx = input("Index of the item you want to update (The number next to it when you run the list command): ")
    if updIdx.isdigit():
        updIdx = int(updIdx) - 1
    else:
        print("Not a valid index number")
    toEdit = str(input("What attribute do you want to edit? (name, weight, amount): "))

    if toEdit.lower() == 'name':
        newName = str(input("What is the new name of the item? "))
        items[updIdx].name = newName
    elif toEdit.lower() == 'weight':
        newWeight = input("What is the new weight of the item? (please note this is the weight of each individual item not the total): ")
        if newWeight.replace('.','',1).isdigit():
            newWeight = float(newWeight)
            items[updIdx].itemWeight = newWeight
        else:
            print('New weight must be a valid integer or float')
    elif toEdit.lower() == 'amount':
        newAmount = input("What is the new amount of the item? ")
        if newAmount.replace('.','',1).isdigit():
            newAmount = float(newAmount)
            items[updIdx].amount = newAmount
        else:
            print('New amount must be a valid integer or float')
    else:
        print("That is not a valid item attribute")

def updateCarrier():
    """
    Updates a carrier
    """
    cUpdIdx = input("Index of the carrier you want to update (The number next to it when you run the list command): ")
    if cUpdIdx.isdigit():
        cUpdIdx = int(cUpdIdx) - 1
    else:
        print("Not a valid index number")
    cToEdit = str(input("What attribute do you want to edit? (Type/Name or capacity) "))

    if cToEdit.lower() in ['name', 'type']:
        newType = str(input("New type/name: "))
        carriers[cUpdIdx].type = newType
    elif cToEdit.lower() == 'capacity':
        newCapacity = input("New carry capacity: ")
        if newCapacity.replace('.','',1).isdigit():
            newCapacity = float(newCapacity)
            carriers[cUpdIdx].capacity = newCapacity
        else:
            print('New weight must be a valid integer or float')
    else:
        print("That is not a valid carrier attribute")

def printItems():
    """
    Prints the storage system
    """
    global currentName
    cartEmbed = discord.Embed(title=currentName,color=0xB288C0)
    global currentWeight
    global totalCap
    retstring = ''
    for i in carriers:
        retstring += f'{carriers.index(i)+1} - Type: {carrier.getType(i)}, Capacity: {carrier.getCapacity(i)}{weightUnit}\n'

    retstring += f'\nTotal Carrying Capacity: {totalCap}{weightUnit}\n'
    retstring += f'Currently Carrying: {currentWeight}{weightUnit}\n'
    retstring += f'Remaining: {totalCap-currentWeight}{weightUnit}\n'

    retstring.strip()
    cartEmbed.add_field(name="Carriers",value=retstring,inline=False)
    retstring = ''
    
    if currentWeight > totalCap:
        retstring += 'SYSTEM OVER CAPACITY, PLEASE REMOVE SOME WEIGHT OR ADD MORE CARRYING CAPACITY\n'
    
    for i in items:
        retstring += f'{items.index(i)+1} - {item.getName(i)}: {item.getTotWeight(i)}{weightUnit}, {item.getAmount(i)}amt ({item.getItemWeight(i)}{weightUnit} per item)\n'
    retstring.strip()
    cartEmbed.add_field(name='Items',value=retstring,inline=False)

    return(cartEmbed)

def save(saveName):
    global currentName
    if saveName is not None:
        currentName = saveName
        with open(f'./saves/{saveName}.items', "wb") as item_file:
            pickle.dump(items, item_file)
        with open(f'./saves/{saveName}.carry', 'wb') as carry_file:
            pickle.dump(carriers, carry_file)
    else:
        with open(f'./saves/{currentName}.items', "wb") as item_file:
            pickle.dump(items, item_file)
        with open(f'./saves/{currentName}.carry', 'wb') as carry_file:
            pickle.dump(carriers, carry_file)

    return(f'Saved cart as {currentName}')

def load(saveName):
    global currentName
    global currentWeight
    global totalCap
    save(currentName)
    currentName = saveName

    with open(f'./saves/{saveName}.items', "rb") as item_file:
        loaditems = pickle.load(item_file)
    for i in loaditems:
        items.append(i)
    with open(f'./saves/{saveName}.carry', "rb") as carry_file:
        loadcarry = pickle.load(carry_file)
    for i in loadcarry:
        carriers.append(i)

    for i in items:
        currentWeight += item.getTotWeight(i)
    for i in carriers:
        totalCap += carrier.getCapacity(i)

def new():
    global items
    global carriers
    global currentWeight
    global totalCap
    global currentName

    items = []
    carriers = []
    currentName = "placeholder"
    currentWeight = 0
    totalCap = 0

def commandParseCart(cmd):
    global cartActive
    parse = cmd.split()
    '''
    handled by DAC
    if 'add' in parse[0]:
        if cartActive:
            if len(parse) != 1:
                print('Incorrect command format. Adding must be \'add\' (name, weight and amount added after you enter the add command)')
            else:
                addWhich()
        else:
            print('No Active Cart')
    '''

    '''
    handled by DAC
    if 'del' in parse[0]:
        if cartActive:
            if len(parse) != 1:
                print('Incorrect command format. del must be \'del\' (item or carrier will be selected after you run del)')
            else:
                delWhich()
        else:
            print('No Active Cart')
    '''

    if 'edit' in parse[0]:
        if cartActive:
            if len(parse) != 1:
                print('Incorrect command format. edit must be \'edit\'')
            else:
                updWhich()
        else:
            print('No Active Cart')

    ''' 
    list is called directly from DAC
    if 'list' in parse[0]:
        if cartActive:
            printItems()
        else:
            print('No Active Cart')
    '''

    if 'save' in parse[0]:
        global currentName
        if cartActive:
            if len(parse) == 2:
                save(parse[1])
            elif len(parse) == 1:
                save(currentName) 
            else:
                print('Incorrect command format. save must be \'save name\' where name is what you want to call the storage system (please have no spaces). To save it as current, leave the name blank or use the exit command and input \'y\'.')
        else:
            print('No Active Cart')

    '''
    load is called directly from DAC
    if 'load' in parse[0]:
        if len(parse) != 2:
            print('Incorrect command format. load must be \'load name\' where name is the storage system you want to load (no spaces).')
        else:
            load(parse[1])
            currentName = parse[1]
            print(f'{currentName} loaded!')
            cartActive = True
    '''
    
    if 'new' in parse[0]:
        global items
        global carriers
        global currentWeight
        global totalCap
        if cartActive:
            save(currentName)
            items = []
            carriers = []
            currentName = "placeholder"
            currentWeight = 0
            totalCap = 0
        else:
            cartActive = True

"""
todo:
- make it so you won't lose changes to a cart when you load a new one
- add help command?
- add GUI?
- add extra RPG tools? (could then call it JERT, Jarvis' Epic RPG Tool)
"""