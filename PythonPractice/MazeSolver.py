import GridFunctions
import heapq
from queue import Queue, LifoQueue as stack

class Node:
    def __init__(self, value, par, search_type):
        self.value = value
        self.parent = par
        self.g = 0  # path cost
        self.h = 0  # heuristic cost
        self.f = self.g + self.h  # A*
        self.priority = self.h if search_type else self.f

    def __lt__(self, other):
        return self.priority < other.priority

    def get_neighbors(self, grid):
        v = self.value

        up = [v[0]-1, v[1]]
        down = [v[0]+1, v[1]]
        left = [v[0], v[1]-1]
        right = [v[0], v[1]+1]

        neighbors = []

        if grid[up[0]][up[1]] != 0:
            neighbors.append(up)
        if grid[down[0]][down[1]] != 0:
            neighbors.append(down)
        if grid[left[0]][left[1]] != 0:
            neighbors.append(left)
        if grid[right[0]][right[1]] != 0:
            neighbors.append(right)

        return neighbors

def main():
    filename = "grid.txt"
    grid = GridFunctions.readGrid(filename)
    start = [1, 1]
    goal = [5, 6]
    print("Please enter a search type. 0 for A*. 1 for Greedy. /n")
    search_type = bool(input())

    path = informed_search(grid, start, goal, search_type)
    print("Hi")
    path_filename = "path.txt"

    if path is None:
        print("No path was found.")
    else:
        GridFunctions.outputGrid(grid, start, goal, path)
        print("Hello")


def expand_node(grid, node, open_list, closed_list, goal, search_type):
    def in_explored(loc, q):
        return loc in [each.value for each in q]

    def in_visited(loc, l):
        return loc in [each.value for each in l]

    for each in node.get_neighbors(grid):
        if not in_visited(each, closed_list) and not in_explored(each, open_list):
            temp_node = Node(each, node, search_type)
            temp_node.g = node.g + grid[each[0]][each[1]]
            temp_node.h = heuristic(node.value, goal)
            temp_node.f = node.g + node.h
            heapq.heappush(open_list, temp_node)


def informed_search(grid, start, goal, search_type):
    current_loc = Node(start, '', search_type)
    current_loc.g = 0
    # print(current_loc)
    current_loc.h = heuristic(current_loc.value, goal)
    closed_list, path = [], []
    open_list = []
    heapq.heappush(open_list, current_loc)

    return search(grid, current_loc, goal, open_list, closed_list, path, search_type)

def heuristic(current_loc, goal):
    manhattan_distance = abs(current_loc[0] - goal[0]) + abs(current_loc[1] - goal[1])
    return manhattan_distance

def search(grid, node, goal, open_list, closed_list, path, search_type):
    closed_list.append(node)
    print(node.value)

    if node.value == goal:
        return set_path(node, path)
    else:
        expand_node(grid, node, open_list, closed_list, goal, search_type)

        if open_list:
            return None
        else:
            return search(grid, open_list.get(), goal, open_list, closed_list, path, search_type)

def set_path(node, path):
    path.append(node.value)
    if node.parent == '':
        return path
    else:
        return set_path(node.parent, path)

main()