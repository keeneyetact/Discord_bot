#this bot is used to give roles if the user clicks on the button

#imports
import discord
from discord_components import DiscordComponents, ComponentsBot, Button
from discord.ext import commands as commands


client = commands.Bot("IB!")   #command to start the bot
token = TOKEN   # bots Token
DiscordComponents(client)

#id for the roles which need to be added
Academic = 913403093914353671
General = 913403093914353670
NTI = 913403093914353667
Alreadydone = 913403093914353668
Lifeskills = 913403093914353669
speakingp = 913403093914353666
readingp = 913403093914353664
listeningp = 913403093897580563
writingp = 913403093914353665

#when bot is ready it prints the message
@client.event
async def on_ready():
    print("Bot Ready")
    
 #to start the command
@client.command()
async def roles(ctx):
    member = ctx.message.author
    await ctx.send("Grab your roles", components = [
        [Button(label="Academic", style="3", custom_id="academic"),Button(label="General", style="3", custom_id="General"),Button(label="Life Skills", style="3", custom_id="lifeskills"),
        Button(label="Already Done", style="3", custom_id="alreadydone")]])
@client.event
async def on_button_click(interaction):    
    if interaction.component.label == "Academic":
        role = discord.utils.get(client.get_guild(interaction.guild.id).roles, id=Academic)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
        else:
            await interaction.user.add_roles(role)
        await interaction.respond(content=f'{interaction.user}Academic')
    elif interaction.component.label =="General":
        role = discord.utils.get(client.get_guild(interaction.guild.id).roles, id=General)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
        else:
            await interaction.user.add_roles(role)
        await interaction.respond(content='General')
    elif interaction.component.label =="Life Skills":
        role = discord.utils.get(client.get_guild(interaction.guild.id).roles, id=Lifeskills)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
        else:
            await interaction.user.add_roles(role)
        await interaction.respond(content='Life Skills')
    elif interaction.component.label =="Already Done":
        role = discord.utils.get(client.get_guild(interaction.guild.id).roles, id=Alreadydone)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
        else:
            await interaction.user.add_roles(role)
        await interaction.respond(content='Already Done')

client.run(token)
