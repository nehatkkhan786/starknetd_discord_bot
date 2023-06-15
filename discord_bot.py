import discord
from discord.ext import commands
from system_function import get_service_status


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix = '@', intents=intents)
token = 'Your Token'

global_service = "starknetd"
@bot.command()
async def get_status(ctx, type):
    try:
        if type == 'status':
            response = get_service_status(global_service)
            await ctx.send(response)
        else:
            await ctx.send("This comand is not supported!")
    except:
        await ctx.send("Something went wrong!")
        
bot.run(token)
