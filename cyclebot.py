# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: orvy
"""

import agent
import discord
import time
#import runbot
import os

agents = agent.findAgents()

for agentx in agents:
    if agentx.TOKEN == '':
        agents.remove(agentx)

i = 0
while(True):
    agentx = agents[i]
    msg = "test message"
    print(i)
    with open('data/agentindex', 'w', encoding = 'utf-8') as f:
        f.write(str(i))
    print('\n')
    print(msg)
    with open('data/agentmsg', 'w', encoding = 'utf-8') as f2:
        f2.write(msg)
    os.system("python runbot.py")
    i = i + 1
    if i == len(agents):
        i = 0
