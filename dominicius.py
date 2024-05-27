#'||''|.                       ||            ||           ||                  
# ||   ||    ...   .. .. ..   ...  .. ...   ...    ....  ...  ... ...   ....  
# ||    || .|  '|.  || || ||   ||   ||  ||   ||  .|   ''  ||   ||  ||  ||. '  
# ||    || ||   ||  || || ||   ||   ||  ||   ||  ||       ||   ||  ||  . '|.. 
#.||...|'   '|..|' .|| || ||. .||. .||. ||. .||.  '|...' .||.  '|..'|. |'..|'

# Bot creado por Nisamov#0001
# Más información en: https://acortar.link/dominicius

# Recomendable leer el README.txt para poder iniciar el bot (usado unicmanete cuando se pasa de un S.O a otro)

# Sección 1 - Dependencias

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
#from discord_slash import SlashCommand     #Los slash commands no funcionan, dejar comentada la sección es lo más adecuado
#from discord_slash import SlashContext
import datetime
from discord import File
import random
import subprocess
from discord import Embed
import asyncio
import time
import requests

load_dotenv()
# De aqui saca el toquen y el ID
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)
intents.message_content = True

# ID del propietario del bot
OWNER_ID = 674968262093570048

#slash = SlashCommand(bot, sync_commands=True)      #Shash command, no funciona

# Envio de log de inicio de sesion
@bot.event
async def on_ready():
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    change_status.start()
    global start_time
    start_time = datetime.datetime.now()
    # Obtén el servidor y el canal específicos
    guild = bot.get_guild(1161488389598613544)  # Reemplaza con el ID de tu servidor
    channel = guild.get_channel(1164101838090543124)  # Reemplaza con el ID de tu canal
    if channel:
        message = f"""
```
**Registro de Inicio del Bot**

- Bot: {bot.user.name}
- ID del Bot: {bot.user.id}
- Prefix: {bot.command_prefix}
- Fecha y hora de inicio: {bot.user.created_at}
- Servidor: {guild.name}
- ID del Servidor: {guild.id}

Bot conectado con éxito a Discord.
```
"""

        await channel.send(message)

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

status_options = ['Legio Aeterna Victrix', 'Nisamov est Aeternum', 'Aeterna Solitudo', '/aeterna', 'VisioNex Wave']
current_status = 0

@tasks.loop(seconds=10)
async def change_status():
    global current_status
    server_count = len(bot.guilds)
    
    if current_status == 0:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{server_count} servers'))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_options[current_status - 1]))

    current_status = (current_status + 1) % (len(status_options) + 1)

# Fin Sección 1- Fin Dependencias

# Nuevos usuarios
@bot.event
async def on_member_join(member):
    # Mensaje de bienvenida para los nuevos miembros
    channel = member.guild.system_channel  # Cambiar esto por el canal de bienvenida de tu servidor solo si es necesario (actualmente no lo es)
    if channel:
        embed = discord.Embed(
            title=f"¡Bienvenido a {member.guild.name}!",
            description=f"Bienvenido, {member.mention}, al servidor {member.guild.name}. Esperamos que te diviertas aquí.",
            color=0x43465
        )
        await channel.send(embed=embed)

@bot.command(name='aeshowtimeonplay')
async def show_time_on_play(ctx):
    current_time = datetime.datetime.now()
    
    if start_time is not None:
        uptime = current_time - start_time
        uptime_str = str(uptime)
        await ctx.send(f"El bot ha estado conectado durante: {uptime_str}")
    else:
        await ctx.send("El bot no ha sido inicializado correctamente. Inténtalo de nuevo más tarde.")

# Mostrar versiones del bot
@bot.command(name='ae', help='Muestra información sobre el Bot')
async def show_aeterna_commands(ctx):
    embed_data = {
        "title": "Soporte",
        "description": "Para comenzar con Dominicius, prueba a usar el comando `/aeterna`",
        "color": 43465,
        "fields": [
            {
                "name": "Información:",
                "value": "Dominicius es un Bot que permite a los usuarios gestionar roles y miembros, este Bot está pensado para la moderación y uso personal del creador `Nisamov#001`, su uso es libre y está en constantes mejoras.",
                "inline": False
            },
            {
                "name": "Mas información:",
                "value": "El Bot utiliza una serie de funciones que permiten al usuario saber más a cerca de las novedades: `/aeversions`.\nCualquier fallo que el Bot pueda tener, pueden reportarlo en el [Servidor de Soporte](https://discord.gg/7hRZ43mtwD).\nMuchas gracias por usar el Bot.",
                "inline": False
            }
        ]
    }

    embeds = [embed_data]

    for data in embeds:
        embed = discord.Embed(
            title=data["title"],
            description=data["description"],
            color=data["color"]
        )
        for field in data["fields"]:
            embed.add_field(name=field["name"], value=field["value"], inline=field["inline"])
        
        # Añadir un footer al embed
        embed.set_footer(text="Creador: Nisamov#0001", icon_url="https://lh3.googleusercontent.com/a/ACg8ocK-Wl0EKh8SCYxtl4laV1kRVMafkN_27UEpsNuda1NyjvAv=s83-c-mo")

        await ctx.send(embed=embed)

#Comando /aehelp
    # No current data

#Comando /aeterna
@bot.command(name='aeterna', help='Muestra la lista de comandos de Dominicius')
async def show_aeterna_commands(ctx):
    embed_data = {
        "title": "Comandos de Dominicius",
        "description": "Estos comandos proporcionan diferentes funciones según el status del Bot con el que estás interactuando, actualmente estás interactuando con **Dominicius**, cuyo rango es XI, al interactuar con Bots de mayor o menor rango, obtendrás funciones diferentes.\n\nCada Bot que sea parte del imperio | [Hantla](https://discord.gg/7hRZ43mtwD) | tendrá una especialización, por ello cada Bot podrá hacer tareas diferentes.\n\nPuedes [invitar a Dominicius](https://discord.com/oauth2/authorize?client_id=1108667860454215690&scope=bot&permissions=8) o probar las funciones de sus compañeros para ver cual es el que más te aporta más cosas.",
        "color": 43465,
        "fields": [
            {
                "name": "Comandos que puedes ejecutar:",
                "value": "/ae\n/aeterna\n/aedata\n/aeinfo\n/aebotinvite\n/aesrvinvite\n/aebotavatar\n/aeshowavatar\n/aeping\n/aeversions\n/aebotpronoun\n/aereport (motivo)\n/aeshowtimeonplay\n/aevote",
                "inline": True
            },
            {
                "name": "Descripción del comando:",
                "value": "Muestra como iniciar con el Bot\nMuestra la lista de comandos\nMuestra información del servidor\nMuestra información del bot\nGenera una invitación (Bot)\nGenera una invitación temporal (Srv)\nEnvia el actual avatar del Bot\nMuestra el avatar del usuario seleccionado\nObten el Ping del Bot\nMuestra información sobre las versiones\nMuestra el pronombre actual del bot\nReporta insjusticias\nTiempo que ha estado conectado el Bot\nVota al Bot en Top.gg",
                "inline": True
            }
        ]
    }

    admin_embed_data = {
        "title": "Comandos Administrador",
        "description": "Estos comandos son únicos para los moderadores y administradores del servidor, para poder ejecutarlos, es necesario contar con los permisos de administrador.\n\nEs necesario que el Bot también cuente con todos los permisos, si tienes problemas, puedes mirar la [pagina de soporte de Discord](https://support.discord.com/hc/es/articles/206029707--Cómo-configurar-Permisos-).",
        "color": 43465,
        "fields": [
            {
                "name": "Comandos de Administrador:",
                "value": "/aekick {@member} {Reason}\n/aeban {@member}\n/aemute {@member}\n/aepurge {X}\n/aeasignrol {@member} {@Rol}\n/aeremoverol {@member} {@Rol}\n/aecreaterol\n/aesetbotpronoun\n/aeremovepronoun\n",
                "inline": True
            },
            {
                "name": "Descripción del comando:",
                "value": "Expulsa al miembro de la comunidad\nBanea el miembro de la comunidad\nMutea (Silencia) en los canales de voz\nElimina los últimos X mensajes enviados\nAsigna un Rol a los miembros\nElimina un rol a los miembros\nCrea un rol nuevo\nEstablece el pronombre del Bot\nElimina el pronombre actual\n",
                "inline": True
            }
        ]
    }

    server_owner_embed_data = {
        "title": "Comandos Propietario del Servidor",
        "description": "Estos comandos están reservados únicamente al propietario del servidor, serán recibidos en el [Servidor Oficial del Bot](https://discord.gg/7hRZ43mtwD).",
        "color": 43465,
        "fields": [
            {
                "name": "Comandos Propietario del Servidor:",
                "value": "/aeowneradvise {mensaje}",
                "inline": True
            },
            {
                "name": "Descripción del comando:",
                "value": "Enviar mensaje a los gestores del Bot",
                "inline": True
            }
        ]
    }

    owner_embed_data = {
        "title": "Comandos Propietario",
        "description": "Estos comandos están reservados al dueño del Bot, con ellos, se pueden gestionar ciertas características del Bot.",
        "color": 43465,
        "fields": [
            {
                "name": "Comandos Propietario:",
                "value": "/aebotavatar\n/aebirthday\n/aestop\n/aesendtoall\n/aewarn (aviso)",
                "inline": True
            },
            {
                "name": "Descripción del comando:",
                "value": "Establece el icono del Bot\nEnvía un mensaje de felicitación al creador\nDetener el Bot\nEnviar un mensaje a todos los servidores\nAvisa a los miembros de algo",
                "inline": True
            }
        ]
    }

    embeds = [embed_data, admin_embed_data, server_owner_embed_data, owner_embed_data]

    for data in embeds:
        embed = discord.Embed(
            title=data["title"],
            description=data["description"],
            color=data["color"]
        )
        for field in data["fields"]:
            embed.add_field(name=field["name"], value=field["value"], inline=field["inline"])
        await ctx.send(embed=embed)


# Mostrar versiones del bot
@bot.command(name='aeversions', help='Muestra la lista de versiones del Bot')
async def show_aeterna_commands(ctx):
    embed_data = {
        "title": "Lista de Versiones",
        "description": "Este es un resumen general de la versión actual del Bot.",
        "color": 43465,
        "fields": [
            {
                "name": "Versiones:",
                "value": "v0.2.1\nv0.2.0\nv0.1.3\nv0.1.2\nv0.1.1\nv0.1.0\nv0.0.1",
                "inline": True
            },
            {
                "name": "Descripción de la versión:",
                "value": "Versión Actual\nAumento de comandos de adminsitrador\nMejora en funciones y embeds\nEnriquecimiento de funciones\nPrimera Función\nVersión de inicio\nVersión prinicpal",
                "inline": True
            }
        ]
    }

    embeds = [embed_data]

    for data in embeds:
        embed = discord.Embed(
            title=data["title"],
            description=data["description"],
            color=data["color"]
        )
        for field in data["fields"]:
            embed.add_field(name=field["name"], value=field["value"], inline=field["inline"])
        await ctx.send(embed=embed)

# IMostrar información de cada versión
@bot.command(name='aeshowversion_0.0.1', help='Muestra información sobre la versión 0.0.1')
async def show_aeterna_commands(ctx):
    embed_data = {
        "title": "V.0.0.1",
        "description": "Información de la versión 0.0.1",
        "color": 43465,
        "fields": [
            {
                "name": "A Cerca De:",
                "value": "Esta versión se basa en la creación de un Bot sencillo cuya única función es mantenerse activo, no cuenta con funciones complejas, solamente lo necesario para que el Bot se mantuviera activo hasta que se paraba la ejecución.",
                "inline": False
            }
        ]
    }
    embeds = [embed_data]

    for data in embeds:
        embed = discord.Embed(
            title=data["title"],
            description=data["description"],
            color=data["color"]
        )
        for field in data["fields"]:
            embed.add_field(name=field["name"], value=field["value"], inline=field["inline"])
        await ctx.send(embed=embed)


#Vota al Bot
@bot.command(name="aevote")
async def aevote(ctx):
    # URL de redirección a la página de votación
    vota_url = "https://top.gg/bot/1108667860454215690/vote"
    # Envía el enlace de redirección como respuesta
    await ctx.send(f"Apoya al Bot votando por el: {vota_url}")

# Diccionario para almacenar los pronombres por servidor
server_pronouns = {}
# Establecer pronombre bot
@bot.command()
@commands.has_permissions(administrator=True)
async def aesetbotpronoun(ctx, *, pronoun_str):
    server_id = ctx.guild.id
    pronoun_str = pronoun_str.lower()  # Convierte los pronombres a minúsculas
    server_pronouns[server_id] = pronoun_str
    await ctx.send(f'Se ha establecido el pronombre del bot para este servidor como "{pronoun_str}".')

# Comando para ver el pronombre del bot en el servidor
@bot.command()
async def aebotpronoun(ctx):
    server_id = ctx.guild.id
    if server_id in server_pronouns:
        pronoun_str = server_pronouns[server_id]
        await ctx.send(f'El pronombre del bot en este servidor es: "{pronoun_str}".')
    else:
        await ctx.send('El pronombre del bot en este servidor no se ha establecido.')

# Comando para eliminar el pronombre del  Bot en el servidor
@commands.has_permissions(administrator=True)
async def aeremovepronoun(ctx):
    guild = ctx.guild

    if 'pronombre' in server_pronouns.get(guild.id, {}):
        del server_pronouns[guild.id]['pronombre']

        await ctx.send('Se ha eliminado el pronombre personalizado del servidor.')
    else:
        await ctx.send('El servidor no tiene un pronombre personalizado configurado.')

# Comando Ping

@bot.command(name='aeping', help='Obtiene el ping del bot')
async def ping(ctx):
    # Obtiene el tiempo de latencia (ping) del bot
    latency = round(bot.latency * 1000)  # Convierte a milisegundos

    await ctx.send(f'Ping: {latency}ms')

@bot.command(name='aebotinvite', help='Genera un enlace de invitación del bot')
async def generate_bot_invite(ctx):
    bot_invite_url = f'https://discord.com/oauth2/authorize?client_id=1108667860454215690&scope=bot&permissions=8'
    embed = discord.Embed(
        title='Invitación del Bot',
        description='¡Aquí tienes un enlace de invitación para añadir a Dominicius a tu servidor!',
        color=discord.Color.purple()
    )
    embed.add_field(name='Enlace de Invitación', value=bot_invite_url, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='aesrvinvite', help='Crea una invitación temporal del servidor')
async def create_server_invite(ctx):
    # Obtiene el canal desde el que se solicitó el comando
    channel = ctx.channel

    # Crea una invitación temporal con una duración de 1 día (86400 segundos)
    invite = await channel.create_invite(max_age=86400, max_uses=1)

    # Envía la invitación al mismo canal desde el que se solicitó el comando
    await ctx.send(f"Aquí tienes una invitación temporal del servidor: {invite.url}")


@bot.command(name='aedata', help='Muestra información del servidor')
async def show_server_info(ctx):
    server = ctx.guild
    member_count = len(server.members)
    bot_count = len([member for member in server.members if member.bot])
    role_count = len(server.roles)
    embed = discord.Embed(
        title='Información del Servidor',
        description=f'Servidor: {server.name}\n'
                    f'Fecha de Creación: {server.created_at}\n'
                    f'Miembros: {member_count}\n'
                    f'Bots: {bot_count}\n'
                    f'Roles: {role_count}',
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

@bot.command(name='aeinfo', help='Muestra información del bot')
async def show_bot_info(ctx):
    bot_user = bot.user
    embed = discord.Embed(
        title='Información del Bot',
        description=f'Nombre: {bot_user.name}\n'
                    f'ID: {bot_user.id}\n'
                    f'Fecha de Creación: {bot_user.created_at}\n'
                    f'Creador: Nisamov#001',
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

# Mostrar avatar de usuarios o a si mismo
@bot.command()
async def aeshowavatar(ctx, user: discord.Member = None):
    # Si no se especifica un usuario, usa el autor del mensaje
    if user is None:
        user = ctx.author

    # Obtiene el avatar del usuario
    user_avatar_url = user.avatar.url

    # Crea un embed con la imagen del avatar
    embed = discord.Embed(title=f"{user.name}'s Avatar", color=0x00ff00)
    embed.set_image(url=user_avatar_url)

    # Envía el embed al canal donde se ejecutó el comando
    await ctx.send(embed=embed)

@bot.command(name='aebirthday', help='Muestra el mensaje de cumpleaños del creador')
async def show_birthday_message(ctx):
    global last_birthday_date
    if ctx.author.id == 674968262093570048:
        # Verificar si es el 7 de marzo y si ha pasado un año desde el último cumpleaños (Mi cumpleaños)
        today = datetime.date.today()
        if today.month == 3 and today.day == 7 and (last_birthday_date is None or today.year > last_birthday_date.year):
            # Actualizar la fecha del último cumpleaños
            last_birthday_date = today
            # Obtener el canal de cumpleaños
            for guild in bot.guilds:
                general_channel = discord.utils.get(guild.text_channels, name='general')
                if general_channel:
                    # Enviar el mensaje de cumpleaños en el canal general
                    embed = discord.Embed(
                        title='¡Feliz Cumpleaños!',
                        description='Hoy es el cumpleaños de <@674968262093570048> (el creador del bot). ¡Deseémosle un feliz cumpleaños!',
                        color=discord.Color.gold()
                    )
                    # Agregar imagen y GIF de cumpleaños
                    embed.set_thumbnail(url='https://i.pinimg.com/originals/0e/e6/ff/0ee6ffa92db793b46a7e694b3ddb918a.gif')
                    embed.set_image(url='https://st2.depositphotos.com/1010735/10659/v/450/depositphotos_106596574-stock-illustration-happy-birthday-paper-card.jpg')
                    await general_channel.send(embed=embed)
                    break
        else:
            await ctx.send('Hoy no es el 7 de marzo o ya se envió el mensaje de cumpleaños este año.')
    else:
        await ctx.send('No tienes permiso para ejecutar este comando.')

# Inicializar la fecha del último cumpleaños
last_birthday_date = None

@bot.command(name='aekick', help='Expulsa a un miembro del servidor')
async def kick_member(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("No has mencionado a ningún miembro para expulsar.")
    else:
        await member.kick()
        await ctx.send(f"{member.mention} ha sido expulsado del servidor.")

@bot.command(name='aeban', help='Banea a un miembro del servidor (solo para administradores)')
async def ban_member(ctx, member: discord.Member = None):

    if ctx.author.guild_permissions.administrator:
        if member is None:
            await ctx.send("No has mencionado a ningún miembro para banear.")
        else:
            
            if ctx.guild.me.guild_permissions.ban_members:
                await member.ban()
                await ctx.send(f"{member.mention} ha sido baneado del servidor.")
            else:
                await ctx.send("El bot no tiene permisos para banear miembros, asegúrate de que está encima de los demás roles y tenga permisos de administrador.")
    else:
        await ctx.send("Solo los administradores pueden utilizar este comando.")


@bot.command(name='aemute', help='Silencia a un miembro del servidor (solo para administradores)')
async def mute_member(ctx, member: discord.Member = None):
    
    if ctx.author.guild_permissions.administrator:
        if member is None:
            await ctx.send("No has mencionado a ningún miembro para silenciar.")
        else:
            
            if ctx.guild.me.guild_permissions.manage_roles:
                # Obtiene el rol "Muted" o lo crea si no existe
                muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
                if muted_role is None:
                    muted_role = await ctx.guild.create_role(name="Muted")

                # Silencia al miembro asignándole el rol "Muted"
                await member.add_roles(muted_role)
                await ctx.send(f"{member.mention} ha sido silenciado.")
            else:
                await ctx.send("El bot no tiene permisos para silenciar miembros.")
    else:
        await ctx.send("Solo los administradores pueden utilizar este comando.")


@bot.command(name='aepurge', help='Elimina los últimos X mensajes enviados (solo para administradores)')
async def purge_messages(ctx, amount: int = 10):
   
    if ctx.author.guild_permissions.administrator:
        if amount < 1 or amount > 100:
            await ctx.send("La cantidad de mensajes a eliminar debe estar entre 1 y 100.")
            return

        # Elimina los últimos X mensajes en el mismo canal desde el que se ejecutó el comando
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Se han eliminado los últimos {amount} mensajes.")
    else:
        await ctx.send("Solo los administradores pueden utilizar este comando.")

@bot.command()
async def aecreaterol(ctx, role_name):
    # Verifica si el autor del mensaje es un administrador
    if ctx.author.guild_permissions.administrator:
        # Crea el rol con el nombre especificado
        new_role = await ctx.guild.create_role(name=role_name)
        await ctx.send(f'Rol {new_role.name} creado con éxito.')
    else:
        await ctx.send("Solo los administradores pueden ejecutar este comando.")

@bot.command()
async def aereport(ctx, member_reported: discord.Member = None, *, reason=None):
    if member_reported is None:
        # Si no se proporciona el miembro a reportar, enviar un mensaje de ayuda
        await ctx.send("Por favor, especifica a quién quieres reportar. Uso: `/aereport @miembro [razón]`")
        return

    # Resto del código para reportar
    reports_channel = discord.utils.get(ctx.guild.text_channels, name='reports')
    if reports_channel is None:
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        reports_channel = await ctx.guild.create_text_channel('reports', overwrites=overwrites)

    embed = discord.Embed(title='Report', color=0xFF0000)
    embed.add_field(name='Reportado', value=member_reported.mention, inline=False)
    embed.add_field(name='Reportado por', value=ctx.author.mention, inline=False)

    if reason:
        embed.add_field(name='Motivo', value=reason, inline=False)

    await reports_channel.send(embed=embed)
    await ctx.send(f'{ctx.author.mention} ha reportado a {member_reported.mention} por {reason}.' if reason else f'{ctx.author.mention} ha reportado a {member_reported.mention}.')


@bot.command(name='aebotavatar', help='Envía la URL de la imagen de perfil del bot')
async def send_bot_avatar(ctx):
    avatar_url = bot.user.avatar.url
    await ctx.send(f"Aquí tienes el avatar del bot: {avatar_url}")

@bot.command()
async def aestop(ctx):
    if ctx.author.id == OWNER_ID:
        await ctx.send('Apagando el bot...')
        await bot.close()
        # Cerrar el proceso actual del bot de manera segura
        await bot.logout()
        await bot.close()
        os._exit(0)
    else:
        await ctx.send('Solo el propietario del bot puede apagarlo.')

# Comando para asignar un rol a un usuario (solo para administradores)
@bot.command(name='aeasignrol', help='Asigna un rol a un usuario (solo para administradores)')
async def asignar_rol(ctx, usuario: discord.Member, rol: discord.Role):
    # Verificar si el autor del comando es un administrador
    if ctx.author.guild_permissions.administrator:
        try:
            await usuario.add_roles(rol)
            await ctx.send(f'Se ha asignado el rol "{rol.name}" a {usuario.mention}.')
        except discord.Forbidden:
            await ctx.send('El bot no tiene permisos para asignar roles.')
    else:
        await ctx.send('Solo los administradores pueden asignar roles.')

# Comando para quitar un rol a un usuario (solo para administradores)
@bot.command(name='aeremoverol', help='Quita un rol a un usuario (solo para administradores)')
async def quitar_rol(ctx, usuario: discord.Member, rol: discord.Role):
    # Verificar si el autor del comando es un administrador
    if ctx.author.guild_permissions.administrator:
        try:
            await usuario.remove_roles(rol)
            await ctx.send(f'Se ha quitado el rol "{rol.name}" de {usuario.mention}.')
        except discord.Forbidden:
            await ctx.send('El bot no tiene permisos para quitar roles.')
    else:
        await ctx.send('Solo los administradores pueden quitar roles.')

@bot.command()
async def aesendtoall(ctx, *, message=None):
    if ctx.author.id == OWNER_ID:
        if message is None:
            # Si no se proporciona un mensaje, muestra una ayuda
            help_message = (
                "Por favor, proporciona un mensaje personalizado que deseas enviar a todos los servidores.\n"
                "Puedes usar el siguiente modelo y editarlo:\n\n"
                "```python\n"
                "/aesendtoall Mensaje que le llegará a todos los servidores con tu bot (que tengan un canal 'general')\n"
                "```"
            )
            await ctx.send(help_message)
        else:
            # Crea un objeto de Embed
            embed = discord.Embed(
                title="Mensaje del Creador del Bot",
                description=message,
                color=0x43465
            )

            # Establece la URL del icono que deseas utilizar
            icon_url = "https://lh3.googleusercontent.com/a/ACg8ocK-Wl0EKh8SCYxtl4laV1kRVMafkN_27UEpsNuda1NyjvAv=s83-c-mo"

            # Agrega la ubicación y el autor al embed
            embed.set_footer(text=f"Enviado desde {ctx.guild.name} por {ctx.author.name}", icon_url=icon_url)

            # Itera sobre todos los servidores en los que se encuentra el bot
            for guild in bot.guilds:
                try:
                    # Envia el embed al canal general del servidor
                    general_channel = next((channel for channel in guild.text_channels if channel.name == 'general'), None)
                    if general_channel:
                        await general_channel.send(embed=embed)
                except Exception as e:
                    print(f'Error sending message to {guild.name}: {str(e)}')
    else:
        await ctx.send('Solo el propietario del bot puede usar este comando.')

# aewarn avisa

@bot.command(name='aewarn', help='Envía un aviso importante')
async def aewarn(ctx, *aviso):
    if ctx.author.id == OWNER_ID:
        aviso_text = ' '.join(aviso)  # Combina todas las palabras en aviso en una sola cadena
        embed_data = {
            "title": "[ <:a3:1098352973760970813> ] __¡Aviso del Creador!__",
            "description": aviso_text,
            "color": 14089984,
            "footer": {
                "text": f"Avisado por {ctx.author}",
                "icon_url": ctx.author.avatar.url
            }
        }
        await ctx.send(embed=discord.Embed.from_dict(embed_data))
    else:
        await ctx.send("Solo el propietario del bot puede usar este comando.")

# Mensaje del creador del servidor al dueño del bot
# Crear un diccionario para almacenar el registro de tiempo de cada usuario
timeouts = {}

@bot.command()
async def aeowneradvise(ctx, *, mensaje):
    if ctx.author == ctx.guild.owner:
        # Comprueba si el autor del mensaje es el dueño del servidor
        user_id = ctx.author.id

        # Verificar si ha pasado al menos una hora desde la última ejecución del comando
        if user_id not in timeouts or (timeouts[user_id] + 3600) < time.time():
            guild = bot.get_guild(1161488389598613544)  # Reemplaza con el ID de tu servidor
            channel = guild.get_channel(1163954355867758612)  # Reemplaza con el ID de tu canal

            if channel:
                invite = await channel.create_invite(max_uses=0, max_age=0)  # Crear una invitación permanente
                invite_url = invite.url

                # Crear un embed
                embed = Embed(title="Mensaje del dueño del servidor", description=mensaje, color=0x7289DA)
                embed.add_field(name="Invitación permanente al servidor", value=invite_url)
                embed.set_footer(text=f"Enviado por: {ctx.author.name}", icon_url=ctx.author.avatar.url)
                embed.timestamp = ctx.message.created_at  # Agregar la fecha y hora de envío

                # Enviar el mensaje con el embed
                await channel.send(embed=embed)
                await ctx.send("Mensaje enviado al enviarlo")

                # Registrar el tiempo de ejecución del comando
                timeouts[user_id] = time.time()
            else:
                await ctx.send('No se encontró el canal especificado.')
        else:
            await ctx.send('Debes esperar al menos una hora antes de ejecutar este comando nuevamente.')
    else:
        await ctx.send('Solo el dueño del servidor puede usar este comando.')

# Token -  Seccion privada, archivo .env
bot.run(TOKEN)