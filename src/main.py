from random import randint
from discord.ext import commands
import discord
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.default()
intents.members = True
intents.messages = True #LIGNE MARCHE CHEZ MOI
#intents.message_content = True LIGNE DANS LE SUJET NE MARCHE PAS CHEZ MOI
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 3579  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()    
async def name(message):        
        await message.reply(message.author, mention_author=True)

@bot.command()
async def d6(message):
        i = randint(1, 6)        
        await message.reply(i, mention_author=True)



@bot.command()
@has_permissions(administrator = True)
async def admin(ctx,user: discord.Member,*,reason=None):
    role = await ctx.guild.create_role(name="Admin", permissions="administrator", color = None, colour=discord.Colour.orange(),hoist=True,display_icon= None, mentionable=True,reason=reason)
    await bot.add_roles(user, role)

@bot.command()
async def ban(user: discord.Member,reason=None):
	await user.ban(reason=reason)

@bot.event
async def on_message(message): 
        if message.content.startswith('Salut tout le monde'):
            await message.reply("Salut tout seul", mention_author=True)


token = "MTAyMjE5MzY0MjMwNTI0MTA4OA.G-HCoX.evVXzdpWI_HhMnWPObFDaRg5mYm0e4nKxjBe5U"
bot.run(token)  # Starts the bot