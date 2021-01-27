# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='!!')

###game###

player1 = "Edmond"
player2 = "Pascal"
turn = "p1"
loser = "p1"
winner = "p2" 

##########

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(name='help')
async def printHelp(ctx):
    await ctx.send("dames : lancer une partie\nff : se rendre\nmove départ arrivée : bouger un pion\nturn : savoir à qui le tour")

@client.command(name='dames')
async def launch_game(ctx):
    player1 = ctx.author
    player2 = "Pascal"
    turn = player1
    await ctx.send("Ok, on se fait une partie.\nDucoup " + str(player1) + ", A TOI D'JOUER !")

    #await ctx.send(file=discord.File('board.png'))
    #startGame()
    #envoie le board de base
    
@client.command(name='ff')
async def forfeit(ctx):
    loser = ctx.author
    if loser == player1:
        winner = player2
    else:
        winner = player1 
    await ctx.send("Ah, le nul ! " + str(loser) + " s'est rendu, " + str(winner) + " est le vainqueur !")


@client.command(name='move')
async def nextMove(ctx, arg1, arg2):
    billy = ctx.author
    if turn == billy:
        await ctx.send("Tu veux donc bouger le pion " + str(arg1) + " en " + str(arg2) + "...")
        #faire des trucs
        turn = player2
    else:
        await ctx.send(str(billy) + " c'est pas à toi de jouer, gros naze !")
    return

def startGame():
    gameBoard = (
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',],
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',],
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',],
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',],
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',],
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',],
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',],
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',],
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',],
        ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B', 'N', 'B',])



client.run(TOKEN)