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
    for residuo in range(random.shuffle(residuos.values())):
        lst += f'{residuo}\n'
    await ctx.send(lst)

bot.run("Token")
