#this bot is creates a Temporary voice channel whenever someone joins in a voice channel 

import discord
from discord_components import DiscordComponents, ComponentsBot, Button
from discord.ext import commands
import discord.utils
from discord import ChannelType

stk=[] #for renaming the temporary voice channels only

Token=TOKEN

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None:
        old= 963085107718157368,963085251519847412,963085155245527063,963084331713171466,880667143318966315     #voice channels id
        if after.channel.id in old:
            for guild in client.guilds:
                category = after.channel.category #category id
                #for naming of channels
                p=0
                s=0
                g=0
                n=0
                sp=(c.name for c in category.voice_channels if c.type==ChannelType.voice)
                for i in sp:
                    if 'speakingpair' in i.replace(" ","").lower():
                        p+=1
                    elif 'speakinggroup' in i.replace(" ","").lower():
                        g+=1
                    elif 'speakingsquad' in i.replace(" ","").lower():
                        s+=1
                    elif 'reading' in i.replace(" ","").lower():
                        n+=1
                    elif 'writing' in i.replace(" ","").lower():
                        n+=1
                    elif 'listening' in i.replace(" ","").lower():
                        n+=1
                    else:
                        n=123
                        print(i)
                a=after.channel.name
                if 'speakinggroup' in a.replace(" ","").lower():
                    n=g
                elif 'speakingpair' in a.replace(" ","").lower():
                    n=p
                elif 'speakingsquad' in a.replace(" ","").lower()':
                    n=s
                channel2 = await guild.create_voice_channel(name=f'{after.channel.name} # {n}', category=category,user_limit=after.channel.user_limit)
                await channel2.set_permissions(member, connect=True, mute_members=True, manage_channels=True)
                await member.move_to(channel2)
                stk.append(channel2)
                def check(x, y, z):
                    return len(channel2.members) == 0
                await client.wait_for('voice_state_update', check=check)
                await channel2.delete()
                stk.remove(channel2)
#channel renaming 
@client.command()
async def rn(ctx, *, new_name):
    channel1=ctx.author.voice.channel
    if channel1 in stk:
        await channel1.edit(name=new_name)
        
client.run(token)
