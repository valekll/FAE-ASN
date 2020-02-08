# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: lordv
"""

import agent
import discord
import time

def genMessage(oldmsg, agentx):
    return 'test'

agents = agent.findAgents()

TOKEN = 'XXXXXXXXXX'
for agentx in agents:
    if agentx.TOKEN == '':
        agents.remove(agentx)
for agentx in agents:        
    TOKEN = agentx.TOKEN

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        channel = client.get_channel(675698151935442967)
        if channel == message.channel:
            oldmsg = ''
            newmsg = genMessage(oldmsg, agentx)
            await channel.send(newmsg)
            await client.logout()
            time.sleep(.2)
            
    client.run(TOKEN)
