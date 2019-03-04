import os

import pygame
from vectors import Vector

GRID = 18
WIDTH = 29 * GRID
HEIGHT = 32 * GRID
running = True

class Wall(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self):
        pygame.draw.rect(window, (0, 0, 200), (self.x, self.y, self.width, self.height), 4)


class PacMan(object):
    def __init__(self):
        self.pos = Vector(14 * GRID - GRID // 2, 23 * GRID, 0)
        self.width = GRID
        self.vel = 4
        self.dir = Vector(0, 0, 0)
        # self.dirs = {"left": False, "right": False, "up": False, "down": False}

    def render(self):
        pygame.draw.ellipse(window, (255, 255, 0), (self.pos.x + 3, self.pos.y + 3, self.width * 2 - 6, self.width * 2 - 6))

    def update(self):
        self.pos = self.pos.sum(self.dir)
        y = self.pos.y
        if self.pos.x < -self.width * 10:  # left tunnel
            self.pos = Vector(WIDTH + 2, y, 0)
        elif self.pos.x > WIDTH + self.width * 9:  # right tunnel
            self.pos = Vector(-self.width - 2, y, 0)

    def change_dir(self, direction):
        # for dir in self.dirs:
        #     if dir == direction:
        #         self.dirs[dir] = True
        #     else:
        #         self.dirs[dir] = False
        if direction == "left":
            self.dir = Vector(-self.vel, 0, 0)
        elif direction == "right":
            self.dir = Vector(self.vel, 0, 0)
        elif direction == "up":
            self.dir = Vector(0, -self.vel, 0)
        elif direction == "down":
            self.dir = Vector(0, self.vel, 0)

    def collide(self, wall):
        if self.pos.x < wall.x + wall.width < self.pos.x + 5:
            if wall.y + wall.height > self.pos.y > wall.y:
                return "left"
        elif self.pos.x + self.width > wall.x > self.pos.x - 5:
            if wall.y + wall.height > self.pos.y + self.width > wall.y:
                return "right"
        else:
            return None

    def stop(self, side):
        if side == "left":
            self.dir = Vector(0, 0, 0)
        elif side == "right":
            self.dir = Vector(0, 0, 0)

    def eat(self):
        pass


class Ghost(object):
    pass


def show_fps():
    fps_text = fps_font.render("FPS: " + str(int(clock.get_fps())), True, (255, 255, 255))
    window.blit(fps_text, (5, HEIGHT - 18))


def show_grid():
    for i in range(29):
        pygame.draw.line(window, (255, 255, 255), (i * GRID, 0), (i * GRID, HEIGHT), 1)
    for j in range(32):
        pygame.draw.line(window, (255, 255, 255), (0, j * GRID), (WIDTH, j * GRID), 1)


def init():
    global window, clock, fps_font, map
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pac-Man")
    clock = pygame.time.Clock()

    fps_font = pygame.font.SysFont("calibri", 16, True)
    top_wall = Wall(0, 0, WIDTH, GRID)
    bottom_wall = Wall(0, HEIGHT - GRID, WIDTH, GRID)
    left_top_wall = Wall(0, 0, GRID, 11 * GRID)
    right_top_wall = Wall(WIDTH - GRID, 0, GRID, 11 * GRID)
    left_down_wall = Wall(0, 19 * GRID, GRID, 13 * GRID)
    right_down_wall = Wall(WIDTH - GRID, 19 * GRID, GRID, 13 * GRID)
    h_left1_wall = Wall(0, 10 * GRID, 6 * GRID, GRID)
    h_left2_wall = Wall(0, 13 * GRID, 6 * GRID, GRID)
    h_left3_wall = Wall(0, 16 * GRID, 6 * GRID, GRID)
    h_left4_wall = Wall(0, 19 * GRID, 6 * GRID, GRID)
    h_right1_wall = Wall(WIDTH - 6 * GRID, 10 * GRID, 6 * GRID, GRID)
    h_right2_wall = Wall(WIDTH - 6 * GRID, 13 * GRID, 6 * GRID, GRID)
    h_right3_wall = Wall(WIDTH - 6 * GRID, 16 * GRID, 6 * GRID, GRID)
    h_right4_wall = Wall(WIDTH - 6 * GRID, 19 * GRID, 6 * GRID, GRID)
    v_left1_wall = Wall(5 * GRID, 10 * GRID, GRID, 4 * GRID)
    v_left2_wall = Wall(5 * GRID, 16 * GRID, GRID, 4 * GRID)
    v_right1_wall = Wall(WIDTH - 6 * GRID, 10 * GRID, GRID, 4 * GRID)
    v_right2_wall = Wall(WIDTH - 6 * GRID, 16 * GRID, GRID, 4 * GRID)
    up_center1_wall = Wall(11 * GRID, 13 * GRID, 3 * GRID, GRID)
    up_center2_wall = Wall(15 * GRID, 13 * GRID, 3 * GRID, GRID)
    down_center_wall = Wall(11 * GRID, 16 * GRID, 7 * GRID, GRID)
    left_center_wall = Wall(11 * GRID, 13 * GRID, GRID, 4 * GRID)
    right_center_wall = Wall(17 * GRID, 13 * GRID, GRID, 4 * GRID)
    square1 = Wall(3 * GRID, 3 * GRID, 3 * GRID, 2 * GRID)
    square2 = Wall(8 * GRID, 3 * GRID, 4 * GRID, 2 * GRID)
    square3 = Wall(17 * GRID, 3 * GRID, 4 * GRID, 2 * GRID)
    square4 = Wall(23 * GRID, 3 * GRID, 3 * GRID, 2 * GRID)
    up_generic_wall = Wall(14 * GRID, 0, GRID, 5 * GRID)
    middle_left_generic_wall = Wall(8 * GRID, 16 * GRID, GRID, 4 * GRID)
    middle_right_generic_wall = Wall(20 * GRID, 16 * GRID, GRID, 4 * GRID)
    up_left_generic_wall = Wall(3 * GRID, 7 * GRID, 3 * GRID, GRID)
    up_right_generic_wall = Wall(WIDTH - 6 * GRID, 7 * GRID, 3 * GRID, GRID)
    h1_wall = Wall(11 * GRID, 7 * GRID, 7 * GRID, GRID)
    h2_wall = Wall(8 * GRID, 10 * GRID, 4 * GRID, GRID)
    h3_wall = Wall(17 * GRID, 10 * GRID, 4 * GRID, GRID)
    v1_wall = Wall(14 * GRID, 7 * GRID, GRID, 4 * GRID)
    v2_wall = Wall(8 * GRID, 7 * GRID, GRID, 7 * GRID)
    v3_wall = Wall(WIDTH - 9 * GRID, 7 * GRID, GRID, 7 * GRID)
    down_left_generic_wall = Wall(8 * GRID, 22 * GRID, 4 * GRID, GRID)
    down_right_generic_wall = Wall(WIDTH - 12 * GRID, 22 * GRID, 4 * GRID, GRID)
    middle_h1_wall = Wall(11 * GRID, 19 * GRID, 7 * GRID, GRID)
    middle_h2_wall = Wall(11 * GRID, 25 * GRID, 7 * GRID, GRID)
    middle_v1_wall = Wall(14 * GRID, 19 * GRID, GRID, 4 * GRID)
    middle_v2_wall = Wall(14 * GRID, 25 * GRID, GRID, 4 * GRID)
    h1_down_wall = Wall(3 * GRID, HEIGHT - 10 * GRID, 3 * GRID, GRID)
    h2_down_wall = Wall(WIDTH - 6 * GRID, HEIGHT - 10 * GRID, 3 * GRID, GRID)
    h3_down_wall = Wall(3 * GRID, HEIGHT - 4 * GRID, 9 * GRID, GRID)
    h4_down_wall = Wall(WIDTH - 12 * GRID, HEIGHT - 4 * GRID, 9 * GRID, GRID)
    v1_down_wall = Wall(5 * GRID, HEIGHT - 10 * GRID, GRID, 4 * GRID)
    v2_down_wall = Wall(WIDTH - 6 * GRID, HEIGHT - 10 * GRID, GRID, 4 * GRID)
    v3_down_wall = Wall(8 * GRID, HEIGHT - 7 * GRID, GRID, 4 * GRID)
    v4_down_wall = Wall(WIDTH - 9 * GRID, HEIGHT - 7 * GRID, GRID, 4 * GRID)
    left_weird_wall = Wall(0, HEIGHT - 7 * GRID, 3 * GRID, GRID)
    right_weird_wall = Wall(WIDTH - 3 * GRID, HEIGHT - 7 * GRID, 3 * GRID, GRID)
    map = [
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
    ]


def loop():
    global window, clock, running
    pacman = PacMan()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    pacman.change_dir("left")
                elif event.key == pygame.K_RIGHT:
                    pacman.change_dir("right")
                elif event.key == pygame.K_UP:
                    pacman.change_dir("up")
                elif event.key == pygame.K_DOWN:
                    pacman.change_dir("down")

        window.fill((0, 0, 0))
        pacman.render()
        pacman.update()
        for wall in map:
            wall.render()
        for wall in map:
            if pacman.collide(wall) == "left":
                pacman.stop("left")
            elif pacman.collide(wall) == "right":
                pacman.stop("right")
        # show_grid()
        show_fps()
        pygame.display.flip()
        clock.tick(60)


def main():
    print("\nHello, Pac-Man!")
    init()
    loop()
    pygame.quit()


if __name__ == "__main__":
    main()
