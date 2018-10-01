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

print('\n')
print('EXAMPLE 1')
eg1.run_arc_consistency()

### Example 2:

## Setup: 

# Instantiate MAS with adjecency matrix

eg2 = mas.MAS(3, [[0,1,1],[1,0,1],[1,1,0]])

# Declare domains

domains = [['red'],['red', 'blue'], ['red', 'blue']]

# Assign domains, values and binary constraints for each agent

for agent in eg2.agent_list:
	agent.domain = domains[agent.id_number]
	agent.value = random.choice(agent.domain)
	agent.binary_constraints = [(agent.id_number, other_agent.id_number) for 
									other_agent in agent.neighbors]

print('\n')
print('EXAMPLE 2')
eg2.run_arc_consistency()


### Example 3:

## Setup: 

# Instantiate MAS with adjecency matrix

eg3 = mas.MAS(3, [[0,1,1],[1,0,1],[1,1,0]])

# Declare domains

domains = [['red', 'blue'],['red', 'blue'], ['red', 'blue']]

# Assign domains, values and binary constraints for each agent

for agent in eg3.agent_list:
	agent.domain = domains[agent.id_number]
	agent.value = random.choice(agent.domain)
	agent.binary_constraints = [(agent.id_number, other_agent.id_number) for 
									other_agent in agent.neighbors]

print('\n')
print('EXAMPLE 3')
eg3.run_arc_consistency()

### Example 4:

## Setup: 

# Instantiate MAS with adjecency matrix

eg4 = mas.MAS(3, [[0,1,1],[1,0,1],[1,1,0]])

# Declare domains

domains = [['red', 'blue', 'green'],['red', 'blue', 'green'], ['red', 'blue', 'green']]

# Assign domains, values and binary constraints for each agent

for agent in eg4.agent_list:
	agent.domain = domains[agent.id_number]
	agent.value = random.choice(agent.domain)
	agent.binary_constraints = [(agent.id_number, other_agent.id_number) for 
									other_agent in agent.neighbors]

print('\n')
print('EXAMPLE 4')
eg4.run_arc_consistency()