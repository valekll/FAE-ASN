# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@authors: lordv, orvy
"""

import agent
import discord
import time
import argparse

parser = argparse.ArgumentParser(
	description='Program used to login a single bot')
parser.add_argument("integer", metavar='N', default=0, type=int, help="Index of the bot")
args = parser.parse_args()
argent = args.integer

def genMessage(oldmsg, agentx):
    return 'reed is a nerd'

agents = agent.findAgents()
        
def runBot(agentx):    
    TOKEN = agentx.TOKEN
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        channel = client.get_channel(675698151935442967)
         
    client.run(TOKEN)

runBot(agents[argent])
