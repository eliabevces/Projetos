import pygame
import random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(50, 590)
    return (x//10 * 10, y//10 * 10)


def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


def wall_collision(c1, c2):
    return (c1[0] == c2[0]+10 or c1[1] == c2[1]+10 or c1[1] == 40 or c1[0] == -10)


def write(screen, txt, color, pos):
    largeFont = pygame.font.SysFont('comicsans', 30)  # Font object
    text = largeFont.render(txt, 1, color)  # create our text
    screen.blit(text, pos)


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

    snake = [(300, 300), (310, 300), (320, 300)]
    direction = LEFT
    SNAKE_SKIN = pygame.Surface((10, 10))
    SNAKE_SKIN.fill(WHITE)

    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill(RED)
    score = 0

    clock = pygame.time.Clock()

    # open previous highscore and read it
    f = open('score.txt', 'r')
    H_score = int(f.read())
    f.close()

    while done:

        clock.tick(SPEED)  # FPS

        for event in pygame.event.get():
            # close game
            if event.type == QUIT:
                pygame.quit()

            # key pressing
            if event.type == KEYDOWN:

                if event.key == K_DOWN:
                    if direction != UP:
                        direction = DOWN

                if event.key == K_UP:
                    if direction != DOWN:
                        direction = UP

                if event.key == K_LEFT:
                    if direction != RIGHT:
                        direction = LEFT

                if event.key == K_RIGHT:
                    if direction != LEFT:
                        direction = RIGHT

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0, 0))
            SPEED = SPEED+0.5
            score = score+1

        for i in range(len(snake)-1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

        if direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)

        elif direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)

        elif direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        elif direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])

        # fill screen with background color
        screen.fill(BLUE)
        # print apple
        screen.blit(apple, apple_pos)

        # score
        write(screen, str(score), WHITE, (10, 10))

        # HIGH SCORE
        write(screen, 'HIGHSCORE' + str(H_score), WHITE, (430, 10))

        # movement
        for pos in snake:
            screen.blit(SNAKE_SKIN, pos)

        # score line
        pygame.draw.lines(screen, WHITE, True, [(0, 40), (600, 40)], 5)

        # WALL Collision - 'die'
        if wall_collision(snake[0], window):
            done = False
        pygame.display.update()

        # touch itself
        for i in range(len(snake)-1, 0, -1):
            if snake[0] == snake[i]:
                done = False

    # save highscore
    if score > H_score:
        f = open('score.txt', 'w')
        f.write(str(score))
        f.close()


main()
