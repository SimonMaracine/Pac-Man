import pygame
import src.display as d


class Wall(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shallow_area = []

    def render(self, surface):
        pygame.draw.rect(surface, (0, 0, 200), (self.x, self.y, self.width, self.height), 4)

    def def_shallow_area(self):
        for x in range(self.x, self.x + self.width + 1, d.GRID):
            for y in range(self.y, self.y + self.height + 1, d.GRID):
                self.shallow_area.append((x, y))


def make_walls() -> tuple:
    top_wall = Wall(0, 0, d.WIDTH, d.GRID)
    bottom_wall = Wall(0, 31 * d.GRID, d.WIDTH, d.GRID)
    left_top_wall = Wall(0, 0, d.GRID, 11 * d.GRID)
    right_top_wall = Wall(d.WIDTH - d.GRID, 0, d.GRID, 11 * d.GRID)
    left_down_wall = Wall(0, 19 * d.GRID, d.GRID, 13 * d.GRID)
    right_down_wall = Wall(d.WIDTH - d.GRID, 19 * d.GRID, d.GRID, 13 * d.GRID)
    h_left1_wall = Wall(0, 10 * d.GRID, 6 * d.GRID, d.GRID)
    h_left2_wall = Wall(0, 13 * d.GRID, 6 * d.GRID, d.GRID)
    h_left3_wall = Wall(0, 16 * d.GRID, 6 * d.GRID, d.GRID)
    h_left4_wall = Wall(0, 19 * d.GRID, 6 * d.GRID, d.GRID)
    h_right1_wall = Wall(d.WIDTH - 6 * d.GRID, 10 * d.GRID, 6 * d.GRID, d.GRID)
    h_right2_wall = Wall(d.WIDTH - 6 * d.GRID, 13 * d.GRID, 6 * d.GRID, d.GRID)
    h_right3_wall = Wall(d.WIDTH - 6 * d.GRID, 16 * d.GRID, 6 * d.GRID, d.GRID)
    h_right4_wall = Wall(d.WIDTH - 6 * d.GRID, 19 * d.GRID, 6 * d.GRID, d.GRID)
    v_left1_wall = Wall(5 * d.GRID, 10 * d.GRID, d.GRID, 4 * d.GRID)
    v_left2_wall = Wall(5 * d.GRID, 16 * d.GRID, d.GRID, 4 * d.GRID)
    v_right1_wall = Wall(d.WIDTH - 6 * d.GRID, 10 * d.GRID, d.GRID, 4 * d.GRID)
    v_right2_wall = Wall(d.WIDTH - 6 * d.GRID, 16 * d.GRID, d.GRID, 4 * d.GRID)
    up_center1_wall = Wall(11 * d.GRID, 13 * d.GRID, 3 * d.GRID, d.GRID)
    up_center2_wall = Wall(15 * d.GRID, 13 * d.GRID, 3 * d.GRID, d.GRID)
    down_center_wall = Wall(11 * d.GRID, 16 * d.GRID, 7 * d.GRID, d.GRID)
    left_center_wall = Wall(11 * d.GRID, 13 * d.GRID, d.GRID, 4 * d.GRID)
    right_center_wall = Wall(17 * d.GRID, 13 * d.GRID, d.GRID, 4 * d.GRID)
    square1 = Wall(3 * d.GRID, 3 * d.GRID, 3 * d.GRID, 2 * d.GRID)
    square2 = Wall(8 * d.GRID, 3 * d.GRID, 4 * d.GRID, 2 * d.GRID)
    square3 = Wall(17 * d.GRID, 3 * d.GRID, 4 * d.GRID, 2 * d.GRID)
    square4 = Wall(23 * d.GRID, 3 * d.GRID, 3 * d.GRID, 2 * d.GRID)
    up_generic_wall = Wall(14 * d.GRID, 0, d.GRID, 5 * d.GRID)
    middle_left_generic_wall = Wall(8 * d.GRID, 16 * d.GRID, d.GRID, 4 * d.GRID)
    middle_right_generic_wall = Wall(20 * d.GRID, 16 * d.GRID, d.GRID, 4 * d.GRID)
    up_left_generic_wall = Wall(3 * d.GRID, 7 * d.GRID, 3 * d.GRID, d.GRID)
    up_right_generic_wall = Wall(d.WIDTH - 6 * d.GRID, 7 * d.GRID, 3 * d.GRID, d.GRID)
    h1_wall = Wall(11 * d.GRID, 7 * d.GRID, 7 * d.GRID, d.GRID)
    h2_wall = Wall(8 * d.GRID, 10 * d.GRID, 4 * d.GRID, d.GRID)
    h3_wall = Wall(17 * d.GRID, 10 * d.GRID, 4 * d.GRID, d.GRID)
    v1_wall = Wall(14 * d.GRID, 7 * d.GRID, d.GRID, 4 * d.GRID)
    v2_wall = Wall(8 * d.GRID, 7 * d.GRID, d.GRID, 7 * d.GRID)
    v3_wall = Wall(d.WIDTH - 9 * d.GRID, 7 * d.GRID, d.GRID, 7 * d.GRID)
    down_left_generic_wall = Wall(8 * d.GRID, 22 * d.GRID, 4 * d.GRID, d.GRID)
    down_right_generic_wall = Wall(d.WIDTH - 12 * d.GRID, 22 * d.GRID, 4 * d.GRID, d.GRID)
    middle_h1_wall = Wall(11 * d.GRID, 19 * d.GRID, 7 * d.GRID, d.GRID)
    middle_h2_wall = Wall(11 * d.GRID, 25 * d.GRID, 7 * d.GRID, d.GRID)  # here
    middle_v1_wall = Wall(14 * d.GRID, 19 * d.GRID, d.GRID, 4 * d.GRID)
    middle_v2_wall = Wall(14 * d.GRID, 25 * d.GRID, d.GRID, 4 * d.GRID)

    h1_down_wall = Wall(3 * d.GRID, 22 * d.GRID, 3 * d.GRID, d.GRID)
    h2_down_wall = Wall(d.WIDTH - 6 * d.GRID, 22 * d.GRID, 3 * d.GRID, d.GRID)
    h3_down_wall = Wall(3 * d.GRID, 28 * d.GRID, 9 * d.GRID, d.GRID)
    h4_down_wall = Wall(d.WIDTH - 12 * d.GRID, 28 * d.GRID, 9 * d.GRID, d.GRID)
    v1_down_wall = Wall(5 * d.GRID, 22 * d.GRID, d.GRID, 4 * d.GRID)
    v2_down_wall = Wall(d.WIDTH - 6 * d.GRID, 22 * d.GRID, d.GRID, 4 * d.GRID)
    v3_down_wall = Wall(8 * d.GRID, 25 * d.GRID, d.GRID, 4 * d.GRID)
    v4_down_wall = Wall(d.WIDTH - 9 * d.GRID, 25 * d.GRID, d.GRID, 4 * d.GRID)
    left_weird_wall = Wall(0, 25 * d.GRID, 3 * d.GRID, d.GRID)
    right_weird_wall = Wall(d.WIDTH - 3 * d.GRID, 25 * d.GRID, 3 * d.GRID, d.GRID)
    walls = (
        top_wall,
        bottom_wall,
        left_top_wall,
        right_top_wall,
        left_down_wall,
        right_down_wall,
        h_left1_wall,
        h_left2_wall,
        h_left3_wall,
        h_left4_wall,
        h_right1_wall,
        h_right2_wall,
        h_right3_wall,
        h_right4_wall,
        v_left1_wall,
        v_left2_wall,
        v_right1_wall,
        v_right2_wall,
        up_center1_wall,
        up_center2_wall,
        down_center_wall,
        left_center_wall,
        right_center_wall,
        square1,
        square2,
        square3,
        square4,
        up_generic_wall,
        middle_left_generic_wall,
        middle_right_generic_wall,
        up_left_generic_wall,
        up_right_generic_wall,
        h1_wall,
        h2_wall,
        h3_wall,
        v1_wall,
        v2_wall,
        v3_wall,
        down_left_generic_wall,
        down_right_generic_wall,
        middle_h1_wall,
        middle_h2_wall,
        middle_v1_wall,
        middle_v2_wall,
        h1_down_wall,
        h2_down_wall,
        h3_down_wall,
        h4_down_wall,
        v1_down_wall,
        v2_down_wall,
        v3_down_wall,
        v4_down_wall,
        left_weird_wall,
        right_weird_wall
    )
    for wall in walls:
        wall.y += 2 * d.GRID
        wall.def_shallow_area()
    return walls
