import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 1000,600

# Screen
SCREEN = pygame.display.set_mode(SIZE)

# R,G,B - Red, Green, Blue
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255
COLOR = 150, 100, 200

rect_x = 0
rect_y = 0

SPEED = 0.4

move_x = 0
move_y = 0

while True:

    SCREEN.fill(COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = SPEED
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -SPEED
                move_y = 0

            elif event.key == pygame.K_DOWN:
                move_y = SPEED
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -SPEED
                move_x = 0

    pygame.draw.rect(SCREEN, BLACK, [rect_x, rect_y, 50,50])
    # pygame.draw.circle(SCREEN, RED, [100,100], 60)
    rect_x += move_x
    rect_y += move_y

    if rect_x > WIDTH - 50:
        move_x = -SPEED
    elif rect_x < 0:
        move_x = SPEED

    if rect_y > HEIGHT - 50:
        move_y = -SPEED
    elif rect_y < 0:
        move_y = SPEED

    # update screen
    pygame.display.flip()