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

def adjustRMS(agentx, rms, lastauthor):
    rms = rms + agentx.disposition + agentx.mood
    faev = 0
    
    for bot in agentx.fae:
        if bot['name'] == lastauthor:
            faev = bot['v'] 
            break   
    
    rms = rms + (.5 * faev)
    rms = rms * agentx.intensity
    rms = rms / 4
    return rms

def cycle(i, agentx):
    #listen for message
    msg = ''
    with open('data/lastmsg', 'r', encoding = 'utf-8') as f:
        msg = f.read()
    author = ''
    with open('data/lastauthor', 'r', encoding = 'utf-8') as f:
        author = f.read()
    print(author)

    msg = '"' + msg + '"'
    print(msg)
        
    #evaluate msg for rms
    rms = evaluation.evaluate_string(msg)

    #adjust received message score
    arms = adjustRMS(agentx, rms, author)

    #then we adjust agent, but we'll get to that.
    #then we generate and decide from dialogue options
    reply = evaluation.decide_dialogue(arms, evaluation.evaluate_dialogue(msg))
    reply = reply.strip()
    if(reply[:-1] == ','):
        reply = reply[:-1]

    #post message to discord
    print(i)
    with open('data/agentindex', 'w', encoding = 'utf-8') as f:
        f.write(str(i))
    print('\n')
    print(reply)
    with open('data/agentmsg', 'w', encoding = 'utf-8') as f2:
        f2.write(reply)
    os.system("python runbot.py")
    return author
    
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
lastauthor = ''
while(True):
    agentx = agents[i]
    if talk(agentx) and lastauthor != agentx.name:
        lastauthor = cycle(i, agentx)
    i = i + 1
    if i == len(agents):
        i = 0
