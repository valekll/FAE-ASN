# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: lordv
"""

import agent
import discord
import time

def genMessage(oldmsg, agentx):
    return agentx.name + ' is a nerd'

agents = agent.findAgents()

TOKEN = 'XXXXXXXXXX'
for agentx in agents:
    if agentx.TOKEN == '':
        agents.remove(agentx)
        
def runBot(agentx, msg):    
    TOKEN = agentx.TOKEN
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        channel = client.get_channel(675698151935442967)
        await channel.send(msg)     
        await client.logout()
        
    client.run(TOKEN)

agentx = agents[0]
msg = genMessage('old msg', agentx)
runBot(agentx, msg)
