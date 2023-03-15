#this bot is creates a Temporary voice channel whenever someone joins in a voice channel 

import discord
from discord_components import DiscordComponents, ComponentsBot, Button
from discord.ext import commands
import discord.utils
from discord import ChannelType

stk=[] #for renaming the temporary voice channels only

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None:
        old= 963085107718156368,963085251519844412,963085150445527063,963084331713171466,880117143318966315   #id of the voice channels 
        if after.channel.id in old:
            for guild in client.guilds:
                category = after.channel.category #category id
                #for naming of channels
                p=0
                s=0
                g=0
                n=0
                sp=(c.name for c in guild.channels if c.type==ChannelType.voice)
                for i in sp:
                    if 'speaking pair' in i:
                        p+=1
                    elif 'speaking group' in i:
                        g+=1
                    elif 'speaking squad' in i:
                        s+=1
                    elif 'reading' in i:
                        n+=1
                if after.channel.name == 'speaking group':    #group/squad/pair refers to the number of users in a voice channel
                    n=g
                elif after.channel.name =='speaking pair':
                    n=p
                elif after.channel.name == 'speaking squad':
                    n=s
                channel2 = await guild.create_voice_channel(name=f'{after.channel.name} # {n}', category=category,user_limit=after.channel.user_limit)
                await channel2.set_permissions(member, connect=True, mute_members=True, manage_channels=True)
                await member.move_to(channel2)
                stk.append(channel2)
                def check(x, y, z):
                    return len(channel2.members) == 0
                await client.wait_for('voice_state_update', check=check)
                await channel2.delete()
                stk.remove(channel2)    #after everyone leaves the channel is deleted
#channel renaming 
@client.command()
async def rn(ctx, *, new_name):   #renameing of the voice channel
    channel1=ctx.author.voice.channel
    if channel1 in stk:
        await channel1.edit(name=new_name)
