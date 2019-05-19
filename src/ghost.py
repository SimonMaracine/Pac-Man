from math import sqrt
import pygame
from vectormath import Vector2 as Vector
import src.display as d
from src.node import Node
from src.a_star import a_star


class Ghost(object):
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)
        self.width = 2 * d.GRID
        self.color = (255, 0, 0)
        self.path_to_pacman = None
        self.pacman = None

    def render(self, surface):
        pygame.draw.ellipse(surface, self.color, (self.pos.x + 4, self.pos.y + 4, self.width - 8, self.width - 8))
        self.draw_path(surface)

    def update(self, pacman):
        self.pacman = pacman

    def eat_pacman(self) -> bool:
        if self.pos.x == self.pacman.pos.x and self.pos.y == self.pacman.pos.y:
            return True
        return False

    def catch_pacman(self, nodes):
        start = self.find_closest_node(nodes)
        goal = self.closest_node_to_pacman(nodes)
        self.path_to_pacman = a_star(start, goal)
        print(self.path_to_pacman)

    def draw_path(self, surface):
        path = self.path_to_pacman
        pygame.draw.line(surface, self.color, (self.pos.x + d.GRID, self.pos.y + d.GRID), (path[0].x, path[0].y), 3)
        for i in range(len(path) - 1):
            pygame.draw.line(surface, self.color, (path[i].x, path[i].y), (path[i + 1].x, path[i + 1].y), 3)
        pygame.draw.line(surface, self.color, (path[-1].x, path[-1].y), (self.pacman.pos.x + d.GRID, self.pacman.pos.y + d.GRID), 3)

    def find_closest_node(self, nodes) -> Node:
        possible_nodes = []
        for node in nodes:
            if node.x - 3 <= self.pos.x + d.GRID <= node.x + 3 or node.y - 3 <= self.pos.y + d.GRID <= node.y + 3:
                possible_nodes.append(node)
        # print(possible_nodes)

        closest_node = possible_nodes[0]
        for node in possible_nodes:
            dist = sqrt((self.pos.x - node.x) ** 2 + (self.pos.y - node.y) ** 2)
            if dist < sqrt((self.pos.x - closest_node.x) ** 2 + (self.pos.y - closest_node.y) ** 2):
                closest_node = node

        return closest_node

    def closest_node_to_pacman(self, nodes) -> Node:
        possible_nodes = []
        for node in nodes:
            if node.x - 3 <= self.pacman.pos.x + d.GRID <= node.x + 3 or node.y - 3 <= self.pacman.pos.y + d.GRID <= node.y + 3:
                possible_nodes.append(node)
        # print(possible_nodes)

        closest_node = possible_nodes[0]
        for node in possible_nodes:
            dist = sqrt((self.pacman.pos.x - node.x) ** 2 + (self.pacman.pos.y - node.y) ** 2)
            if dist < sqrt((self.pacman.pos.x - closest_node.x) ** 2 + (self.pacman.pos.y - closest_node.y) ** 2):
                closest_node = node

        return closest_node
