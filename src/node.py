import pygame
import src.display as d


class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, surface):
        pygame.draw.circle(surface, (0, 0, 255), (self.x, self.y), 8)


def make_nodes() -> tuple:
    node1 = Node(2 * d.GRID, 2 * d.GRID)
    node2 = Node(7 * d.GRID, 2 * d.GRID)
    node3 = Node(13 * d.GRID, 2 * d.GRID)
    node4 = Node(16 * d.GRID, 2 * d.GRID)
    node5 = Node(22 * d.GRID, 2 * d.GRID)
    node6 = Node(27 * d.GRID, 2 * d.GRID)
    node7 = Node(2 * d.GRID, 6 * d.GRID)
    node8 = Node(7 * d.GRID, 6 * d.GRID)
    node9 = Node(10 * d.GRID, 6 * d.GRID)
    node10 = Node(13 * d.GRID, 6 * d.GRID)
    node11 = Node(16 * d.GRID, 6 * d.GRID)
    node12 = Node(19 * d.GRID, 6 * d.GRID)
    node13 = Node(22 * d.GRID, 6 * d.GRID)
    node14 = Node(27 * d.GRID, 6 * d.GRID)
    node15 = Node(2 * d.GRID, 9 * d.GRID)
    node16 = Node(7 * d.GRID, 9 * d.GRID)
    node17 = Node(10 * d.GRID, 9 * d.GRID)
    node18 = Node(13 * d.GRID, 9 * d.GRID)
    node19 = Node(16 * d.GRID, 9 * d.GRID)
    node20 = Node(19 * d.GRID, 9 * d.GRID)
    node21 = Node(22 * d.GRID, 9 * d.GRID)
    node22 = Node(27 * d.GRID, 9 * d.GRID)
    node23 = Node(10 * d.GRID, 12 * d.GRID)
    node24 = Node(13 * d.GRID, 12 * d.GRID)
    node25 = Node(16 * d.GRID, 12 * d.GRID)
    node26 = Node(19 * d.GRID, 12 * d.GRID)
    node27 = Node(7 * d.GRID, 15 * d.GRID)
    node28 = Node(10 * d.GRID, 15 * d.GRID)
    node29 = Node(19 * d.GRID, 15 * d.GRID)
    node30 = Node(22 * d.GRID, 15 * d.GRID)
    node31 = Node(10 * d.GRID, 18 * d.GRID)
    node32 = Node(19 * d.GRID, 18 * d.GRID)
    node33 = Node(2 * d.GRID, 21 * d.GRID)
    node34 = Node(7 * d.GRID, 21 * d.GRID)
    node35 = Node(10 * d.GRID, 21 * d.GRID)
    node36 = Node(13 * d.GRID, 21 * d.GRID)
    node37 = Node(16 * d.GRID, 21 * d.GRID)
    node38 = Node(19 * d.GRID, 21 * d.GRID)
    node39 = Node(22 * d.GRID, 21 * d.GRID)
    node40 = Node(27 * d.GRID, 21 * d.GRID)
    node41 = Node(2 * d.GRID, 24 * d.GRID)
    node42 = Node(4 * d.GRID, 24 * d.GRID)
    node43 = Node(7 * d.GRID, 24 * d.GRID)
    node44 = Node(10 * d.GRID, 24 * d.GRID)
    node45 = Node(13 * d.GRID, 24 * d.GRID)
    node46 = Node(16 * d.GRID, 24 * d.GRID)
    node47 = Node(19 * d.GRID, 24 * d.GRID)
    node48 = Node(22 * d.GRID, 24 * d.GRID)
    node49 = Node(25 * d.GRID, 24 * d.GRID)
    node50 = Node(27 * d.GRID, 24 * d.GRID)
    node51 = Node(2 * d.GRID, 27 * d.GRID)
    node52 = Node(4 * d.GRID, 27 * d.GRID)
    node53 = Node(7 * d.GRID, 27 * d.GRID)
    node54 = Node(10 * d.GRID, 27 * d.GRID)
    node55 = Node(13 * d.GRID, 27 * d.GRID)
    node56 = Node(16 * d.GRID, 27 * d.GRID)
    node57 = Node(19 * d.GRID, 27 * d.GRID)
    node58 = Node(22 * d.GRID, 27 * d.GRID)
    node59 = Node(25 * d.GRID, 27 * d.GRID)
    node60 = Node(27 * d.GRID, 27 * d.GRID)
    node61 = Node(2 * d.GRID, 30 * d.GRID)
    node62 = Node(13 * d.GRID, 30 * d.GRID)
    node63 = Node(16 * d.GRID, 30 * d.GRID)
    node64 = Node(27 * d.GRID, 30 * d.GRID)
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
        node.y += 2 * d.GRID
    return nodes
