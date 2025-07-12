import discord, json,logging, os, random, emoji
from discord.ext import commands
from discord import app_commands
from weather import Weather
from rps import rps

with open("Api.json", "r") as API:
	APIs=json.load(API)["api"][0]
discordToken=APIs["discordTokenCode"]
with open("Answers.json", "r") as answer:
	answers=json.load(answer)["Answers"]

handler= logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents=discord.Intents.all()

pending_requests={}

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
		content= message.content.lower()
		
		if message.author==self.user or message.author.bot == True:
			return
			
		elif content == "hi" :
			await message.reply("HIIIIII")
			
		elif content == "hytale":
			await message.reply("F")
			
		elif "technoblade" in message.content.lower():
			await message.reply("TECHNOBLADE NEVER DIE")
			
		elif content=="hi comrade":
			await message.reply("Hello Comrade")
			
		elif content=="im sad" or content=="i'm sad":
			await message.reply("https://youtu.be/QuNhTLVgV2Y\n\nAfter you listen to this song go and kill yourself")
			
		elif content=="fuck you":
			await message.reply("Fuck you you piece of shit")
			
			await self.process_commands(message)
			
	async def on_message_edit(self, before, after):
		if after.author.bot==True:
			return 
		else:
			await after.reply(f"hey I saw you edit that from \"{before.content}\" to \"{after.content}\" >:)")
			
			
bot= myBot(command_prefix="/", intents=intents)

#button function




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
	
	call=rps(play)
	result=call.function()
	if result!= None:
		embed=discord.Embed(title=result[0], description=f"{interaction.user.name.capitalize()}: {result[2]}\nArthur: {result[1]}")
		await interaction.followup.send(embed=embed)
	else:
		await interaction.followup.send("Please enter a valid play (rock, paper, scissors)", ephemeral=True)

#@bot.tree.command(name="log", description="log")
#async def log(interaction: discord.Interaction):
#	await interaction.response.send_message(interaction)


bot.run(discordToken)