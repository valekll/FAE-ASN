# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: lordv
"""

import agent
import discord
import time
import argparse

"""
parser = argparse.ArgumentParser(
	description='Program used to login a single bot and send a message')
parser.add_argument("integer", metavar='N', default=0, type=int, required=False, help="Index of the bot")
parser.add_argument("string", metavar='S', default='', type=str, required=False, help="Message to be sent by the bot")
args = parser.parse_args()
index = args.integer
argmsg = args.string
"""
def getMessage():
    msg = ''
    with open('data/agentmsg', 'r', encoding = 'utf-8') as f:
        msg = f.read()
    return msg

def getIndex():
    index = 0
    with open('data/agentindex', 'r', encoding = 'utf-8') as f:
        index = int(f.read())
    return index

agents = agent.findAgents()
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
        lastmsg = channel.last_message.content
        lastauthor = channel.last_message.author.name
        with open('data/lastmsg', 'w', encoding = 'utf-8') as f:
            f.write(lastmsg)
        with open('data/lastauthor', 'w', encoding = 'utf-8') as f2:
            f2.write(lastauthor)
        await client.logout()
        
    client.run(TOKEN)

agentx = agents[getIndex()]
msg = getMessage()
runBot(agentx, msg)

