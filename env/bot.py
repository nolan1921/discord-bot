
import discord
import random
import bestloan

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#ethloan = bestloan.handle_response()

@client.event

async def on_message(message):
    print(message)
    
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    #if message.content.startswith('How are you today?'):
    #    await message.channel.send('Average at best')
    
    #if message.content.startswith('roll'):
    #    await message.channel.send(str(random.randint(1,6)))
                                   
    if message.content.startswith('Ethereum loan'):
       await message.channel.send('The best avaiable loan for Etherem: ' )#inputbestloan

client.run('MTExODM3MTEzMTQ2OTA5MDgzNg.GP7zba.aIvAlexTIydSIFaiA0rMneF8zBpaYsLbV-yq9k')