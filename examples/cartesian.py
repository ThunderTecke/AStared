from AStared.AStared import Node, AStar

def heuristic(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    return  (x1 - x2)**2 + (y1 - y2)**2

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

def neighbours(coords):
    neighbours = []

    for xOffset, yOffset in [(+1, 0), (0, +1), (-1, 0), (0, -1)]:
        x, y = coords

        # Check if new coords qre outside the map
        if ((y + yOffset) < 0) or ((y + yOffset) >= len(map)):
            continue

        if ((x + xOffset) < 0) or ((x + xOffset) >= len(map[y + yOffset])):
            continue

        if map[y][x] == 1:
            continue

        neighbours.append(Node((x + xOffset, y + yOffset)))

    return neighbours

print(AStar(Node((0, 0)), Node((9, 0)), neighboursFunction=neighbours, heuristicFunction=heuristic))