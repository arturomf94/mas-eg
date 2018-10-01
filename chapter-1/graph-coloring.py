import mas

#### Graph coloring problems: 

### Example 1:

## Setup: 

# Instantiate MAS with adjecency matrix

eg1 = mas.MAS(3, [[0,1,1],[1,0,1],[1,1,0]])

# Declare domains

domains = [['red'],['red', 'blue'], ['red', 'blue', 'green']]

# Assign domains and values for each agent

for i, agent in enumerate(eg1.agent_list):
	agent.domain = domains[i]
	agent.value = random.choice(agent.domain)

import pdb;pdb.set_trace()