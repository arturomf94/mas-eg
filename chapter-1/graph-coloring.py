import mas
import random

#### Graph coloring problems: 

### Example 1:

## Setup: 

# Instantiate MAS with adjecency matrix

eg1 = mas.MAS(3, [[0,1,1],[1,0,1],[1,1,0]])

# Declare domains

domains = [['red'],['red', 'blue'], ['red', 'blue', 'green']]

# Assign domains, values and binary constraints for each agent

for agent in eg1.agent_list:
	agent.domain = domains[agent.id_number]
	agent.value = random.choice(agent.domain)
	agent.binary_constraints = [(agent.id_number, other_agent.id_number) for 
									other_agent in agent.neighbors]


import pdb;pdb.set_trace()