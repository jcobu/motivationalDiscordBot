'''
@jcobu
Requirements: https://github.com/Rapptz/discord.py
'''

import discord, urllib.request

client = discord.Client()
url = "https://inspirobot.me/api?generate=true"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!motivateme'): # Chose a ! prefix but that and the words can be changed
        def inspiroBotGrabber():
            user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
            headers= {'User-Agent':user_agent,}
            request = urllib.request.Request(url,None,headers) # The assembled request
            response = urllib.request.urlopen(request)
            data = response.read() # The data
            return data.decode('UTF-8')
        print('{client.user} requested !motivateme')
        image = inspiroBotGrabber()
        await message.channel.send(image)
        
client.run('DISCORD-KEY-GOES-HERE')
