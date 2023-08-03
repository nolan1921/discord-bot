
import discord
import random
import bestloan
import requests
import json

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
    
    if message.content.startswith('$loans'):
        if len(message.content.split())>1:
            collection = message.content.split()[1]
            BASE_URL = "https://dev-skillet-backend-rng3tbs6qq-uc.a.run.app/topLoanOfferForCollection"

            collection_address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
            response = requests.get(f"{BASE_URL}?collectionAddress={collection_address}")

            offer = json.loads(response.text)
            print(offer)
            #await message.channel.send("Loans for " + collection)
            #print(message.content.split())
    #if message.content.startswith('How are you today?'):
    #    await message.channel.send('Average at best') hello 
    
    #if message.content.startswith('roll'):
    #    await message.channel.send(str(random.randint(1,6)))
                                   
    if message.content.startswith('Ethereum loan'):
       await message.channel.send('The best avaiable loan for Etherem: ' )#inputbestloan

client.run('MTExODM3MTEzMTQ2OTA5MDgzNg.GYZpMo.O9NGiLD4HcsssiNs2-tUibjBR2RDD0PICkp3r8')