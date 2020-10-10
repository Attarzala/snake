import pygame
import time
import random

pygame.init()

width = 800
height = 600
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

ball_width = 120

clock = pygame.time.Clock()
pygame.display.set_caption('A bit Racey')
screen = pygame.display.set_mode((width, height))

ball = pygame.image.load('intro_ball.png')


def food(foodx, foody, foodw, foodh, color):
    pygame.draw.rect(screen, color, [foodx, foody, foodw, foodh])


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    text_type = pygame.font.SysFont(None, size=70)
    text_surf, text_rect = text_objects(text, text_type)
    text_rect.center = (width/2, height/2)
    screen.blit(text_surf, text_rect)
    pygame.display.update()

    time.sleep(3)

    game_loop()


def fail():
    message_display("You sack")


def update_ball(x, y):
    screen.blit(ball, (x, y))


def game_loop():
    ball_x = (width * 0.45)
    ball_y = (height * 0.8)
    x_change = 0
    y_change = 0

    food_spawnx = random.randrange(ball_width, width)
    food_spawny = random.randrange(ball_width, height)
    food_width = 150
    food_heigth = 150
    error = False

    while not error:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                error = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 5
                    x_change = 0
                if event.key == pygame.K_UP:
                    y_change = -5
                    x_change = 0
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    y_change = 0
        ball_y += y_change
        ball_x += x_change

        screen.fill(white)
        food(food_spawnx, food_spawny, food_width, food_heigth, red) # food(foodx, foody, foodw, foodh, color)
        update_ball(ball_x, ball_y)

        # Out of borders(screen atm)?
        if ball_x > width - ball_width or ball_x < 0 or ball_y > height - ball_width or ball_y < 0:
            fail()

        # Is the ball touching the food?
        if ball_x + ball_width > food_spawnx and ball_x < food_spawnx + food_width:
            if ball_y < food_spawny + food_width and ball_y + ball_width > food_spawny:
                print("Nisse")

        # if ball on food, spawn new food and delete old food from screen..?

        pygame.display.update()
        clock.tick(10)


game_loop()
pygame.quit()
quit()
