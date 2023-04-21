# This example describe how to use AStared package with a hexagonal grid
# You can find more information about using hexagonal grid here : https://www.redblobgames.com/grids/hexagons/

from AStared.AStared import Node, AStar

# Define the heuristic function that estimate the remaining distance
# This function needs to return a number to estimate the remaining distance to the end node
# In this example I use the function describe on the web page given above.
def heuristic(coord1, coord2):
    q1, r1 = coord1
    q2, r2 = coord2

    return  (abs(q1 - q2) + abs(q1 + r1 - q2 - r2) + abs(r1 - r2)) / 2

# Maps, 1 => wall, 0 => valid path
map = [      [0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
           [0,0,1,1,1,1,0,0],
          [0,0,1,0,0,0,1,0,0],
         [0,0,1,0,1,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
         [0,0,1,0,1,1,0,1,0,0],
          [0,0,1,0,0,0,1,0,0],
           [0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0],
             [0,0,0,0,0,0]]

# This function is used to translate axial coordinate to indexes for the map
def AxialToMap(q, r):
    x = y = 0
    match (r):
        case -5:
            y = 0
            x = q

        case -4:
            y = 1
            x = q + 1

        case -3:
            y = 2
            x = q + 2

        case -2:
            y = 3
            x = q + 3

        case -1:
            y = 4
            x = q + 4

        case 0:
            y = 5
            x = q + 5

        case 1:
            y = 6
            x = q + 5

        case 2:
            y = 7
            x = q + 5

        case 3:
            y = 8
            x = q + 5

        case 4:
            y = 9
            x = q + 5

        case 5:
            y = 10
            x = q + 5
    
    return x, y

# Get neighbours in the map
# This function needs to get node's coordinate and return a list of Node. Coordinates are not used inside the A* algorithm, so it can be anything you want.
# It's your work to define an heuristic function that can use these coordinates.
# Neighbours are the node that can be reached with only 1 step.
# In this case in a hexagonal grid, it can be the 6 nodes around a node.
def neighbours(coords):
    neighbours = []

    # Iterate through the possible movements
    for qOffset, rOffset in [(+1, 0), (0, +1), (-1, +1), (-1, 0), (0, -1), (+1, -1)]:
        newQ = coords[0] + qOffset
        newR = coords[1] + rOffset

        # Check if the new coords are outside the map
        if newQ < -5 or newQ > 5:
            continue
        
        if newR < -5 or newR > 5:
            continue

        # Check if new coord ar in a wall
        x, y = AxialToMap(newQ, newR)

        if map[y][x] == 1:
            continue

        neighbours.append(Node((newQ, newR)))
    
    return neighbours

# Call A* algorithm; with start and end nodes, and also the function created before
print(AStar(Node((0, 0)), Node((+5, -5)), neighboursFunction=neighbours, heuristicFunction=heuristic))