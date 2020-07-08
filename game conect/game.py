import sys
import pygame
import numpy as np


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 50
HEIGHT = 50
MARGIN = 1
MATRIZ_SIZE = 3


def main():
    grid = []
    for row in range(MATRIZ_SIZE):
        grid.append([])
        for column in range(MATRIZ_SIZE):
            grid[row].append(0)

    check_grid = []
    for row in range(MATRIZ_SIZE):
        check_grid.append([])
        for column in range(MATRIZ_SIZE):
            check_grid[row].append(1)

    pygame.init()

    size = [255, 255]

    done = False

    window = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    while not done:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                if grid[row][column] == 1:
                    grid[row][column] = 0
                else:
                    grid[row][column] = 1

                print(grid)

                print("Click ", pos, "Grid coordinates: ", row, column)

            if grid == check_grid:
                print("completo")
                done = True

        window.fill(BLACK)

        for row in range(MATRIZ_SIZE):
            for column in range(MATRIZ_SIZE):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(window,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()


main()
