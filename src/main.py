import sys
import pygame
import src.display as d
from src.display import set_size, set_window, show_fps, show_grid, switch_fullscreen
from src.pacman import PacMan
from src.wall import make_walls
from src.node import make_nodes
from src.dot import make_dots
from src.power import make_powers
from src.ghost import Ghost

set_size(18, 29, 36)  # 18 (24), 29, 32
window, fullscreen = set_window(d.WIDTH, d.HEIGHT, False)
clock = pygame.time.Clock()
fps_font = pygame.font.SysFont("calibri", 16, True)
score_font = pygame.font.SysFont("calibri", 22, True)
score = 0
lives = 3


def show_score(surface, font, scr):
    score_text = font.render("HIGH SCORE: " + str(scr), True, (255, 255, 255))
    surface.blit(score_text, (d.WIDTH // 2 - score_text.get_width() // 2, 4))


def show_lives(surface, font, liv):
    text = font.render("LIVES: " + str(liv), True, (255, 255, 255))
    surface.blit(text, (60, d.HEIGHT - 26))


def quit():
    pygame.quit()
    sys.exit()


def revive():
    global lives, score
    lives -= 1
    if lives < 1:
        score = 0
        lives = 3
        init_objects(True, False, False, True, True)
    else:
        init_objects(True, False, False, False, False)


def init_objects(pm=True, w=True, n=True, d=True, p=True):
    global pacman, walls, nodes, dots, powers
    if pm:
        pacman = PacMan()
    if w:
        walls = make_walls()
    if n:
        nodes = make_nodes()
    if d:
        dots = make_dots(walls)
        assert len(dots) == 242, "There have to be 242 dots, not " + str(len(dots))
    if p:
        powers = make_powers()


def main():
    global window, score, fullscreen, lives
    init_objects()
    blinky = Ghost(3 * d.GRID, 3 * d.GRID)
    g = False  # temporary
    n = False  # temporary

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    quit()
                elif event.key == pygame.K_f:
                    window, fullscreen = switch_fullscreen(fullscreen)
                elif event.key == pygame.K_r:
                    # pygame.time.wait(1000)
                    revive()
                elif event.key == pygame.K_g: # temporary
                    g = not g
                elif event.key == pygame.K_n: # temporary
                    n = not n
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.change_dir("left")
                elif event.key == pygame.K_RIGHT:
                    pacman.change_dir("right")
                elif event.key == pygame.K_UP:
                    pacman.change_dir("up")
                elif event.key == pygame.K_DOWN:
                    pacman.change_dir("down")

        window.fill((2, 2, 2))
        for wall in walls:
            wall.render(window)
            pacman.collide(wall)
        # print(pacman.hit_wall)
        pacman.update()
        blinky.update(pacman)
        blinky.catch_pacman(nodes)
        if blinky.eat_pacman():
            revive()
        for node in nodes:
            if n:  # temporary
                node.render(window)
            pacman.hit_node(node)
        score = pacman.eat(dots, score)
        score = pacman.eat(powers, score)
        if not dots:
            pygame.time.wait(1000)
            init_objects(True, False, False, True, True)
        for dot in dots:
            dot.render(window)
        for power in powers:
            power.render(window)
        pacman.render(window)
        blinky.render(window)
        show_score(window, score_font, score)
        show_lives(window, score_font, lives)
        if g:  # temporary
            show_grid(window)
        show_fps(window, clock, fps_font)
        pygame.display.flip()
        clock.tick(30)
        # print(pacman.pos)
        # print(pacman.vel)
