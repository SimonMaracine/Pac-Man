import pygame
import src.display as d


class Dot(object):
    points = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.color = (255, 240, 160)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.x - self.width//2, self.y - self.width//2, self.width, self.width))


def make_dots(walls) -> list:
    where_dots_cant_be = []
    for x in range(0, 6 * d.GRID + 1, d.GRID):
        for y in range(10 * d.GRID, 20 * d.GRID + 1, d.GRID):
            where_dots_cant_be.append((x, y))
    for x in range(23 * d.GRID, d.WIDTH + 1, d.GRID):
        for y in range(10 * d.GRID, 20 * d.GRID + 1, d.GRID):
            where_dots_cant_be.append((x, y))
    for x in range(8 * d.GRID, 21 * d.GRID + 1, d.GRID):
        for y in range(10 * d.GRID, 20 * d.GRID + 1, d.GRID):
            where_dots_cant_be.append((x, y))
    where_dots_cant_be.extend([(2 * d.GRID, 4 * d.GRID), (27 * d.GRID, 4 * d.GRID),
                               (2 * d.GRID, 24 * d.GRID), (27 * d.GRID, 24 * d.GRID)])

    dots = []
    for x in range(d.GRID * 2, d.WIDTH - d.GRID, d.GRID):
        for y in range(d.GRID * 2, d.HEIGHT - 4 * d.GRID, d.GRID):
            if all(list(map(lambda wall: (x, y) not in wall.shallow_area and (x, y) not in where_dots_cant_be, walls))):
                dot = Dot(x, y)
                dots.append(dot)

    for dot in dots:
        dot.y += 2 * d.GRID
    return dots
