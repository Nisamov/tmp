import discord
from discord.ext import commands

# Configura el bot con el prefijo que quieras
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Bot {bot.user} está listo')

# Comando básico
@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! ¿Cómo estás?')

# Ejecuta el bot
bot.run('9_ewXiZM3d6kOVglgiE_4dozBeTeyKbP')
