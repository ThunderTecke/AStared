from AStared.AStared import Node, AStar

def heuristic(coord1, coord2):
    q1, r1 = coord1
    q2, r2 = coord2

    return  (abs(q1 - q2) + abs(q1 + r1 - q2 - r2) + abs(r1 - r2)) / 2

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

def neighbours(coords):
    neighbours = []

    for qOffset, rOffset in [(+1, 0), (0, +1), (-1, +1), (-1, 0), (0, -1), (+1, -1)]:
        newQ = coords[0] + qOffset
        newR = coords[1] + rOffset

        if newQ < -5 or newQ > 5:
            continue
        
        if newR < -5 or newR > 5:
            continue

        x, y = AxialToMap(newQ, newR)

        if map[y][x] == 1:
            continue

        neighbours.append(Node((newQ, newR)))
    
    return neighbours

print(AStar(Node((0, 0)), Node((+5, -5)), neighboursFunction=neighbours, heuristicFunction=heuristic))