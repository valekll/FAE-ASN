# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: orvy
"""

import agent
import discord
import time
import runbot

agents = agent.findAgents()

for agentx in agents:
    if agentx.TOKEN == '':
        agents.remove(agentx)

i = 0
while(True):
	agentx = agents[i]
	msg = "test message"
	runbot.runBot(agentx,msg)
	i = i + 1
	if(i==len(agents)):
		i = 0
