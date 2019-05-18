from math import sqrt
from node import Node


def find_node_min_f(nodes) -> Node:
    node_min_f = nodes[0]
    for node in nodes:
        if node.f < node_min_f.f:
            node_min_f = node
    return node_min_f


def h(node: Node, end: Node) -> float:
    return abs(node.x - end.x) + abs(node.y - end.y)


def reconstruct_path(came_from: dict, current: Node) -> list:
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return list(reversed(total_path))


def a_star(st: Node, en: Node):
    open_list = []
    closed_list = []
    came_from = {}

    start = st
    end = en
    open_list.append(start)
    start.g = 0
    start.f = h(start, end)

    while open_list:
        current = find_node_min_f(open_list)

        if current == end:
            return reconstruct_path(came_from, current)

        open_list.remove(current)
        closed_list.append(current)

        neighbors = current.neighbors.values()

        for neighbor in neighbors:
            if neighbor in closed_list:
                continue

            tentative_g = current.g + sqrt((neighbor.x - current.x) ** 2 + (neighbor.y - current.y) ** 2)

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g >= neighbor.g:
                continue

            came_from[neighbor] = current
            neighbor.g = tentative_g
            neighbor.f = neighbor.g + h(neighbor, end)
