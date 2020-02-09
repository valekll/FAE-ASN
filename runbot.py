# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: lordv
"""

import agent
import discord
import time
import argparse

parser = argparse.ArgumentParser(
	description='Program used to login a single bot and send a message')
parser.add_argument("--i", default=0, type=int, help="Index of the bot")
parser.add_argument("--m", default='', type=str, help="Message to be sent by the bot")
args = parser.parse_args()
index = args.i
argmsg = args.m

def genMessage(oldmsg, agentx):
    return agentx.name + ' is a nerd'

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
        await client.logout()
        
    client.run(TOKEN)

agentx = agents[index]
msg = genMessage('old msg', agentx)
msg = argmsg
runBot(agentx, msg)
