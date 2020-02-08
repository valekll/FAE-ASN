# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: lordv
"""

import agent
import discord

def genMessage(oldmsg, agentx):
    return 'test'

agents = agent.findAgents()

TOKEN = 'XXXXXXXXXX'

for agentx in agents:
    TOKEN = agentx.TOKEN

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        channel = client.get_channel(675698151935442967)
        newmsg = genMessage(oldmsg, agentx)
        await channel.send(newmsg)
        await client.logout()

    client.run(TOKEN)