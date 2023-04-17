class Node:
    def __init__(self, coords: tuple, parent = None) -> None:
        self.parent = parent
        self.coords = coords

        self.g = 0
        self.h = 0
    
    def f(self) -> float:
        return self.g + self.h
    
    def __eq__(self, __value: object) -> bool:
        #print(f"{self.coords} == {__value.coords} : {isinstance(__value, Node) and (self.coords == __value.coords)}")
        return isinstance(__value, Node) and (self.coords == __value.coords)

    def __ne__(self, __value: object) -> bool:
        return not self == __value
        

def AStar(startNode: Node, endNode: Node, neighboursFunction, heuristicFunction):
    openedNodes = [startNode]
    closedNodes = []

    while len(openedNodes) > 0:
        # Get the node with the best score (smallest)
        currentNode = openedNodes[0]
        currentIndex = 0

        for index, item in enumerate(openedNodes):
            if item.f() < currentNode.f():
                currentNode = item
                currentIndex = index
        
        # Close the node selected
        openedNodes.pop(currentIndex)
        closedNodes.append(currentNode)

        # Check if the node is the end node
        if currentNode == endNode:
            path = []
            current = currentNode

            while current is not None:
                path.append(current.coords)
                current = current.parent
            
            return path[::-1]

        # Check neighbours and calculate score
        for neighbour in neighboursFunction(currentNode.coords):
            if not isinstance(neighbour, Node):
                raise Exception("the neighboursFunction must return a list of Node")
            
            # Check if neighbour is not in closed nodes list
            find = False
            for closed in closedNodes:
                if neighbour == closed:
                    find = True
                    break
            
            if find:
                continue
            
            # Calculate node score
            neighbour.g = currentNode.g + 1
            neighbour.h = heuristicFunction(neighbour.coords, endNode.coords)

            # Assign parent
            neighbour.parent = currentNode

            # Check if node is qlreqdy in opened node, update it if the score is better
            find = False
            for index, opened in enumerate(openedNodes):
                if (neighbour == opened):
                    if (neighbour.g < opened.g):
                        openedNodes[index] = neighbour

                    find = True
                    break
            
            if find:
                continue
            
            openedNodes.append(neighbour)

if __name__=="__main__":
    def heuristic(coord1, coord2):
        q1, r1 = coord1
        q2, r2 = coord2

        return  (abs(q1 - q2) + abs(q1 + r1 - q2 - r2) + abs(r1 - r2)) / 2

    map = [     [0,0,0,0,0,0],
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