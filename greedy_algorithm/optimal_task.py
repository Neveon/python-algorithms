# Given a list of numbers with each number corresponding to a duration of a task
# assign each item to a 'worker' with each 'worker' taking 2 items/tasks maximum
# and contain the minimum max duration to wait

# EXAMPLE
# [6, 3, 2, 7, 5, 5]
# worker 1 (6, 3) 
# worker 2 (2, 7)
# worker 3 (5, 5)
# max(6+3, 2+7, 5+5) = 10 (smallest number generated)

# Greedy approach
# pair the longest task with the shortest task
# [2, 3, 5, 5, 6, 7]
# (2,7), (3,6), (5,5)
# Time complexity is O(n log n) due to sorting

tasks = [1, 6, 3, 5, 2, 7]

def optimal_task(tasks):
  tasks = sorted(tasks)
  for i in range(len(tasks) // 2):
    # ~ (not) -> ~0 = -1  ~1 = -2
    print(tasks[i], tasks[~i])
  
optimal_task(tasks)

# What is a greedy algorithm? What makes this a greedy algorithm?

# A greedy algorithm is an algorithmic strategy that makes the best optimal choice at
# each small stage with the goal of this eventually leading to a globally optimum
# solution. This means that the algorithm picks the best solution at the moment
# without regard for consequences. It picks the best immediate output, but does
# not consider the big picture, hence it is considered greedy.