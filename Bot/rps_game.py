import discord
import random
from discord.ext import commands

TOKEN = "put"


prefix = "!"
needed_intents = discord.Intents.default()
needed_intents.message_content = True

client = commands.Bot(command_prefix=prefix,intents=needed_intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
async def rps(ctx):
    rpsGame=["rock", "paper", "scissors"]
    win_combination = [["rock", "scissors"],
                        ["paper", "rock"],
                        ["scissors", "paper"]]
    computer_choice = random.choice(rpsGame)
    user_choice = random.choice(rpsGame)
    emoji = {
    "rock"    : ":fist:",
    "paper"  : ":hand_splayed:",
    "scissors": ":v:"
    }
    if user_choice == computer_choice:
        await ctx.send(f"**Tie**:confused: You chose {emoji[user_choice]},Computer chose {emoji[computer_choice]}")
    elif [user_choice,computer_choice] in win_combination:
        await ctx.send(f"**Win**:partying_face: You chose {emoji[user_choice]},Computer chose {emoji[computer_choice]}")
    else:
        await ctx.send(f"**Loss**:smiling_face_with_tear: You chose {emoji[user_choice]},Computer chose {emoji[computer_choice]}")

client.run(TOKEN)
