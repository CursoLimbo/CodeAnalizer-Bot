import discord
import io
import sys
from code import interact
from lib2to3.pgen2 import token
from msilib import datasizemask
from multiprocessing.sharedctypes import Value
from turtle import title
from unicodedata import name
from discord.ext import commands
from decouple import config

intents=discord.Intents.all()
bot = commands.Bot(command_prefix="!", description='The Best Bot', intents = intents)
token = config('DISCORD_TOKEN')

structure = ["if", "for", "for-each", "while", "array", "ArrayList", "matriz", "arreglos", "listas enlazadas", "pilas", "colas", "arbol binario"]

@bot.event
async def on_ready():
    print('On ready')
    
@bot.command()
async def hackerrank(ctx, dificultad):
    embed = discord.Embed(title=f"problema nivel {dificultad}", description="Se desea hacer un if que revise si a es mayor que b", color=discord.Color.dark_purple())
    embed.add_field(name="codigo", value="\t  a = input()\n  b = input()\n#Poner codigo aqui")
    await ctx.send(embed=embed)

@bot.command()
async def helpCommands(ctx):
    embed = discord.Embed(title="Hello! I'm BotCode", description="Comados que el bot escucha", color=discord.Color.blue())
    embed.add_field(name="!helpmeCommands", value="Comando que da la informacion de todos los comados")
    embed.add_field(name="!helpme", value="Comando que da una explicación y un ejemplo de la estructura de control o de dato que especifique el usuario")
    embed.add_field(name="!inline", value="Comando que permite escribir código en la plataforma actual para realizar funciones básicas")
    embed.add_field(name="!archive", value="Comando que resive un archivo donde revisa si funciona bien el programa")
    embed.add_field(name="!hackerrank", value="Comando que envía problemas segun la dificultad elegida y se dara puntos si se resuelve exitosamente")
    embed.add_field(name="!points", value="Comando que muestra los puntos obtenidos por problemas resuelto por usuario")
    await ctx.send(embed=embed)

@bot.command()
# !helpme for java
async def helpme(ctx, struc: str, lenguaje: str):
    if (struc=="if" and lenguaje == "java"):
        embed1 = discord.Embed(title="Estructura de Control-if", description="La sentencia if se utiliza para ejecutar un bloque de código si, y solo si, se cumple una determinada condición. Por tanto, if es usado para la toma de decisiones. Es decir, solo si condición se evalúa a True , se ejecutarán las sentencias que forman parte de bloque de código .", color=discord.Color.dark_purple())
        embed1.add_field(name="codigo", value=f"```java\nedad = 70;\nif (edad >= 60){{\n    System.out.println('es un Aduto Mayor');\n}}else{{\n    System.out.println('es un Aduto');\n}}```")
        await ctx.send(embed=embed1)
        
    if (struc=="if" and lenguaje == "python"):
        embed1 = discord.Embed(title="Estructura de Control-if", description="La sentencia if se utiliza para ejecutar un bloque de código si, y solo si, se cumple una determinada condición. Por tanto, if es usado para la toma de decisiones. Es decir, solo si condición se evalúa a True , se ejecutarán las sentencias que forman parte de bloque de código .", color=discord.Color.dark_purple())
        embed1.add_field(name="codigo", value=f"```python\nedad = 70\nif edad >= 60:\n    print('es adulto mayor')```")
        await ctx.send(embed=embed1)
        
#     if (struc=="for"):
#         embed1 = discord.Embed(title="Estructura de Control-for", description="", color=discord.Color.dark_purple())
#         embed1.set_image(url="")
#         await ctx.send(embed=embed1)
        
#     if (struc=="for-each"):
#         embed1 = discord.Embed(title="Estructura de Control-", description="", color=discord.Color.dark_purple())
#         embed1.set_image(url="")
#         await ctx.send(embed=embed1)
        
#     if (struc=="while"):
#         embed1 = discord.Embed(title="Estructura de Control-", description="", color=discord.Color.dark_purple())
#         embed1.set_image(url="")
#         await ctx.send(embed=embed1)
        
#     if (struc=="array"):
#         embed1 = discord.Embed(title="Estructura de Control-", description="", color=discord.Color.dark_purple())
#         embed1.set_image(url="")
#         await ctx.send(embed=embed1)
        
#     if (struc=="ArrayList"):
#         embed1 = discord.Embed(title="Estructura de Control-", description="", color=discord.Color.dark_purple())
#         embed1.set_image(url="")
#         await ctx.send(embed=embed1)
#     if (struc=="matriz"):
#         embed1 = discord.Embed(title="Estructura de Control-", description="", color=discord.Color.dark_purple())
#         embed1.set_image(url="")
#         await ctx.send(embed=embed1)


@bot.command()
async def coderun(ctx, language: str, *args):
    if language == 'python':
        code = ";".join(args)
        stdout = io.StringIO()
        sys.stdout = stdout
        exec(code)
        sys.stdout = sys.__stdout__
        result = stdout.getvalue()
        print(result)
        await ctx.send(result)
    else:
        await ctx.send(f"Lo siento, {language} no es compatible en este momento.")

bot.run(token)