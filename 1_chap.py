import numpy as np

class SMA:
    def __init__(self, nb_agents, adjacency_matrix):
        self.tick = 0
        self.agentList = []
        
        # Initialize accointances based on the matrix
        for i in range(nb_agents):
            self.agentList.append(Agent(i, np.nonzero(adjacency_matrix[i].A1)[0]))
            
    def run(self, rounds):
        for i in range(0,rounds):
            self.runOnce()

    def runOnce(self):
        self.tick += 1
        for agent in self.agentList:
            agent.decide(self.tick)
        print("tick " + str(self.tick) + " ended")
           
class Agent:
    def __init__(self, id_number, accointances) : 
        self.id_number = id_number
        self.accointances = []
        self.domain = []
        self.messages = []
        self.flag = True
            
    def decide(self):
        self.revise()

    def revise(self):
        for message in self.messages:
            # each message is a list containing some other nodes domain
            