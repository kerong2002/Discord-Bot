import discord
import random
from discord.ext import commands

TOKEN = "put"


word=[]
f = open("word.txt", "r")
for s in f:
    word.append(s)
answer = random.choice(word)
check = []
for i in range(5):
    check.append(-1)
prefix = "!"
needed_intents = discord.Intents.default()
needed_intents.message_content = True

client = commands.Bot(command_prefix=prefix,intents=needed_intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def wordle(ctx, message):
    global answer,word,check
    user_guess = message.lower()
    print(answer)
    for x in range(5):
        check[x] = -1
    for A in range(5):
        if(check[A] == -1 and user_guess[A] == answer[A]):
            check[A] = 1
    for y in range(0,5):
        for x in range(0,5):
            if (check[y] != 1 and user_guess[x]==answer[y]):
                check[y] = 0
    returnString = ""
    cnt = 0
    for x in range(5):
        if(check[x] == 1):
            cnt += 1
            returnString += ":green_square:"
        elif(check[x] == 0):
            returnString += ":yellow_square:"
        else:
            returnString += ":white_large_square:"
    await ctx.send(returnString)
    if(cnt == 5):
        answer = random.choice(word)
        await ctx.send(":partying_face: ")
client.run(TOKEN)
