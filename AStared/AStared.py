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