import pygame
import src.display as d
from src.display import set_size, set_window, show_fps, show_grid
from src.pacman import PacMan
from src.wall import make_walls
from src.node import make_nodes
from src.dot import make_dots

running = True
clock = pygame.time.Clock()
fps_font = pygame.font.SysFont("calibri", 16, True)
score_font = pygame.font.SysFont("calibri", 22, True)
score = 0


def show_score(surface, font, score):
    score_text = font.render("HIGH SCORE: " + str(score), True, (255, 255, 255))
    surface.blit(score_text, (d.WIDTH // 2 - score_text.get_width() // 2, 4))


def main():
    global window, running, score
    set_size(18, 29, 36)  # 18, 29, 32
    window = set_window(d.WIDTH, d.HEIGHT)
    pacman = PacMan()
    walls = make_walls()
    nodes = make_nodes()
    dots = make_dots(walls)

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
            wall.render(window)
            pacman.collide(wall)
        # print(pacman.hit_wall)
        pacman.update()
        for node in nodes:
            # node.render(window)
            pacman.hit_node(node)
        score = pacman.eat(dots, score)
        for dot in dots:
            dot.render(window)
        pacman.render(window)
        show_score(window, score_font, score)
        # show_grid(window)
        show_fps(window, clock, fps_font)
        pygame.display.flip()
        clock.tick(30)
        # print(pacman.pos)
        # print(pacman.vel)
        print(score)

    pygame.quit()
