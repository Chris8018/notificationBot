# Discord BOT: notification BOT

My first Discord BOT with python

## How to

1. Create a server
Create at https://discordapp.com

2. Create an app and a bot for the app
Create at https://discordapp.com/developers/applications/me
Then go to section *bot* to create a bot

3. Authorize the bot for a server
https://discordapp.com/oauth2/authorize?client_id=X&scope=bot
where X = *CLIENT ID*

4. Install discord package
python -m pip install discord.py==0.16.12

5. Sample code

        # Work with Python 3.6
        import discord
        
        TOKEN = 'XXXXXXXXXX'
        
        client = discord.Client()
        
        @client.event
        async def on_message(message):
            # we do not want the bot to reply to itself
            if message.author == client.user:
                return
        
            if message.content.startswith('!hello'):
                msg = 'Hello {0.author.mention}'.format(message)
                await client.send_message(message.channel, msg)
        
        @client.event
        async def on_ready():
            print('Logged in as')
            print(client.user.name)
            print(client.user.id)
            print('------')
        
        client.run(TOKEN)
    
