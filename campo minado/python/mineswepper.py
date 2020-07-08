import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

MARGIN = 1
size = [511, 511]
WIDTH = 50
HEIGHT = 50
MATRIZ_SIZE = 10
NumBombs = 10
clock = pygame.time.Clock()


class Cell:
    def __init__(self):
        self.bomb = False


def main():

    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Campo Minado")
    done = False

    grid = [[Cell() for n in range(MATRIZ_SIZE)] for n in range(MATRIZ_SIZE)]

    for n in range(NumBombs):
        while True:
            x = randint(0, 9)
            y = randint(0, 9)
            if grid[x][y].bomb == False:
                grid[x][y].bomb = True
                print(x, y)
                break

    while not done:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     # User clicks the mouse. Get the position
            #     pos = pygame.mouse.get_pos()
            #     # Change the x/y screen coordinates to grid coordinates
            #     column = pos[0] // (WIDTH + MARGIN)
            #     row = pos[1] // (HEIGHT + MARGIN)
            #     # Set that location to one

            #     # click(column, row)

        screen.fill(BLACK)
        y = 0
        for row in grid:
            x = 0
            for cell in row:
                if cell.bomb == True:
                    pygame.Rect(screen, RED, [x, y], WIDTH)
                else:
                    pygame.draw.rect(screen, WHITE, [x, y], WIDTH)

                x += WIDTH
            y += HEIGHT
        clock.tick(60)

        pygame.display.flip()
    pygame.quit()


main()
