import os
from copy import deepcopy

import pygame
from vectormath import Vector2 as Vector

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
        self.shallow_area = []

        for x in range(self.x, self.x + self.width + 1, GRID):
            for y in range(self.y, self.y + self.height + 1, GRID):
                self.shallow_area.append((x, y))

    def render(self):
        pygame.draw.rect(window, (0, 0, 200), (self.x, self.y, self.width, self.height), 4)


class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        pygame.draw.circle(window, (0, 0, 255), (self.x, self.y), 8)


class PacMan(object):
    def __init__(self):
        self.pos = Vector(14 * GRID - GRID // 2, 23 * GRID)
        self.width = GRID * 2
        self.speed = 3
        self.vel = Vector(0, 0)
        self.hit_wall = {"left": False, "right": False, "up": False, "down": False}
        self.next_vel = Vector(0, 0)
        self.can_move = {"x": True, "y": True}

    def render(self):
        pygame.draw.ellipse(window, (255, 255, 0), (self.pos.x + 3, self.pos.y + 3, self.width - 6, self.width - 6))
        # pygame.draw.ellipse(window, (255, 255, 0), (self.pos.x, self.pos.y, self.width, self.width))

        # draw hitbox
        # pygame.draw.rect(window, (255, 0, 0), (self.pos.x, self.pos.y + 3, 5, self.width - 6), 1)  # left hitbox
        # pygame.draw.rect(window, (255, 0, 0), (self.pos.x + self.width - 5, self.pos.y + 3, 5, self.width - 6), 1)  # right hitbox
        # pygame.draw.rect(window, (255, 0, 0), (self.pos.x + 3, self.pos.y, self.width - 6, 5), 1)  # up hitbox
        # pygame.draw.rect(window, (255, 0, 0), (self.pos.x + 3, self.pos.y + self.width - 5, self.width - 6, 5), 1)  # down hitbox

    def update(self):
        self.pos += self.vel

        if self.pos.x < 0:
            self.can_move["y"] = False
            if self.pos.x < -self.width * 10:  # left tunnel
                self.pos.x = WIDTH
        elif self.pos.x > WIDTH:
            self.can_move["y"] = False
            if self.pos.x > WIDTH + self.width * 9:  # right tunnel
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
                    if self.next_vel.y != 0:
                        self.vel.y = deepcopy(self.next_vel.y)
                        self.vel.x = 0
                elif self.vel.y != 0:
                    if self.next_vel.x != 0:
                        self.vel.x = deepcopy(self.next_vel.x)
                        self.vel.y = 0

    def eat(self, dots):
        global score
        for i in range(len(dots)):
            if dots[i].x - self.speed * 2 < self.pos.x + self.width//2 < dots[i].x + self.speed * 2 and \
                    dots[i].y - self.speed * 2 < self.pos.y + self.width//2 < dots[i].y + self.speed * 2:
                score += Dot.points
                del dots[i]
                break


class Ghost(object):
    pass


class Dot(object):
    points = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.color = (255, 240, 100)

    def render(self):
        pygame.draw.rect(window, self.color, (self.x - self.width//2, self.y - self.width//2, self.width, self.width))


class Power(Dot):
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
    global window, clock, fps_font, walls, nodes, dots, score
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
    middle_h2_wall = Wall(11 * GRID, 25 * GRID, 7 * GRID, GRID)  # here
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
    node1 = Node(2 * GRID, 2 * GRID)
    node2 = Node(7 * GRID, 2 * GRID)
    node3 = Node(13 * GRID, 2 * GRID)
    node4 = Node(16*GRID, 2*GRID)
    node5 = Node(22*GRID, 2*GRID)
    node6 = Node(27*GRID, 2*GRID)
    node7 = Node(2*GRID, 6*GRID)
    node8 = Node(7*GRID, 6*GRID)
    node9 = Node(10*GRID, 6*GRID)
    node10 = Node(13*GRID, 6*GRID)
    node11 = Node(16*GRID, 6*GRID)
    node12 = Node(19*GRID, 6*GRID)
    node13 = Node(22*GRID, 6*GRID)
    node14 = Node(27*GRID, 6*GRID)
    node15 = Node(2*GRID, 9*GRID)
    node16 = Node(7*GRID, 9*GRID)
    node17 = Node(10 * GRID, 9 * GRID)
    node18 = Node(13*GRID, 9*GRID)
    node19 = Node(16*GRID, 9*GRID)
    node20 = Node(19*GRID, 9*GRID)
    node21 = Node(22*GRID, 9*GRID)
    node22 = Node(27*GRID, 9*GRID)
    node23 = Node(10*GRID, 12*GRID)
    node24 = Node(13*GRID, 12*GRID)
    node25 = Node(16*GRID, 12*GRID)
    node26 = Node(19*GRID, 12*GRID)
    node27 = Node(7*GRID, 15*GRID)
    node28 = Node(10*GRID, 15*GRID)
    node29 = Node(19*GRID, 15*GRID)
    node30 = Node(22*GRID, 15*GRID)
    node31 = Node(10*GRID, 18*GRID)
    node32 = Node(19*GRID, 18*GRID)
    node33 = Node(2*GRID, 21*GRID)
    node34 = Node(7*GRID, 21*GRID)
    node35 = Node(10*GRID, 21*GRID)
    node36 = Node(13*GRID, 21*GRID)
    node37 = Node(16*GRID, 21*GRID)
    node38 = Node(19*GRID, 21*GRID)
    node39 = Node(22*GRID, 21*GRID)
    node40 = Node(27*GRID, 21*GRID)
    node41 = Node(2*GRID, 24*GRID)
    node42 = Node(4*GRID, 24*GRID)
    node43 = Node(7*GRID, 24*GRID)
    node44 = Node(10*GRID, 24*GRID)
    node45 = Node(13*GRID, 24*GRID)
    node46 = Node(16*GRID, 24*GRID)
    node47 = Node(19*GRID, 24*GRID)
    node48 = Node(22*GRID, 24*GRID)
    node49 = Node(25*GRID, 24*GRID)
    node50 = Node(27*GRID, 24*GRID)
    node51 = Node(2*GRID, 27*GRID)
    node52 = Node(4*GRID, 27*GRID)
    node53 = Node(7*GRID, 27*GRID)
    node54 = Node(10*GRID, 27*GRID)
    node55 = Node(13*GRID, 27*GRID)
    node56 = Node(16*GRID, 27*GRID)
    node57 = Node(19*GRID, 27*GRID)
    node58 = Node(22*GRID, 27*GRID)
    node59 = Node(25*GRID, 27*GRID)
    node60 = Node(27*GRID, 27*GRID)
    node61 = Node(2*GRID, 30*GRID)
    node62 = Node(13 * GRID, 30 * GRID)
    node63 = Node(16 * GRID, 30 * GRID)
    node64 = Node(27*GRID, 30*GRID)
    nodes = (
        node1, node2, node3, node4, node5, node6, node7, node8, node9, node10,
        node11, node12, node13, node14, node15, node16, node17, node18, node19, node20,
        node21, node22, node23, node24, node25, node26, node27, node28, node29, node30,
        node31, node32, node33, node34, node35, node36, node37, node38, node39, node40,
        node41, node42, node43, node44, node45, node46, node47, node48, node49, node50,
        node51, node52, node53, node54, node55, node56, node57, node58, node59, node60,
        node61, node62, node63, node64
    )

    where_dots_cant_be = []
    for x in range(0, 6 * GRID + 1, GRID):
        for y in range(10 * GRID, 20 * GRID + 1, GRID):
            where_dots_cant_be.append((x, y))
    for x in range(23 * GRID, WIDTH + 1, GRID):
        for y in range(10 * GRID, 20 * GRID + 1, GRID):
            where_dots_cant_be.append((x, y))
    for x in range(8 * GRID, 21 * GRID + 1, GRID):
        for y in range(10 * GRID, 20 * GRID + 1, GRID):
            where_dots_cant_be.append((x, y))

    dots = []
    for x in range(GRID * 2, WIDTH - GRID, GRID):
        for y in range(GRID * 2, HEIGHT - GRID, GRID):
            if all(list(map(lambda wall: (x, y) not in wall.shallow_area and (x, y) not in where_dots_cant_be, walls))):
                dot = Dot(x, y)
                dots.append(dot)

    score = 0


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
        for wall in walls:
            wall.render()
            pacman.collide(wall)
        # print(pacman.hit_wall)
        pacman.update()
        for node in nodes:
            # node.render()
            pacman.hit_node(node)
        pacman.eat(dots)
        for dot in dots:
            dot.render()
        pacman.render()
        # show_grid()
        show_fps()
        pygame.display.flip()
        clock.tick(30)
        print(pacman.pos)
        # print(pacman.vel)


def main():
    print("\nHello, Pac-Man!")
    init()
    loop()
    pygame.quit()


if __name__ == "__main__":
    main()
