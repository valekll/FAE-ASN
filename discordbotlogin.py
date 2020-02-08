# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: lordv
"""

import agent
import discord
import time

agents = agent.findAgents()

TOKEN = 'XXXXXXXXXX'
for agentx in agents:
    if agentx.TOKEN == '':
        agents.remove(agentx)
        
def runBot(agentx):    
    TOKEN = agentx.TOKEN
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
       
            
    client.run(TOKEN)

runBot(agents[0])
