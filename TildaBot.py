import discord, datetime, random, os
from discord.ext.commands import Bot
from datetime import datetime as dt

bot_name = "TildaBot"
client = discord.Client()
bot = Bot(command_prefix="!")
current_time = dt.now().strftime('%H:%M:%S')
current_date = dt.now().strftime('%Y-%m-%d')

token_file = open("user_token.txt")
user_token = token_file.read()
tilda_dev = discord.Object(id="299224095365529600")
tilda_null = discord.Object(id="299225312410075136")
# Tilda-dev 299224095365529600
# Tilda-null 299225312410075136
# Test channel 299220779047059456


# Events

@bot.event  # Boot
async def on_ready():
    print("Online".format(bot_name))
    await bot.send_message(tilda_null,"Up and running")
    #return await bot.say("Up and running!")

# @bot.event  # Reboot command used as event
# async def on_message(message, *args):
#     if str(args) == "()":
#         if message.channel == discord.utils.get(message.server.channels, name="tilda-null"):
#             if message.content.startswith("$reboot"):
#                 #await discord.Client(delete_message(message))
#                 await bot.send_message(tilda_null, "Rebooting...")
#                 print("Rebooting...")
#                 os.system("start reboot.py")
#                 import sys; sys.exit()
#         if message.content.startswith("!hello"):
#             await bot.send_message(tilda_null, "Hello, world!")
#     else:
#         if message.content.startswith("!hello"):
#             await bot.send_message(tilda_null, "Hello, {}!".format(*args))


# Commands

@bot.command()
async def reboot(*args):
    """Reboot the bot"""
    await bot.say("Rebooting...")
    os.system("start reboot.py")
    import sys; sys.exit()

    # Ping
@bot.command()
async def ping(*args):
    """Pong!"""
    return await bot.say("Pong!")

    # Echo
@bot.command()
async def echo(*args):
    """Repeats the text you say"""
    say_this = ""
    for i in args:
        say_this += i + " "
    return await bot.say(say_this)

    # Time and date
@bot.command()
async def time():
    """Current time and date (UTM+2 only atm)"""
    return await bot.say("The time is: {}\nThe date is: {}"\
    .format(current_time,current_date))

    # Roll the dice - Add sides options
@bot.command(description="Use !roll for a single dice and !roll x for more")
async def roll(*args):
    """Roll the dice"""
    rand_numbers = []
    if str(args) == "()":
        rand_numbers.append(random.randint(1,6))
    elif not int(*args) >= 6:
        for i in range(int(*args)):
            rand_numbers.append(random.randint(1,6))
    else:
        for i in range(6):
            rand_numbers.append(random.randint(1,6))
    numbers = "".join(str(rand_numbers))
    return await bot.say("You rolled: {}".format(numbers[1:-1]))

    # Cool
@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

    # You're right
@bot.command()
async def amiright():
    """Check if you're right"""
    return await bot.say("You're totally right.")
    print("amiright")


os.system("cls")
print("Starting")
bot.run(user_token)
#https://discordapp.com/oauth2/authorize?client_id=YOUR_ID_HERE&scope=bot&permissions=0
