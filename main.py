import pygame
import time
pygame.init()

width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)

ball_width = 120

clock = pygame.time.Clock()
pygame.display.set_caption('A bit Racey')
screen = pygame.display.set_mode((width, height))

ball = pygame.image.load('intro_ball.png')


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
    x = (width * 0.45)
    y = (height * 0.8)
    x_change = 0
    y_change = 0
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
        y += y_change
        x += x_change

        screen.fill(white)
        update_ball(x, y)

        if x > width - ball_width or x < 0 or y > height - ball_width or y < 0:
            fail()



        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
