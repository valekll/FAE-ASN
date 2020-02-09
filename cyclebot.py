# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: orvy
"""

import agent
import discord
import time
from random import randint
import os

def cycle(i):
    msg = "test message"
    print(i)
    with open('data/agentindex', 'w', encoding = 'utf-8') as f:
        f.write(str(i))
    print('\n')
    print(msg)
    with open('data/agentmsg', 'w', encoding = 'utf-8') as f2:
        f2.write(msg)
    os.system("python runbot.py")

def talk(agentx):
    chatTotal = 0
    agents = agent.findAgents()
    for agentx in agents:
        if agentx.TOKEN == '':
            agents.remove(agentx)
        else:
            chatTotal += agentx.chatRate
    rng = randint(0, chatTotal) + 1
    if rng <= agentx.chatRate:
        return True;
    return False;
    
    
agents = agent.findAgents()
for agentx in agents:
    if agentx.TOKEN == '':
        agents.remove(agentx)

i = 0
lastBot = agents[0]
while(True):
    agentx = agents[i]
    if talk(agentx) and lastBot != agentx:
        cycle(i)
        lastBot = agentx
    i = i + 1
    if i == len(agents):
        i = 0
