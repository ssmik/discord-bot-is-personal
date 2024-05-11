import discord
from discord import utils
import random
from discord.ext import commands
from discord.utils import get
import json


TOKEN = "Token"
PREFIX = ""

client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
@client.command()
async def q( ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    await ctx.send(f"**Общий** {author.mention}, **подтяни свои подштанники**")

@client.event
async def on_ready():
    print("Здарова сынки")

@client.command( pass_context = True )
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount + 1)
    await ctx.send("**я удалил твою жирную мамашу, возможно это сообщение не надо писать боту, ну мне пох**")

@client.command()
async def обнять(ctx, member: discord.Member = None):
    if member == None:
        return
    await ctx.channel.send(f"***сын марадонны*** {ctx.author.mention} ***обнял сына Пепе*** {member.mention}")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity= discord.Game("tg @ssmik1"))

@client.command()
async def embed(ctx):
    embed = discord.Embed(title="Правила Discord server`s", description="***Если ты админу отвечаешь не*** |**Сэр,да,Сэр | Сэр,нет,Сэр**| ***-->   то пункт 1.1***", color=discord.Color.red())
    embed.add_field(name="1.1", value="||**Тебе пиздец**||", inline=False)
    await ctx.send(embed=embed)

####### KICK FOR THE ROLE MAN
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1237038182479171636:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.name == "titan":
            role = discord.utils.get(guild.roles, name="titan")
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("sdelano ake done")
            else:
                print("role not found ake roly nety")
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 1238728036430385183:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.name == 'titan':
            role = discord.utils.get(guild.roles, name="titan")
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found")


@client.command()
async def t(ctx):
    default_role = utils.get(ctx.guild.roles, name="@everyone")
    for member in ctx.guild.members:
        if (len(member.roles) == 1) and (member.roles[0] == default_role):
            print(member.kick)
    await ctx.send(f"писька")



client.run(token=TOKEN)
