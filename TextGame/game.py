import discord
import re
import asyncio
import player

def read_token(): # place server token in token.txt for privacy
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

token = read_token()

client = discord.Client()
newplayer = player.Player()

urlF =  r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

@client.event
async def on_message(message):
    id = client.get_guild(723641747896270928) # server id goes here
    if str(message.channel):
        if message.content.find("!play") != -1:
            await message.channel.send("Welcome Hunter {0.author.mention}".format(message))
        elif message.content.find("!stats") != -1:
            await message.channel.send("Your stats are" + newplayer.stats )





client.run(token)
