from agent import Agent
from Mission import Mission
from FieldAgent import FieldAgent
from CyberAgent import CyberAgent

agent1 = Agent("meir", 4)
agent2 = CyberAgent("efi", 5, "glilot")
agent3 = FieldAgent("ari",4,'yemen')

list_of_agents = [agent1, agent2,agent3]



def list_of_agents_1(list_agents: list):
    for i in list_agents:
        print(i.report())