import random
import discord
import time
from discord import channel

# there you can insert your discord token
token = ("OTE5MzUxMjQ4OTkyNTAxNzgw.YbUikg.wAD9a5PXq4PcAXoh1SK8tGInawk")
# this is the prnt.sc url that we use to create full link
prnt_sc = ("https://prnt.sc/")
# protocol
# protocol
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
     "r", "s", "t", "u", "v", "w", "x", "y", "z" "1", "2", "3", "4", "5", "6", "7", "8", "9"]
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
     "r", "s", "t", "u", "v", "w", "x", "y", "z" "1", "2", "3", "4", "5", "6", "7", "8", "9"]
c = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
     "r", "s", "t", "u", "v", "w", "x", "y", "z" "1", "2", "3", "4", "5", "6", "7", "8", "9"]
d = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
     "r", "s", "t", "u", "v", "w", "x", "y", "z" "1", "2", "3", "4", "5", "6", "7", "8", "9"]
e = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
     "r", "s", "t", "u", "v", "w", "x", "y", "z" "1", "2", "3", "4", "5", "6", "7", "8", "9"]
f = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
     "r", "s", "t", "u", "v", "w", "x", "y", "z" "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# discord
client = discord.Client()


@client.event
async def on_ready():
    print("We are allready logged in as: {0.user}".format(client))


def mejn():
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith("&help"):
            await message.channel.send("""
    `&help` - show help
    ```&prntsc1 - shows 1 random print screen
    &prntsc10 - shows 10 random print screens
    &prntsc3 - shows 100 random print screens
    &prntsc4 - shows 1000 random print screens
    &prntsc5 - shows 10000 random print screens```
    ||Bot created by Ccondir#0556 and Perchant#2178||
            """)
        if message.content.startswith("&prntsc"):
            await message.channel.send("**sendin 1 prntsc**")
            await message.channel.send("https://prnt.sc/"+random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d)+random.choice(e)+random.choice(f))
            await message.channel.send("**done**")
        if message.content.startswith("&prntsc10"):
            await message.channle.send("**sendin 10 prtscs**")
            for i in range(10):
                await message.channel.send("https://prnt.sc/"+random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d)+random.choice(e)+random.choice(f))
                time.sleep(1)
            await message.channel.send("**done**")
        if message.content.startswith("&prntsc100"):
            await message.channel.send("**sendin 100 prtscs**")
            for i in range(100):
                await message.channel.send("https://prnt.sc/"+random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d)+random.choice(e)+random.choice(f))
                time.sleep(1)
            await message.channel.send("**done**")
        if message.content.startswith("&prntsc1000"):
            await message.channel.send("**sendin 1000 prtscs**")
            for i in range(1000):
                await message.channel.send("https://prnt.sc/"+random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d)+random.choice(e)+random.choice(f))
                time.sleep(1)
            await message.channel.send("**done**")
        if message.content.startswith("&prntsc10000"):
            await message.channel.send("**sendin 10000 prtscs**")
            for i in range(10000):
                await message.channel.send("https://prnt.sc/"+random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d)+random.choice(e)+random.choice(f))
                time.sleep(1)
            await message.channel.send("**done**")
    client.run(token)


for i in range(999999):
    mejn()
    time.sleep(1)
