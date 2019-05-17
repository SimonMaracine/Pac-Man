import os
import pygame

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
GRID = 0
WIDTH = 0
HEIGHT = 0


def set_size(grid, width: int, height: int):
    global GRID, WIDTH, HEIGHT
    GRID = grid
    WIDTH = width * GRID
    HEIGHT = height * GRID


def set_window(width, height, fullscreen=False) -> tuple:
    if fullscreen:
        window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pac-Man")
    return window, fullscreen


def switch_fullscreen(fullscreen) -> tuple:
    if not fullscreen:
        window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((WIDTH, HEIGHT))
    return window, not fullscreen


def show_fps(surface, clock, font):
    fps_text = font.render("FPS: " + str(int(clock.get_fps())), True, (255, 255, 255))
    surface.blit(fps_text, (5, HEIGHT - 18))


def show_grid(surface):
    for i in range(29):
        pygame.draw.line(surface, (255, 255, 255), (i * GRID, 0), (i * GRID, HEIGHT), 1)
    for j in range(32):
        pygame.draw.line(surface, (255, 255, 255), (0, j * GRID), (WIDTH, j * GRID), 1)
