# AStared
This package provide the A* algorithm for any type of coordinates.
You can find more information [here](https://en.wikipedia.org/wiki/A*_search_algorithm).

## Installation
```python3.11 -m pip install AStared```

## Usage
You can find examples [here](https://github.com/ThunderTecke/AStared/tree/main/examples).

In global lines, you must define 2 functions to interact with your coordinates. And then pass it to the function `AStar`

These function are :
- Heuristic estimation to the end node
- Neighbours giver, that return all valid neightbours that can be reached with only 1 step