import pygame
import time
import random

pygame.init()

width = 800
height = 600
black = (0, 0, 0)
red = (255, 0, 0)  # Replace with apple
white = (255, 255, 255)

ball_width = 111


clock = pygame.time.Clock()
pygame.display.set_caption('A bit Racey')
screen = pygame.display.set_mode((width, height))

ball = pygame.image.load('intro_ball.png')
apple = pygame.image.load('apple.png')


def update_food(foodx, foody, foodw, foodh):
    pygame.draw.rect(screen, white, [foodx, foody, foodw, foodh])
    screen.blit(apple, (foodx, foody))


def score_counter(count):
    text_font = pygame.font.SysFont(None, size=30)
    score_counter = text_font.render("Score:" + str(count), True, black)
    screen.blit(score_counter, ((width-70)/2, 0))


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


def new_food_position():
    food_spawnx = random.randrange(ball_width, width-ball_width)
    food_spawny = random.randrange(ball_width, height-ball_width)
    return food_spawny, food_spawnx


def game_loop():
    ball_x = (width * 0.45)
    ball_y = (height * 0.8)
    x_change = 0
    y_change = 0
    food_spawny, food_spawnx = new_food_position()
    food_width = 38  # Actual size of apple.png
    tick = 60
    score = 0

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
        # food(food_spawnx, food_spawny, food_width, food_width, red)  # food(foodx, foody, foodw, foodh, color)
        update_ball(ball_x, ball_y)
        update_food(food_spawnx,food_spawny, food_width, food_width)
        score_counter(score)
        # Out of borders(screen atm)?
        if ball_x > width - ball_width or ball_x < 0 or ball_y > height - ball_width or ball_y < 0:
            fail()

        # Is the ball touching the food?
        if ball_x + ball_width > food_spawnx and ball_x < food_spawnx + food_width:
            if ball_y < food_spawny + food_width and ball_y + ball_width > food_spawny:
                print(tick)
                score += 1
                tick += 1
                food_spawny, food_spawnx = new_food_position()

        # if ball on food, spawn new food and delete old food from screen..?

        pygame.display.update()
        clock.tick(tick)



game_loop()
pygame.quit()
quit()
