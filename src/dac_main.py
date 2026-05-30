import discord
import os
import yaml

from roller.roller import commandParseRoller
from cart.cart import new, load, save, addCarry, addItem, delCarry, delItem, printItems
from config.error_handling.getError import getErrMsg, adminError
from datetime import datetime
# from lenny import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

basePath = os.path.dirname(os.path.abspath(__file__))

configDir = os.path.join(basePath, "config")
saveDir = os.path.join(basePath, "saves")

helpfile = os.path.join(configDir, "help.txt")

with open(os.path.join(configDir, "config.yaml"), "r") as config_file:
	config = yaml.safe_load(config_file)
	adminUser = config["instance"]["admin"]
	botToken = config["instance"]["token"]

global LMAO
LMAO = False
global toAnnoy
toAnnoy = 0
global rigDice
rigDice = False


@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
	global LMAO
	global toAnnoy
	global rigDice
	if message.author == client.user:
		return

	if message.content.startswith("DAC-"):
		now = datetime.now()
		now = now.strftime("%d/%m/%Y %H:%M:%S")
		print(
			f"{message.author} requested DAC! Time: {now}, Command: {message.content}"
		)
		mesg = message.content.split(" ")

		match mesg[1]:
			case "roll":
				await message.reply(embed=commandParseRoller(message.content, rigDice))
			case "rigrolls":
				if message.author.id == adminUser:
					if rigDice:
						rigDice = False
					else:
						rigDice = True

			case "help":
				f = open(helpfile, "r")
				await message.channel.send(f.read())
				f.close()

			case "load":
				new()
				load(mesg[2], saveDir)
			case "list":
				await message.reply(embed=printItems())
			case "show":
				listOcarts = ""
				for file in os.listdir(saveDir):
					if ".items" in file:
						strFile = str(file)
						fName = strFile.split(".items")
						listOcarts += f"{fName[0]}\n"
				listOcarts = listOcarts.rstrip("\n")
				listCartEmbed = discord.Embed(
					title="Carts that can be loaded:",
					description=listOcarts,
					color=0x7A306C,
				)
				await message.reply(embed=listCartEmbed)
			case "add":
				match mesg[2]:
					case "item":
						await message.channel.send(addItem(mesg[3], mesg[4], mesg[5]))
					case "carry":
						await message.channel.send(addCarry(mesg[3], mesg[4]))
			case "del":
				match mesg[2]:
					case "item":
						await message.channel.send(delItem(mesg[3]))
					case "carry":
						await message.channel.send(delCarry(mesg[3]))
			case "save":
				await message.channel.send(save(mesg[2], saveDir))

			case "error":
				if message.author.id == adminUser:
					await message.channel.send(adminError(mesg[2]))
					await message.channel.send(
						f"<@{adminUser}> admin, why must you make me error?"
					)

			case "annoy":
				if message.author.id == adminUser:
					toAnnoy = int(mesg[2])
					LMAO = True
				else:
					await message.channel.send(
						f"<@{message.author.id}> sorry bud, but you don't get to do that"
					)
			case "annoyStop":
				if message.author.id == adminUser:
					LMAO = False
				else:
					await message.channel.send(
						f"<@{message.author.id}> sorry bud, but you don't get to do that"
					)
			case "say":
				if message.author.id == adminUser:
					chan = client.get_channel(int(mesg[2]))
					send = ""
					for i in mesg[3:]:
						send += i + " "
					await chan.send(send)
				else:
					await message.channel.send(
						f"<@{message.author.id}> sorry bud, but you don't get to do that"
					)

			case _:
				await message.reply(embed=getErrMsg())

		if LMAO:
			eef = await client.fetch_user(toAnnoy)
			await eef.send("Lmao get DM'd on")


client.run(botToken)

# to run DAC, open windows terminal, type 'd:', then make sure in JERT, then run 'py -3 example_bot.py'
# on UNIX, navigate to the directory this file is in and run 'python3 ./dac_main.py'
