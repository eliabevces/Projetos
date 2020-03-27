import sys
import pygame
import numpy as np


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 100
HEIGHT = 100
MARGIN = 1
MATRIZ_SIZE = 3

grid = []
for row in range(MATRIZ_SIZE):
    grid.append([])
    for column in range(MATRIZ_SIZE):
        grid[row].append(0)


pygame.init()

size = [305, 305]

done = False
turn = True
comp = True

window = pygame.display.set_mode(size)
pygame.display.set_caption('JOGO DA VELHA')
clock = pygame.time.Clock()

while not done:
    window.fill(BLACK)
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
            if turn == True and grid[row][column] == 0:
                grid[row][column] = 1
                turn = False
            elif turn == False and grid[row][column] == 0:
                grid[row][column] = 2
                turn = True
            print(grid)

            print("Click ", pos, "Grid coordinates: ", row, column)

        comp = False
        for row in range(MATRIZ_SIZE):
            for column in range(MATRIZ_SIZE):
                if grid[row][column] == 0:
                    comp = True
                    break

    for row in range(MATRIZ_SIZE):
        for column in range(MATRIZ_SIZE):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            if grid[row][column] == 2:
                color = RED
            pygame.draw.rect(window,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    if comp == False:
        print('completo')
        window.fill(WHITE)
        clock.tick(200)
        done = True

    # diagonal principal
    if grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1:
        print('Verde Ganhou')
        window.fill(GREEN)
        clock.tick(200)
        done = True
    if grid[0][0] == 2 and grid[1][1] == 2 and grid[2][2] == 2:
        print('Vermelho Ganhou')
        window.fill(RED)
        clock.tick(200)
        done = True

    # COLUNA 1
    if grid[0][0] == 1 and grid[1][0] == 1 and grid[2][0] == 1:
        print('Verde Ganhou')
        window.fill(GREEN)
        clock.tick(200)
        done = True
    if grid[0][0] == 2 and grid[1][0] == 2 and grid[2][0] == 2:
        print('Vermelho Ganhou')
        window.fill(RED)
        clock.tick(200)
        done = True
    # COLUNA 2
    if grid[0][1] == 1 and grid[1][1] == 1 and grid[2][1] == 1:
        print('Verde Ganhou')
        window.fill(GREEN)
        clock.tick(200)
        done = True
    if grid[0][1] == 2 and grid[1][1] == 2 and grid[2][1] == 2:
        print('Vermelho Ganhou')
        window.fill(RED)
        clock.tick(200)
        done = True
    # COLUNA 3
    if grid[0][2] == 1 and grid[1][2] == 1 and grid[2][2] == 1:
        print('Verde Ganhou')
        window.fill(GREEN)
        clock.tick(200)
        done = True
    if grid[0][2] == 2 and grid[1][2] == 2 and grid[2][2] == 2:
        print('Vermelho Ganhou')
        window.fill(RED)
        clock.tick(200)
        done = True
    # linha 1
    if grid[0][0] == 1 and grid[0][1] == 1 and grid[0][2] == 1:
        print('Verde Ganhou')
        window.fill(GREEN)
        clock.tick(200)
        done = True
    if grid[0][0] == 2 and grid[0][1] == 2 and grid[0][2] == 2:
        print('Vermelho Ganhou')
        window.fill(RED)
        clock.tick(200)
        done = True
    # linha 2
    if grid[1][0] == 1 and grid[1][1] == 1 and grid[1][2] == 1:
        print('Verde Ganhou')
        window.fill(GREEN)
        clock.tick(200)
        done = True
    if grid[1][0] == 2 and grid[1][1] == 2 and grid[1][2] == 2:
        print('Vermelho Ganhou')
        window.fill(RED)
        clock.tick(200)
        done = True
    # linha 3
    if grid[2][0] == 1 and grid[2][1] == 1 and grid[2][2] == 1:
        print('Verde Ganhou')
        window.fill(GREEN)
        clock.tick(200)
        done = True
    if grid[2][0] == 2 and grid[2][1] == 2 and grid[2][2] == 2:
        print('Vermelho Ganhou')
        window.fill(RED)
        clock.tick(200)
        done = True
    # diagonal secundaria
    if grid[0][2] == 1 and grid[1][1] == 1 and grid[2][0] == 1:
        print('Verde Ganhou')
        window.fill(GREEN)
        clock.tick(200)
        done = True
    if grid[0][2] == 2 and grid[1][1] == 2 and grid[2][0] == 2:
        print('Vermelho Ganhou')
        window.fill(RED)
        clock.tick(200)
        done = True

    clock.tick(60)

    pygame.display.flip()


pygame.quit()
