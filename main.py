import sys
import pygame


pygame.init()

width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)

car_width = 73

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("intro_ball.png")


def update_ball(x, y):
    screen.blit(ball, (x, y))


def game_loop():
    x = (width * 0.45)
    y = (height * 0.8)
    x_change = 0
    y_change = 0
    error = False
    while not error:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if pygame.K_DOWN:
                    y_change = -5
                if pygame.K_UP:
                    y_change = 5
                if pygame.K_LEFT:
                    x_change = -5
                if pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    x_change = 0
                    y_change = 0

        y += y_change
        x += x_change

        screen.fill(black)
        update_ball(x, y)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
