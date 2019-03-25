# Work with Python 3.6

from discord import Game
from discord.ext.commands import Bot

# Get at discordapp.com/developers/applications/me
TOKEN = 'NTUyNzgwNTk0MjA0MTE0OTYz.D2wmuQ.oTH-g08OJFHLqWtapj3KXninegU'

BOT_PREFIX = "!"

commands = {
    '!help': 'Print this',
    '!f1': 'f1'
}


client = Bot(command_prefix=BOT_PREFIX)


@client.command()
async def helps():
    for k in commands:
        await client.say(k + ':' + commands[k])


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
