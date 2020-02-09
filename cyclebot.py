# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:55:33 2020

@author: lordv, orvy
"""

import agent
import discord
import time
import evaluation
from random import randint
import os

def adjustRMS(agentx, rms, lastbot):
    rms = rms + agentx.disposition + agentc.mood
    rms = rms + (.5 * agentx.fae.lastbot)
    rms = rms * agentx.intensity
    rms = rms / 4
    return rms

def cycle(i, agentx, lastbot):
    #listen for message
    msg = "test message"

    #evaluate msg for rms
    rms = evaluation.evaluate_string(msg)

    #adjust received message score
    arms = adjustRMS(agentx, rms, lastbot)

    #then we adjust agent, but we'll get to that.
    #then we generate and decide from dialogue options
    reply = evaluation.decide_dialogue(arms, evaluate_dialogue(msg))

    #post message to discord
    print(i)
    with open('data/agentindex', 'w', encoding = 'utf-8') as f:
        f.write(str(i))
    print('\n')
    print(reply)
    with open('data/agentmsg', 'w', encoding = 'utf-8') as f2:
        f2.write(reply)
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
        cycle(i, agentx, lastbot)
        lastBot = agentx
    i = i + 1
    if i == len(agents):
        i = 0
