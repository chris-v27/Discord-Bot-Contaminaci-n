import discord
from bot_logic import *
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("Se inicio el bot")

residuos= {'Residuos orgánicos': ["Cáscaras de frutas y verduras", "Restos de comida", "Cáscaras de huevo", "Hojas secas",],
              'Residuos reciclables': ["Bolsas plásticas", "Tapas", "Periódicos", "revistas", "hojas de papel", "Cajas y cartón", "Envases de vidrio", "Jarrones", "Utensilios de cocina", "Latas",       ],
              'Residuos no reciclables': ["Pañales", "Esponjas de cocina", "Envolturas de caramelos"]}

@bot.command()
async def info(ctx):
    await ctx.send("Escribe -/residuos- para ver la lista de materiales disponibles a desechar",
                   "\nEscribe -/desechar- y escribe un número correspondiente, en que lugar se puede desechar el residuo",
                   "\nEscribe -/consejos- para ver una lista de consejos que te ayudaran a mejorar el planeta")

@bot.command()
async def residuos(ctx):
    lst = ''
    number = 0
    f = open("residuos.txt", "r")
    for residuo in f:
        number += 1
        lst += f'{number} {residuo}\n'
    f.close()
    await ctx.send(lst)

@bot.command()
async def desechar(ctx, num:int):
    f = open("residuos.txt", "r")
    residuo = {f.readline(num)}
    if residuo in residuos['Residuos orgánicos']:
        l_desechar = 'el compost'
    elif residuo in residuos['Residuos reciclables']:
        l_desechar = 'el contenedor de reciclaje'
    elif residuo in residuos['Residuos no reciclables']:
        l_desechar = 'Tacho de basura'
    f.close()
    
    await ctx.send(f'El residuo {residuo} debe tirarse en{l_desechar}')

@bot.command()
async def consejos(ctx):
    f = open("consejos.txt", "r")
    consejo = f.readline(random.randint(1,len(f)))
    await ctx.send(consejo)
    f.close()
    
bot.run("Token")
