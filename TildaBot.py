import discord, datetime, random
from discord.ext.commands import Bot
from datetime import datetime as dt

bot = Bot(command_prefix="!")
current_time = dt.now().strftime('%H:%M:%S')
current_date = dt.now().strftime('%Y-%m-%d')

token_file = open("user_token.txt")
user_token = token_file.read()


#   Events
@bot.event
async def on_ready():
    print("[x] Online")


# Commands

    # Hello world
@bot.command()
async def hello(*args):
    if str(args) == "()":
        return await bot.say("Hello, world!")
    else:
        return await bot.say("Hello, {}!".format(*args))

    # Time and date
@bot.command()
async def time():
    return await bot.say("The time is: {}\nThe date is: {}"\
    .format(current_time,current_date))

    # Echo
@bot.command()
async def echo(*args):
    say_this = ""
    for i in args:
        say_this += i + " "
    return await bot.say(say_this)

    # Roll the dice
@bot.command()
async def roll(*args):
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

    # You're right
@bot.command()
async def amiright():
    return await bot.say("You're totally right.")

    # r6 eric: I would rather poop in my hands and clap than have AMD
    # INTEL FTW
@bot.command()
async def poopandclap():
    return await bot.say(":poop: :clap:")


print("[ ] Running")
bot.run(user_token)
#https://discordapp.com/oauth2/authorize?client_id=YOUR_ID_HERE&scope=bot&permissions=0
