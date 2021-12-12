import random
import discord
import time
#there you can insert your discord token
token = ("INSERT YOUR DISCORD TOKEN")
#this is the prnt.sc url that we use to create full link
prnt_sc = ("https://prnt.sc/")
#protocol
def abc():
	a =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" "1","2","3","4","5","6","7","8","9"]
	b =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" "1","2","3","4","5","6","7","8","9"]
	c =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" "1","2","3","4","5","6","7","8","9"]
	d =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" "1","2","3","4","5","6","7","8","9"]
	e =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" "1","2","3","4","5","6","7","8","9"]
	f =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" "1","2","3","4","5","6","7","8","9"]
	#discord part
	client = discord.Client()
	@client.event
	async def on_ready():
		print ("We are allready logged in as {0.user}".format(client))
	@client.event
	async def on_message(message):
		if message.author == client.user:
			return
		if message.content.startswith("&help"):
			await message.channel.send("""` &help ` - show help
` !prntsc ` - show random print screen
|| Bot CREATED BY Perchant#2178 ||
    	    """)
		if message.content.startswith("&prntsc"):
			await message.channel.send(prnt_sc+random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d)+random.choice(e)+random.choice(f))
	client.run(token)
for i in range(9999999999999999999999999):
	abc()
	time.sleep(1)