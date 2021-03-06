from copy import deepcopy
from math import sqrt
import pygame
from vectormath import Vector2 as Vector
import src.display as d


class PacMan(object):
    def __init__(self):
        self.pos = Vector(14 * d.GRID - d.GRID // 2, 25 * d.GRID)
        self.width = 2 * d.GRID
        self.speed = 3
        self.vel = Vector(0, 0)
        self.hit_wall = {"left": False, "right": False, "up": False, "down": False}
        self.next_vel = Vector(0, 0)
        self.can_move = {"x": True, "y": True}

    def render(self, surface):
        pygame.draw.ellipse(surface, (255, 255, 0), (self.pos.x + 3, self.pos.y + 3, self.width - 6, self.width - 6))
        # pygame.draw.ellipse(window, (255, 255, 0), (self.pos.x, self.pos.y, self.width, self.width))

        # draw the hitbox
        # pygame.draw.rect(window, (255, 0, 0), (self.pos.x, self.pos.y + 3, 5, self.width - 6), 1)  # left hitbox
        # pygame.draw.rect(window, (255, 0, 0), (self.pos.x + self.width - 5, self.pos.y + 3, 5, self.width - 6), 1)  # right hitbox
        # pygame.draw.rect(window, (255, 0, 0), (self.pos.x + 3, self.pos.y, self.width - 6, 5), 1)  # up hitbox
        # pygame.draw.rect(window, (255, 0, 0), (self.pos.x + 3, self.pos.y + self.width - 5, self.width - 6, 5), 1)  # down hitbox

    def update(self):
        self.pos += self.vel

        if self.pos.x < 0:
            self.can_move["y"] = False
            if self.pos.x < -self.width * 3:  # left tunnel
                self.pos.x = d.WIDTH
        elif self.pos.x > d.WIDTH:
            self.can_move["y"] = False
            if self.pos.x > d.WIDTH + self.width * 2:  # right tunnel
                self.pos.x = -self.width
        else:
            self.can_move["y"] = True

        for side in self.hit_wall:
            self.hit_wall[side] = False

    def change_dir(self, direction):
        if direction == "left":
            self.vel.x = -self.speed
            self.next_vel.x = -self.speed
            self.next_vel.y = 0
        elif direction == "right":
            self.vel.x = self.speed
            self.next_vel.x = self.speed
            self.next_vel.y = 0

        if self.can_move["y"]:
            if direction == "up":
                self.vel.y = -self.speed
                self.next_vel.y = -self.speed
                self.next_vel.x = 0
            elif direction == "down":
                self.vel.y = self.speed
                self.next_vel.y = self.speed
                self.next_vel.x = 0

    def collide(self, wall):
        if self.pos.x < wall.x + wall.width < self.pos.x + 5:
            if wall.y + wall.height > self.pos.y + 3 and wall.y < self.pos.y + self.width - 3:
                self.stop("left")
                self.hit_wall["left"] = True

        if self.pos.x + self.width > wall.x > self.pos.x - 5:
            if wall.y + wall.height > self.pos.y + 3 and wall.y < self.pos.y + self.width - 3:
                self.stop("right")
                self.hit_wall["right"] = True

        if self.pos.y < wall.y + wall.height < self.pos.y + 5:
            if self.pos.x + self.width - 3 > wall.x and self.pos.x + 3 < wall.x + wall.width:
                self.stop("up")
                self.hit_wall["up"] = True

        if self.pos.y + self.width > wall.y > self.pos.y + self.width - 5:
            if self.pos.x + self.width - 3 > wall.x and self.pos.x + 3 < wall.x + wall.width:
                self.stop("down")
                self.hit_wall["down"] = True

    def stop(self, side):
        if side == "left":
            self.vel.x = 0
            self.pos.x += self.speed
            self.next_vel.y = 0
        elif side == "right":
            self.vel.x = 0
            self.pos.x -= self.speed
            self.next_vel.y = 0
        elif side == "up":
            self.vel.y = 0
            self.pos.y += self.speed
            self.next_vel.x = 0
        elif side == "down":
            self.vel.y = 0
            self.pos.y -= self.speed
            self.next_vel.x = 0

    def hit_node(self, node):
        if self.pos.x - 3 + self.width//2 <= node.x <= self.pos.x + 3 + self.width//2:
            if self.pos.y - 3 + self.width//2 <= node.y <= self.pos.y + 3 + self.width//2:
                if self.vel.x != 0:
                    if self.next_vel.y > 0 and "d" in node.neighbors or self.next_vel.y < 0 and "u" in node.neighbors:
                        self.vel.y = deepcopy(self.next_vel.y) # todo deepcopy might not be needed
                        self.vel.x = 0
                elif self.vel.y != 0:  # todo node 27 and 30 need "l" and "r" respectively
                    if self.next_vel.x > 0 and "r" in node.neighbors or self.next_vel.x < 0 and "l" in node.neighbors:
                        self.vel.x = deepcopy(self.next_vel.x)
                        self.vel.y = 0

    def eat(self, dots, score) -> int:
        for i in range(len(dots)):
            if dots[i].x - self.speed * 2 < self.pos.x + self.width//2 < dots[i].x + self.speed * 2 and \
                    dots[i].y - self.speed * 2 < self.pos.y + self.width//2 < dots[i].y + self.speed * 2:
                score += dots[i].points
                del dots[i]
                break
        return score
