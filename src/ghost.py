from math import sqrt
import pygame
from vectormath import Vector2 as Vector
import src.display as d
from src.node import Node, MobileNode
from src.a_star import a_star
import time


class Ghost(object):
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.vel = Vector(3, 0)
        self.speed = 3
        self.width = 2 * d.GRID
        self.color = (255, 0, 0)
        self.node = MobileNode(x + d.GRID, y + d.GRID)
        self.path_to_pacman = []
        self.pacman = None

    def render(self, surface):
        pygame.draw.ellipse(surface, self.color, (self.pos.x + 4, self.pos.y + 4, self.width - 8, self.width - 8))
        self.draw_path(surface)

    def update(self, pacman):
        self.pos += self.vel
        self.pacman = pacman
        self.node.x = self.pos.x + d.GRID
        self.node.y = self.pos.y + d.GRID

    def eat_pacman(self) -> bool:  # todo collision check needs a change
        if self.pos.x == self.pacman.pos.x and self.pos.y == self.pacman.pos.y:
            return True
        return False

    def catch_pacman(self, nodes):
        self.node.find_neighbors2(nodes, self.vel)
        print(self.node.neighbors)
        start = self.node
        goal = self.closest_node_to_pacman(nodes)
        self.path_to_pacman = a_star(start, goal)
        # print(self.path_to_pacman)
        self.node.neighbors.clear()

        self.go_to_node(self.path_to_pacman[1])

        # if self.node.x == nodes[37].x and self.node.y == nodes[37].y:
        #     print(self.vel)
        #     time.sleep(6)

    def draw_path(self, surface):
        path = self.path_to_pacman
        pygame.draw.line(surface, self.color, (self.pos.x + d.GRID, self.pos.y + d.GRID), (path[0].x, path[0].y), 3)
        for i in range(len(path) - 1):
            pygame.draw.line(surface, self.color, (path[i].x, path[i].y), (path[i + 1].x, path[i + 1].y), 3)
        pygame.draw.line(surface, self.color, (path[-1].x, path[-1].y), (self.pacman.pos.x + d.GRID, self.pacman.pos.y + d.GRID), 3)

    def closest_node_to_pacman(self, nodes) -> Node:
        possible_nodes = []
        for node in nodes:
            if node.x - 3 <= self.pacman.pos.x + d.GRID <= node.x + 3 or node.y - 3 <= self.pacman.pos.y + d.GRID <= node.y + 3:
                possible_nodes.append(node)

        closest_node = possible_nodes[0]
        for node in possible_nodes:
            dist = sqrt((self.pacman.pos.x - node.x) ** 2 + (self.pacman.pos.y - node.y) ** 2)
            if dist < sqrt((self.pacman.pos.x - closest_node.x) ** 2 + (self.pacman.pos.y - closest_node.y) ** 2):
                closest_node = node

        return closest_node

    def go_to_node(self, node):
        assert self.node.x == node.x or self.node.y == node.y, "ghost: ({}, {}), node: ({}, {})".format(self.node.y, self.node.y, node.x, node.y)
        if self.node.y == node.y:
            if self.node.x != node.x:  # if not arrived at that node
                if self.node.x < node.x:
                    print("node is on the right")
                    self.vel.x = self.speed
                else:
                    print("node is on the left")
                    self.vel.x = -self.speed
                self.vel.y = 0
            else:
                print("arrived at node")
        else:
            if self.node.y != node.y:  # if not arrived at that node
                if self.node.y < node.y:
                    print("node is downwards")
                    self.vel.y = self.speed
                else:
                    print("node is upwards")
                    self.vel.y = -self.speed
                self.vel.x = 0
            else:
                print("arrived at node")
