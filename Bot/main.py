import discord

TOKEN = 'MTAxNjAxNTQzNjYxNTI1NDA3Ng.GTlrzV.UcBuK80WSeD7jh_Y0_JZKwFxqqwRC_4qUJu6i4'

intent = discord.Intents.default()
intent.message_content = True

client = discord.Client(intents=intent)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Ken'):
        await message.channel.send('Ken ejaculate!')


client.run(TOKEN)
