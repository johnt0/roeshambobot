import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
TOKEN = 'tokencharacters'
@client.event
async def on_ready():
    print('Bot is ready')
    
@client.command()
async def shoot(ctx, *, shoot):
    options = ['rock','paper','scissors']
    if(shoot.lower() not in options):
        await ctx.send("Invalid option")
        return
    random_pick = ''.join(random.choices(options))
    await ctx.send(random_pick)
    if(random_pick == 'rock' and shoot.lower() == 'scissors'):
        await ctx.send("I win!")
    elif(random_pick == 'paper' and shoot.lower() == 'rock'):
        await ctx.send("I win!")
    elif(random_pick == 'scissors' and shoot.lower() == 'paper'):
        await ctx.send("I win!")
    elif(random_pick == shoot.lower()):
        await ctx.send("It's a tie!")
    else:
        await ctx.send("I lose :(")
    
client.run(TOKEN)
