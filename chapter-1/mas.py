import numpy as np
import sys

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
        final_tick = sys.maxint
        while not finished:
            self.tick += 1
            agents_no_solution_flag = []
            agents_domain_lengths = []
            for agent in self.agent_list:
                agents_no_solution_flag.append(agent.no_solution_flag)
                agents_domain_lengths.append(len(agent.domain))
            if self.tick == final_tick or True in agents_no_solution_flag:
                finished = True
                if self.tick == final_tick:
                    print('Solution found!')
                if True in agents_no_solution_flag:
                    print('There is no solution!')
                break
            for agent in self.agent_list:
                print('Agent ' + str(agent.id_number) + ' has domain: \n')
                print(agent.domain)
                agent.arc_consistency()
            if all(length == 1 for length in agents_domain_lengths):
                final_tick = self.tick + 1
            print("tick " + str(self.tick) + " ended")
            if self.tick == 5:
                print('Could not find solution!')
                break
       
class Agent:
    def __init__(self, id_number, neighbors) : 
        self.id_number = id_number
        self.neighbors = neighbors
        self.domain = []
        self.value = ''
        self.binary_constraints = []
        self.messages = []
        self.no_solution_flag = False
            
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
        if len(self.domain) == 0:
            self.no_solution_flag = True

    # def revise(self):
    #     for message in self.messages:
    #         # each message is a list containing some other nodes domain