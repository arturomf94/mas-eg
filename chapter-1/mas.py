import numpy as np

class MAS:
    def __init__(self, nb_agents, adjacency_matrix):
        self.tick = 0
        self.agent_list = []
        
        # Initialize neighbors based on the matrix
        for i in range(nb_agents):
            self.agent_list.append(Agent(i, np.nonzero(adjacency_matrix[i])[0]))

        # Update neighbors: 
        for agent in self.agent_list:
            neighbor_ids = agent.neighbors
            agent.neighbors = [self.agent_list[i] for i in neighbor_ids]
            
    def run(self, rounds):
        for i in range(0,rounds):
            self.runOnce()

    def runOnce(self):
        self.tick += 1
        for agent in self.agent_list:
            agent.decide(self.tick)
        print("tick " + str(self.tick) + " ended")

    def run_arc_consistency(self):
        finished = False
        while not finished:
            self.tick += 1
            agents_finished = []
            for agent in self.agent_list:
                agents_finished.append(agent.finished_flag)
            for agent in self.agent_list:
                print('Agent ' + str(agent.id_number) + ' has domain: \n')
                print(agent.domain)
                agent.arc_consistency()
            if not False in agents_finished:
                finished = True
            print("tick " + str(self.tick) + " ended")
            if self.tick == 5:
                break
       
class Agent:
    def __init__(self, id_number, neighbors) : 
        self.id_number = id_number
        self.neighbors = neighbors
        self.domain = []
        self.value = ''
        self.binary_constraints = []
        self.messages = []
        self.finished_flag = False
            
    def decide(self, tick):
        print('something')

    def send_message(self, message, neighbor):
        neighbor.messages.append((self.id_number, message))

    def arc_consistency(self):
        if len(self.domain) == 1:
            for neighbor in self.neighbors:
                self.send_message(self.domain[0], neighbor)
        if self.messages != []:
            for message in self.messages:
                if (self.id_number, message[0]) in self.binary_constraints and \
                    message[1] in self.domain:
                    self.domain.remove(message[1])
        if len(self.domain) == 1 or len(self.domain) == 0:
            self.finished_flag = True

    # def revise(self):
    #     for message in self.messages:
    #         # each message is a list containing some other nodes domain