# BerraMihribanOrence_MetroSimulation.py
 Ending Project For Akbank Python - Intro to AI Bootcamp, Metro Simulation

![Image](https://github.com/user-attachments/assets/667f5d9b-1bb5-4162-9095-86a705bcbdc1)

## A functional Metro Simulation project that is designed for finding the shortest path while using the least amount of transfers in subway by implementing BFS (Breadth First Research) and A* algorithms


This project is desgined and built for as an ending project for Akbank Bootcamp called Introduction to Artificial Intelligence(AI) and Introduction to Python. Every part of this project shows how to do the following:

1.Create a subway simulation with using python and algorithm structures

2.Automatically find the shortest path between two stations using the least amount of transfers


# Why it has a hybrid approach

## A) BFS (Breadth First Research) to determine transfer-minimal paths

BFS algorithm keywords:

1. Traversal, BFS explores nodes level by level.
2. Queue, It uses a queue for order processing.
3. Shortest Path, It finds the shortest path in unweighted graphs.
4. Neighbors, It visits all adjacent nodes before moving deeper.
5. FIFO, Nodes are processed in a first-in, first-out manner.
6. Graph, Works on trees, grids, and general graphs.
7. Unweighted, Guarantees the fewest edges to a destination.
8. Complexity, Runs in O(V + E) time.
9. Cycle, Detects cycles in an undirected graph.
10. Connected, Finds all reachable nodes from a source.

## How does it work:

The BFS (Breadth-First Search) algorithm explores a graph level by level using a queue (FIFO order). It starts from the source node, visiting all adjacent (neighbor) nodes before moving deeper. BFS ensures the shortest path in an unweighted graph by always expanding the earliest discovered nodes first. The algorithm marks visited nodes to avoid cycles and redundant processing. It continues until it either finds the goal node or explores all possible paths. With a time complexity of O(V + E), BFS is useful for shortest pathfinding, connected components detection, and cycle detection in undirected graphs.

## B) A* for fine-tuning shortest travel time

A* algorithm keywords:

1. Heuristic, A* uses a heuristic to guide the search.
2. Cost, It calculates the total cost as g(n) + h(n).
3. Priority Queue, Nodes are processed based on priority.
4. Shortest Path, Finds the most efficient route in weighted graphs.
5. Exploration, Expands the lowest-cost node first.
6. Grid, Commonly used for pathfinding in maps.
7. Efficiency, Faster than Dijkstra algorithm in many cases.
8. Obstacles, Can navigate around barriers efficiently.
9. Waypoints, Finds optimal paths through multiple points.
10. Flexibility, Adapts to different heuristics for accuracy.

## How does it work:

The A* algorithm finds the shortest path by evaluating nodes based on their total cost, f(n) = g(n) + h(n), where g(n) is the cost from the start node and h(n) is the estimated cost to the goal (heuristic). It starts by adding the initial node to a priority queue, selecting the node with the lowest f(n), and expanding its neighbors. If a better path is found, it updates g(n) and recalculates f(n). The algorithm continues exploring the most promising routes using h(n) until it reaches the goal, then reconstructs the shortest path through backtracking.


## User Instructions - How to Install

The easiest way to see how this works here is the shortest version

1. Clone this repository
2. Go into repository
3. Set up a 
4. Install with
5. Run


## How to Tweak This Project For Your own Uses

Since this is an example project, I'd encourage you to clone and rename this project to add new improvements.


## Find a Bug?

If you found an issue or would like to submit an improvement please submit an issue using the issues tab above. If you would  like to submit a PR with a fix, reference the issue you created.


## Known Issues

This project is still ongoing and hasnt been completed yet. This is coming soon!


## Visual 

Example visual of the subway path

![Image](https://github.com/user-attachments/assets/566ef702-0139-4ac8-a9f5-1d20e8765173)
