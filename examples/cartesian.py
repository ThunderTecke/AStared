# This example describe how to use AStared package with a cartesian system in two-dimension

from AStared.AStared import Node, AStar

# Define the heuristic function that estimate the remaining distance
# This function needs to return a number to estimate the remaining distance to the end node
# For example in a cartesian system, this function can used pythagoras theorems
# In this case the square root doesn't matter, so it can be ignored to decrease calculation time.
def heuristic(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    return  (x1 - x2)**2 + (y1 - y2)**2

# Maps, 1 => wall, 0 => valid path
map = [[0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

# Get neighbours in the map
# This function needs to get node's coordinate and return a list of Node. Coordinates are not used inside the A* algorithm, so it can be anything you want.
# It's your work to define an heuristic function that can use these coordinates.
# Neighbours are the node that can be reached with only 1 step
# For example in cartesian system, it can be the next node in -x, +x, -y and +y. And, if you want, the nodes in diagonal
# Or it can be the movement of the knight on a chessboard
def neighbours(coords):
    neighbours = []

    for xOffset, yOffset in [(+1, 0), (0, +1), (-1, 0), (0, -1)]:
        x, y = coords

        # Check if new coords are outside the map
        if ((y + yOffset) < 0) or ((y + yOffset) >= len(map)):
            continue

        if ((x + xOffset) < 0) or ((x + xOffset) >= len(map[y + yOffset])):
            continue

        # Check if new coords are in a wall
        if map[y][x] == 1:
            continue

        neighbours.append(Node((x + xOffset, y + yOffset)))

    return neighbours

# Call the A* algorithm, with start and end nodes, and also the functions created before
print(AStar(Node((0, 0)), Node((9, 0)), neighboursFunction=neighbours, heuristicFunction=heuristic))