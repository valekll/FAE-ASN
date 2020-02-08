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
    
    i = 1
    with open('data/agents.json', 'a') as agentFile:
        for agentx in agents:
            json.dump(agentx.__dict__, agentFile)
            if i < len(agents):
                agentFile.write(',')
            agentFile.write('\n')
        i += 1
    
    agentFile.write(']')

def createAgents():
    agents = []
    dict = { "name" : "", "TOKEN" : "", "chatRate" : ""}
    for i in range(4):
        agentx = Agent(dict)
        agents.append(agentx)
        
    print('Created the following agents: ')
    for agentx in agents:
            print(agentx.__dict__)
    print('\n')
    return agents
    
#agents = findAgents()
#agents = createAgents()
#writeAgents(agents)