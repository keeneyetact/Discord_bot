# This bot is used to message in specific channel, and the bots message always at last , it used to ensure members that the channel is used correctly

import discord
from discord_components import DiscordComponents, ComponentsBot, Button
from discord.ext import commands as commands

client = commands.Bot("IB!")
token = TOKEN
DiscordComponents(client)


@client.event
async def on_ready():
    print("Bot Ready")

@client.event
async def on_message(message):
    if message.channel.name == 'session-planning':    #channels name in which the bot should message 
        if message.author==client.user :
            return
        else:
            if len(await message.channel.purge(limit=5, check=lambda x: (x.author==client.user))) > 0:    #checks the last 5 messages if the bot has messaged yet if yes its delete that message and sends again
                await message.channel.send('its me again in bot testing')
        
    elif  message.channel.name == 'tech-department':
        if message.author==client.user :
            return
        else:
            if len(await message.channel.purge(limit=5, check=lambda x: (x.author==client.user))) > 0:
                await message.channel.send('its me again in techdepartment')
                
           
    else:
        return

client.run(token)
