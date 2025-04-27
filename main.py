import discord
from discord.ext import commands

# Define intents necesarios
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Crea una instancia del bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Diccionario base de recomendaciones por preferencia
auto_recomendaciones = {
    "elegancia": "Mercedes-Benz Clase E o Clase S",
    "comodidad": "Mercedes-Benz Clase V o Clase E",
    "deportivo": "Porsche 911 o BMW M4",
    "económico": "Toyota Corolla o Kia Rio",
    "tecnológico": "Tesla Model 3 o Audi e-tron",
}

# Evento cuando el bot esté listo
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Comando para recomendar un auto según el gusto
@bot.command()
async def auto(ctx, gusto: str):
    gusto = gusto.lower()
    if gusto in auto_recomendaciones:
        recomendacion = auto_recomendaciones[gusto]
        await ctx.send(f"Según tu gusto por la **{gusto}**, te recomiendo: **{recomendacion}**")
    else:
        await ctx.send("No tengo una recomendación para ese gusto. Intenta con: elegancia, comodidad, deportivo, económico o tecnológico.")

# Ejecutar el bot (reemplaza 'TU_TOKEN_AQUI' por el token de tu bot de Discord)
bot.run('TU_TOKEN_AQUI')
