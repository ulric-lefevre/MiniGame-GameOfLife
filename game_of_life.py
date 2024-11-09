import pygame
import numpy as np

width, height = 800, 600
grid_size = 10
grid_width = width // grid_size
grid_height = height // grid_size

black = (0, 0, 0)
white = (255, 255, 255)

def create_grid():
    return np.zeros((grid_height, grid_width))

def update_grid(grid):
    new_grid = np.copy(grid)
    for row in range(grid_height):
        for col in range(grid_width):
            live_neighbors = np.sum(grid[max(0, row-1):min(grid_height, row+2), max(0, col-1):min(grid_width, col+2)]) - grid[row, col]
            if grid[row, col] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[row, col] = 0
            else:
                if live_neighbors == 3:
                    new_grid[row, col] = 1
    return new_grid

def draw_grid(screen, grid):
    for row in range(grid_height):
        for col in range(grid_width):
            color = white if grid[row, col] == 1 else black
            pygame.draw.rect(screen, color, (col * grid_size, row * grid_size, grid_size, grid_size))

def game():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jeu de la Vie")
    clock = pygame.time.Clock()

    grid = create_grid()
    running = True
    paused = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid[y // grid_size, x // grid_size] = 1 - grid[y // grid_size, x // grid_size]

        if not paused:
            grid = update_grid(grid)

        screen.fill(black)
        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

game()