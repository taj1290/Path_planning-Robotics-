# Path_planning-Robotics-
Path planning algorithms in Python

# A* Algorithm
A* (A-star) is a popular pathfinding and graph traversal algorithm used in various applications like navigation, robotics, and AI. It combines the strengths of Dijkstra's algorithm and greedy best-first search by considering both the cost to reach the current node (known as g(n)) and the estimated cost to reach the goal from that node (known as h(n)), which is derived from a heuristic. 
A* is optimal and complete, meaning it guarantees finding the shortest path if one exists, given an admissible heuristic (one that never overestimates the cost).

# Hybrid A* Algorithm
Hybrid A* is an extension of the A* algorithm, particularly designed for continuous state spaces, often used in robotics for pathfinding in environments where the robot's movement is non-holonomic (i.e., it has constraints like turning radius). Unlike standard A*, which plans in a discrete grid, Hybrid A* considers the continuous nature of the environment and generates smoother paths. It incorporates motion models and sometimes uses a post-processing step, like curve fitting, to refine the path.

# Breadth-First Search (BFS)
BFS is an uninformed search algorithm that explores all possible nodes at the present depth level before moving on to nodes at the next depth level. It is implemented using a queue and is particularly effective for finding the shortest path in unweighted graphs. BFS guarantees finding the shortest path if all edges have the same weight, but it is not optimal for weighted graphs like A*.

These algorithms have their unique strengths and applications, with A* being widely used due to its balance of efficiency and accuracy, Hybrid A* for robotics in complex environments, and BFS for simple, unweighted pathfinding tasks.



https://github.com/user-attachments/assets/20186f24-4eb5-47fe-84d5-49d4828a393e

