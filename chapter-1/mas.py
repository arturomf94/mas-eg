import numpy as np

class MAS:
    def __init__(self, nb_agents, adjacency_matrix):
        self.tick = 0
        self.agent_list = []
        
        # Initialize neighbors based on the matrix
        for i in range(nb_agents):
            self.agent_list.append(Agent(i, np.nonzero(adjacency_matrix[i])[0]))
            
    def run(self, rounds):
        for i in range(0,rounds):
            self.runOnce()

    def runOnce(self):
        self.tick += 1
        for agent in self.agent_list:
            agent.decide(self.tick)
        print("tick " + str(self.tick) + " ended")
           
class Agent:
    def __init__(self, id_number, neighbors) : 
        self.id_number = id_number
        self.neighbors = neighbors
        self.domain = []
        self.value = ''
        self.binary_constraints = []
        self.messages = []
        self.flag = True
            
    def decide(self, tick):
        #self.revise()
        print(self.neighbors)

    # def revise(self):
    #     for message in self.messages:
    #         # each message is a list containing some other nodes domain