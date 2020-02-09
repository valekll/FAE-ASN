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

i = len(agents)
while(True):
	agentx = agents[i]
	msg = "test message"
	runBot(agentx,msg)
	i = i-1
	if(i==-1):
		i = len(agents)
