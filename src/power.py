import pygame
import src.display as d
from src.dot import Dot


class Power(Dot):
    points = 40

    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 7

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.width)


def make_powers() -> list:
    power1 = Power(2 * d.GRID, 6 * d.GRID)
    power2 = Power(27 * d.GRID, 6 * d.GRID)
    power3 = Power(2 * d.GRID, 26 * d.GRID)
    power4 = Power(27 * d.GRID, 26 * d.GRID)
    powers = [power1, power2, power3, power4]
    return powers
