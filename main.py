import discord
from discord.ext import commands
from main import get_class
import os, random 
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data ["url"]
@bot.command("duck")
async def duck(ctx):
    print("hola esta va a ser la foto")
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename     # Aquí guardamos el nombre del archivo
            file_url = attachment.url           # (opcional, si quisieras hacer algo con la URL)
            # Usamos file_name en lugar de repetir attachment.filename
            await attachment.save(f"./{file_name}")
            result = get_class(
                model_path="./keras_model.h5",
                labels_path="labels.txt",
                image_path=f"./{file_name}"
            )
            await ctx.send(result)
    else:
        await ctx.send("no subiste tu imagen :(")


bot.run("token")