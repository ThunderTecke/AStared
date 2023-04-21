from typing import Callable

class Node:
    """
    Node class use to store coordinates, scores and parent node

    Parameters
    ----------
    coords: tuple
        `coords` store the coordinate of the node. It can be anything, the A* algorithm don't use it directly.

    parent: Node
        `parent` is used to store the incoming path to the node. You don't have to set it manually, the algorithm do it.
    
    Attributes
    ----------
    parent: Node
        Same as `parent` in parameters section.
    
    coords: tuple
        Same as `coords` in parameters section.
    
    g: float
        Is the distance made since the beginning.
    
    h: float
        Is the heuristic estimation distance to the end node.
        It calculate from heuristic function given to `AStar` function.
    
    Methods
    -------
    f()
        Return the total score "g + h"
    """
    def __init__(self, coords: tuple, parent = None) -> None:
        self.parent = parent
        self.coords = coords

        self.g = 0
        self.h = 0
    
    def f(self) -> float:
        """
        Return the total score "g + h"

        Returns
        -------
        float
            The total score
        """
        return self.g + self.h
    
    def __eq__(self, __value: object) -> bool:
        #print(f"{self.coords} == {__value.coords} : {isinstance(__value, Node) and (self.coords == __value.coords)}")
        return isinstance(__value, Node) and (self.coords == __value.coords)

    def __ne__(self, __value: object) -> bool:
        return not self == __value
        

def AStar(startNode: Node, endNode: Node, neighboursFunction: Callable[[tuple], list[Node]], heuristicFunction: Callable[[tuple, tuple], float]):
    """
    The main function, it calls the A* algorithm. It needs 2 function, one for neighbours and one other for heuristic estimation.
    The neighbours function needs to get node's coordinate and return a list of node that can be reached with only 1 step.
    Coordinate can be anything. These coordinates are never used directly by the A* algorithm.

    Parameters
    ----------
    startNode: Node
        Is the start of the path finding
    
    endNode: Node
        Is the goal of the path finding
    
    neighboursFunction: function
        It used to pass the neighbours function to the A* algorithm. 
        This function needs to take the coordinate in argument, and return a list of node that can be reached with one step.
    
    heuristicFunction: function
        It used to pass the heuristic estimation function to the A* algorithm.
        This function needs to take the coordinates of the nodes A and B, and return the heuristic estimated distance between them.
    
    Returns
    -------
    list
        Return a list of coordinates. The first elements is the start node coordinate, and the last the end node coordinate.
    """
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