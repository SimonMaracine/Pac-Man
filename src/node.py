from math import inf
import pygame
import src.display as d


class Node(object):
    def __init__(self, x, y, neighbor_dirs: tuple):
        self.x = x
        self.y = y
        self.neighbor_dirs = neighbor_dirs
        self.neighbors = {}
        self.f = inf
        self.g = inf

    def __repr__(self) -> str:
        return "Node({}, {})".format(self.x // d.GRID, self.y // d.GRID)

    def render(self, surface):
        pygame.draw.circle(surface, (0, 0, 255), (self.x, self.y), 8)

    def find_neighbors(self, nodes: tuple, dirs: tuple):
        if not dirs:
            dirs = self.neighbor_dirs

        for dir in dirs:
            if dir == "u":
                y = self.y
                found_neighbor = False
                c = 0
                while not found_neighbor:
                    c += 1
                    if c > 11:
                        break
                    y -= d.GRID
                    for node in nodes:
                        if node.x == self.x and node.y < self.y:
                            if y - d.GRID <= node.y <= y + d.GRID:
                                self.neighbors["u"] = node
                                found_neighbor = True
                                break
            elif dir == "l":
                x = self.x
                found_neighbor = False
                c = 0
                while not found_neighbor:
                    c += 1
                    if c > 11:
                        break
                    x -= d.GRID
                    for node in nodes:
                        if node.y == self.y and node.x < self.x:
                            if x - d.GRID <= node.x <= x + d.GRID:
                                self.neighbors["l"] = node
                                found_neighbor = True
                                break
            elif dir == "d":
                y = self.y
                found_neighbor = False
                c = 0
                while not found_neighbor:
                    c += 1
                    if c > 11:
                        break
                    y += d.GRID
                    for node in nodes:
                        if node.x == self.x and node.y > self.y:
                            if y - d.GRID <= node.y <= y + d.GRID:
                                self.neighbors["d"] = node
                                found_neighbor = True
                                break
            elif dir == "r":
                x = self.x
                found_neighbor = False
                c = 0
                while not found_neighbor:
                    c += 1
                    if c > 11:
                        break
                    x += d.GRID
                    for node in nodes:
                        if node.y == self.y and node.x > self.x:
                            if x - d.GRID <= node.x <= x + d.GRID:
                                self.neighbors["r"] = node
                                found_neighbor = True
                                break


class MobileNode(Node):
    def __init__(self, x, y):
        super().__init__(x, y, ())

    def find_neighbors2(self, nodes: tuple, entity_dir):
        if entity_dir.x != 0:
            for node in nodes:
                if self.x == node.x and self.y == node.y:
                    dirs = node.neighbor_dirs
                    super().find_neighbors(nodes, dirs)
                    break
            else:
                # print("search x")
                super().find_neighbors(nodes, ("l", "r"))
        elif entity_dir.y != 0:
            for node in nodes:
                if self.x == node.x and self.y == node.y:
                    dirs = node.neighbor_dirs
                    super().find_neighbors(nodes, dirs)
                    break
            else:
                # print("search y")
                super().find_neighbors(nodes, ("u", "d"))
        else:
            for node in nodes:
                if self.x == node.x and self.y == node.y:
                    dirs = node.neighbor_dirs
                    super().find_neighbors(nodes, dirs)
                    break


def make_nodes() -> tuple:
    node1 = Node(2 * d.GRID, 2 * d.GRID, ("d", "r"))
    node2 = Node(7 * d.GRID, 2 * d.GRID, ("d", "r", "l"))
    node3 = Node(13 * d.GRID, 2 * d.GRID, ("d", "l"))
    node4 = Node(16 * d.GRID, 2 * d.GRID, ("d", "r"))
    node5 = Node(22 * d.GRID, 2 * d.GRID, ("d", "l", "r"))
    node6 = Node(27 * d.GRID, 2 * d.GRID, ("d", "l"))
    node7 = Node(2 * d.GRID, 6 * d.GRID, ("u", "d", "r"))
    node8 = Node(7 * d.GRID, 6 * d.GRID, ("u", "d", "l", "r"))
    node9 = Node(10 * d.GRID, 6 * d.GRID, ("l", "d", "r"))
    node10 = Node(13 * d.GRID, 6 * d.GRID, ("u", "l", "r"))
    node11 = Node(16 * d.GRID, 6 * d.GRID, ("u", "l", "r"))
    node12 = Node(19 * d.GRID, 6 * d.GRID, ("l", "d", "r"))
    node13 = Node(22 * d.GRID, 6 * d.GRID, ("u", "d", "l", "r"))
    node14 = Node(27 * d.GRID, 6 * d.GRID, ("u", "l", "d"))
    node15 = Node(2 * d.GRID, 9 * d.GRID, ("u", "r"))
    node16 = Node(7 * d.GRID, 9 * d.GRID, ("u", "l", "d"))
    node17 = Node(10 * d.GRID, 9 * d.GRID, ("u", "r"))
    node18 = Node(13 * d.GRID, 9 * d.GRID, ("l", "d"))
    node19 = Node(16 * d.GRID, 9 * d.GRID, ("d", "r"))
    node20 = Node(19 * d.GRID, 9 * d.GRID, ("u", "l"))
    node21 = Node(22 * d.GRID, 9 * d.GRID, ("u", "r"))
    node22 = Node(27 * d.GRID, 9 * d.GRID, ("u", "l"))
    node23 = Node(10 * d.GRID, 12 * d.GRID, ("d", "r"))
    node24 = Node(13 * d.GRID, 12 * d.GRID, ("u", "l", "r"))
    node25 = Node(16 * d.GRID, 12 * d.GRID, ("u", "l", "r"))
    node26 = Node(19 * d.GRID, 12 * d.GRID, ("l", "d"))
    node27 = Node(7 * d.GRID, 15 * d.GRID, ("u", "d", "r"))
    node28 = Node(10 * d.GRID, 15 * d.GRID, ("u", "l", "d"))
    node29 = Node(19 * d.GRID, 15 * d.GRID, ("u", "d", "r"))
    node30 = Node(22 * d.GRID, 15 * d.GRID, ("u", "d", "l"))
    node31 = Node(10 * d.GRID, 18 * d.GRID, ("u", "d", "r"))
    node32 = Node(19 * d.GRID, 18 * d.GRID, ("u", "d", "l"))
    node33 = Node(2 * d.GRID, 21 * d.GRID, ("d", "r"))
    node34 = Node(7 * d.GRID, 21 * d.GRID, ("u", "d", "l", "r"))
    node35 = Node(10 * d.GRID, 21 * d.GRID, ("u", "l", "r"))
    node36 = Node(13 * d.GRID, 21 * d.GRID, ("l", "d"))
    node37 = Node(16 * d.GRID, 21 * d.GRID, ("d", "r"))
    node38 = Node(19 * d.GRID, 21 * d.GRID, ("u", "l", "r"))
    node39 = Node(22 * d.GRID, 21 * d.GRID, ("u", "d", "l", "r"))
    node40 = Node(27 * d.GRID, 21 * d.GRID, ("l", "d"))
    node41 = Node(2 * d.GRID, 24 * d.GRID, ("u", "r"))
    node42 = Node(4 * d.GRID, 24 * d.GRID, ("l", "d"))
    node43 = Node(7 * d.GRID, 24 * d.GRID, ("u", "d", "r"))
    node44 = Node(10 * d.GRID, 24 * d.GRID, ("d", "l", "r"))
    node45 = Node(13 * d.GRID, 24 * d.GRID, ("u", "l", "r"))
    node46 = Node(16 * d.GRID, 24 * d.GRID, ("u", "l", "r"))
    node47 = Node(19 * d.GRID, 24 * d.GRID, ("d", "l", "r"))
    node48 = Node(22 * d.GRID, 24 * d.GRID, ("u", "d", "l"))
    node49 = Node(25 * d.GRID, 24 * d.GRID, ("d", "r"))
    node50 = Node(27 * d.GRID, 24 * d.GRID, ("u", "l"))
    node51 = Node(2 * d.GRID, 27 * d.GRID, ("d", "r"))
    node52 = Node(4 * d.GRID, 27 * d.GRID, ("u", "l", "r"))
    node53 = Node(7 * d.GRID, 27 * d.GRID, ("u", "l"))
    node54 = Node(10 * d.GRID, 27 * d.GRID, ("u", "r"))
    node55 = Node(13 * d.GRID, 27 * d.GRID, ("l", "d"))
    node56 = Node(16 * d.GRID, 27 * d.GRID, ('d', "r"))
    node57 = Node(19 * d.GRID, 27 * d.GRID, ("u", "l"))
    node58 = Node(22 * d.GRID, 27 * d.GRID, ("u", "r"))
    node59 = Node(25 * d.GRID, 27 * d.GRID, ("u", "r"))
    node60 = Node(27 * d.GRID, 27 * d.GRID, ("l", "d"))
    node61 = Node(2 * d.GRID, 30 * d.GRID, ("u", "r"))
    node62 = Node(13 * d.GRID, 30 * d.GRID, ("u", "l", "r"))
    node63 = Node(16 * d.GRID, 30 * d.GRID, ("u", "l", "r"))
    node64 = Node(27 * d.GRID, 30 * d.GRID, ("u", "l"))
    nodes = (
        node1, node2, node3, node4, node5, node6, node7, node8, node9, node10,
        node11, node12, node13, node14, node15, node16, node17, node18, node19, node20,
        node21, node22, node23, node24, node25, node26, node27, node28, node29, node30,
        node31, node32, node33, node34, node35, node36, node37, node38, node39, node40,
        node41, node42, node43, node44, node45, node46, node47, node48, node49, node50,
        node51, node52, node53, node54, node55, node56, node57, node58, node59, node60,
        node61, node62, node63, node64
    )
    for node in nodes:
        node.find_neighbors(nodes, ())
        # print(node.neighbors)
    for node in nodes:
        node.y += 2 * d.GRID
    return nodes
