Programa creado por Nisamov, derechos pertenecientes a el, si se plagia por lo menos decir que no es vuestro código


[AutoStartup]:
Startup	>> \Windows\Start Menu\Programs\Startup
		>> shell:startup

Acceso directo de "startup" en \Programs\Startup

[ManualStartup]:
venv\Scripts\activate
python dominicius.py


[Es necesario instalar las dependencias]:

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import tasks
import datetime
from discord import File
import random
import subprocess
from discord import Embed
import asyncio
import time


[Instalación]:
pip install requests
pip install discord
pip install python-dotenv
pip install asyncio
pip install datetime