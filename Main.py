import discord, json,logging, random, emoji
from discord.ext import commands
from discord import app_commands
from weather import Weather
from rps import rps
from Data import BankData

with open("Api.json", "r") as API:
	APIs=json.load(API)["api"][0]
discordToken=APIs["discordTokenCode"]
with open("Answers.json", "r") as answer:
	answers=json.load(answer)["Answers"]

handler= logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents=discord.Intents.all()

ownerID=834856531693797438

#events

class myBot(commands.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	async def on_ready(self):
		print(f"the bot is online {self.user}")
		try:
			syncing= await self.tree.sync()
			print(f"{len(syncing)} commands have been synced")
		except Exception as e:
			print("the commands didn't synced because\n" + str(e))
			
			
	async def on_message(self, message):
		messages_responses={
			"hi": "Hiiiii",
			"hytale": "F",
			"arthur": "What do you want?",
			"im sad": "https://youtu.be/QuNhTLVgV2Y\n\nCome and let's be sad and cry together ",
			"i'm sad": "https://youtu.be/QuNhTLVgV2Y\n\nCome and let's be sad and cry together",
			"hi comrade": "Hello Comrade",
			"fuck you": "Fuck you you piece of shit",
			}

		content= message.content.lower()
		
		if message.author==self.user or message.author.bot == True:
			return
		elif content in messages_responses:
			await message.reply(messages_responses[content])
			content=content.split()
		elif "technoblade" in content:
			await message.reply("TECHNOBLADE NEVER DIES")
		await self.process_commands(message)
			
	async def on_message_edit(self, before, after):
		if after.author.bot==True:
			return 
		else:
			await after.reply(f"Hey I saw you edit that from \"{before.content}\" to \"{after.content}\" >:)")
			
			
bot= myBot(command_prefix="/", intents=intents)

#button function (will work on it later)




#commands

@bot.tree.command(name="botofanswers", description="Got a question but no answer? Don’t worry Arthur’s here! Ask now and get the answer you need!")
async def botofanswers(interaction: discord.Interaction, question: str):
	await interaction.response.defer()
	the_respond=discord.Embed()
	the_respond.add_field(name=f"{question}", value=random.choice(answers), inline=False)
	await interaction.followup.send(embed=the_respond)
	
	
@bot.tree.command(name="weather", description="Arthur know the weather of every city don't ask why now ask Arthor and he will give it to you")
async def weathercommand(interaction: discord.Interaction, city: str):

	await interaction.response.defer()
	theWeather=Weather(city)
	result=theWeather.weather()
	if result!=False:
		flag=emoji.emojize(f":flag_{result["sys"]["country"].lower()}:")
		the_respond=discord.Embed(title="**Weather**", description=f"Country: {result["sys"]["country"]} {flag}\n\nCity Name: {result["name"]}\n\nWeather: {result["weather"][0]["description"]}\n\nWind Speed: {result["wind"]["speed"]}Km/s\n\nHumidity: {result["main"]["humidity"]}%\n\nTemperature: {int(result["main"]["temp"]-273)}°C")
		await interaction.followup.send(embed=the_respond)
	else:
		await interaction.followup.send(f"{city} is not a City please enter a City name", ephemeral=True)
		
	
@bot.tree.command(name="rps", description="Rock paper scissors a classic game play against Arthur and see your luck")
async def rpscommand(interaction: discord.Interaction, play: str):
	await interaction.response.defer()
	bank_account=BankData(interaction.user.id, interaction.user.name)
	call=rps(play)
	result=call.function()
	if result!= None:
		embed=discord.Embed(title=result[0], description=f"{interaction.user.name.capitalize()}: {result[2]}\nArthur: {result[1]}")
		embed.set_footer(text=f"You got {result[-1]}$")
		bank_account.add_Money(result[-1])
		await interaction.followup.send(embed=embed)
	else:
		await interaction.followup.send("Please enter a valid play (rock, paper, scissors)", ephemeral=True)
		

@bot.tree.command(name="rdice", description="Arthur have a magical dice let's use it!")
async def rdice(interaction: discord.Interaction, min: int=1, max: int=6):
	await interaction.response.defer()
	await interaction.followup.send(f"{random.randint(min, max)} {emoji.emojize(":game_die:")}")
	

@bot.tree.command(name="mba", description="Arthur own's bank account and you can make one for free! How cool is that")
async def bank(interaction: discord.Interaction):
	await interaction.response.defer()
	bank=BankData(interaction.user.id,interaction.user.name)
	await interaction.followup.send(f"{interaction.user.mention} {bank.create_bank()}")
		
				
@bot.tree.command(name="give-money", description="feel generous today? Then give money to people!")
async def givemoney(interaction: discord.Interaction, amount: int, user: discord.User):
	await interaction.response.defer()
	if user.bot==False:
		if interaction.user.id==user.id:
				await interaction.followup.send("You can't give money to yourself ", ephemeral=True)
				return
		call=BankData(user.id, user.name)
		output=call.transfer_Money(amount, interaction.user.id, user.id)
		if output[1] ==0:
			embed=discord.Embed(title=f"{amount}$ transferred", description=output[0])
			await interaction.followup.send(embed=embed)
		elif output[1]>0:
			embed=discord.Embed(title="Something went wrong", description=output[0])
			await interaction.followup.send(embed=embed, ephemeral=True)
		else:
			embed=discord.Embed(title="Something went wrong", description=output[0])
			await interaction.followup.send(embed=embed, ephemeral=True)
			
			
			
@bot.tree.command(name="profile", description="Well it's obvious by the name see your profile")
async def profile(interaction: discord.Interaction,user: discord.User=None):
			await interaction.response.defer()
			if user==None:
				call=BankData(interaction.user.id, interaction.user.name)
				info=call.get_info()
				if info==None:
					call.create_bank()
				embed=discord.Embed(title=f"{interaction.user.name} profile", description=f"Name: {interaction.user.name}\n\nMoney: {info[1]}\n\nID: {interaction.user.id}")
				embed.set_thumbnail(url=interaction.user.avatar)
				await interaction.followup.send(embed=embed)
			else:
				if user.bot !=True:
					call=BankData(user.id, user.name)
					info=call.get_info()
					if info==None:
						call.create_bank()
						info=call.get_info()
					embed=discord.Embed(title=f"{user.name} profile", description=f"Name: {user.name}\n\nMoney: {info[1]}\n\nID: {user.id}")
					embed.set_thumbnail(url=user.avatar)
					await interaction.followup.send(embed=embed)
				else:
					await interaction.response.send("You can't check bot profile", ephemeral=True)
				
@bot.tree.command(name="log", description="log")
async def log(interaction: discord.Interaction, user: discord.User):
	await interaction.response.send_message(f"{interaction}\n\n{user.bot}")


bot.run(discordToken)