import pygame
import random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)


def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


def wall_collision(c1, c2):
    return (c1[0] == c2[0]+10 or c1[1] == c2[1]+10 or c1[1] == -10 or c1[0] == -10)


def SCORE(win, score):
    largeFont = pygame.font.SysFont('comicsans', 30)  # Font object
    text = largeFont.render(str(score), 1, WHITE)  # create our text

    win.blit(text, (10, 10))  # draw the text to the screen
    pygame.display.update()


def main():

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    SPEED = 15

    done = True

    window = [600, 600]

    pygame.init()
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption("Cobrinha")

    snake = [(100, 100), (110, 100), (120, 100)]
    direction = LEFT
    SNAKE_SKIN = pygame.Surface((10, 10))
    SNAKE_SKIN.fill(WHITE)

    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill(RED)
    score = 0

    clock = pygame.time.Clock()

    while done:
        clock.tick(SPEED)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:

                if event.key == K_DOWN:
                    direction = DOWN

                if event.key == K_UP:
                    direction = UP

                if event.key == K_LEFT:
                    direction = LEFT

                if event.key == K_RIGHT:
                    direction = RIGHT

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0, 0))
            SPEED = SPEED+1
            score = score+1

        if wall_collision(snake[0], window):
            done = False

        for i in range(len(snake)-1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

        if direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)

        if direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)

        if direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        if direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])

        screen.fill(BLACK)
        screen.blit(apple, apple_pos)

        largeFont = pygame.font.SysFont('comicsans', 30)  # Font object
        text = largeFont.render(str(score), 1, WHITE)  # create our text
        screen.blit(text, (10, 10))  # draw the text to the screen

        for pos in snake:
            screen.blit(SNAKE_SKIN, pos)

        pygame.display.update()


main()
