import sys
import pygame
import src.display as d
from src.display import set_size, set_window, show_fps, show_grid, switch_fullscreen
from src.pacman import PacMan
from src.wall import make_walls
from src.node import make_nodes
from src.dot import make_dots

set_size(18, 29, 36)  # 18, 29, 32
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
        init_objects(True, False, False, True)
    else:
        init_objects(True, False, False, False)


def init_objects(p=True, w=True, n=True, d=True):
    global pacman, walls, nodes, dots
    if p:
        pacman = PacMan()
    if w:
        walls = make_walls()
    if n:
        nodes = make_nodes()
    if d:
        dots = make_dots(walls)
        assert len(dots) == 246, "There have to be 246 dots."


def main():
    global window, score, fullscreen, lives
    init_objects()

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
                    pygame.time.wait(1000)
                    revive()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.change_dir("left")
                elif event.key == pygame.K_RIGHT:
                    pacman.change_dir("right")
                elif event.key == pygame.K_UP:
                    pacman.change_dir("up")
                elif event.key == pygame.K_DOWN:
                    pacman.change_dir("down")

        window.fill((0, 0, 0))
        for wall in walls:
            wall.render(window)
            pacman.collide(wall)
        # print(pacman.hit_wall)
        pacman.update()
        for node in nodes:
            # node.render(window)
            pacman.hit_node(node)
        score = pacman.eat(dots, score)
        if not dots:
            pygame.time.wait(1000)
            init_objects(True, False, False, True)
        for dot in dots:
            dot.render(window)
        pacman.render(window)
        show_score(window, score_font, score)
        show_lives(window, score_font, lives)
        # show_grid(window)
        show_fps(window, clock, fps_font)
        pygame.display.flip()
        clock.tick(300)
        print(pacman.pos)
        # print(pacman.vel)
