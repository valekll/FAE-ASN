# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 09:11:26 2020

@author: lordv
"""

import os
import json

class Agent:
    def __init__(self, data):
        self.__dict__ = data
        
def findAgents():
    with open('data/agents.json', 'r') as agentFile:
        agentsJSON = json.load(agentFile)
       
        agents = []
        for agentJSON in agentsJSON:
            agentx = Agent(agentJSON)
            agents.append(agentx)
        
        print('Found the following agents: ')
        for agentx in agents:
            print(agentx.__dict__)
        print('\n')
        
        return agents

def writeAgents(agents):
    print('Writing the following agents: ')
    for agentx in agents:
            print(agentx.__dict__)
    print('\n')
                
    with open('data/agents.json', 'w') as agentFile:
        agentFile.write('[\n')
    
    with open('data/agents.json', 'a') as agentFile:
        i = 1
        for agentx in agents:
            json.dump(agentx.__dict__, agentFile)
            if i < len(agents):
                agentFile.write(',')
            agentFile.write('\n')
        i += 1
    
    agentFile.write(']')

def createAgents(num):
    agents = []
    dict = { "name" : "", "TOKEN" : "", "chatRate" : 5, "disposition" : 0.0, 
            "intensity" : 0.0, "likes" : 0, "dislikes" : 0, "relationships" : {}}
    for i in range(num):
        agentx = Agent(dict)
        agents.append(agentx)
        
    print('Created the following agents: ')
    for agentx in agents:
            print(agentx.__dict__)
    print('\n')
    return agents
