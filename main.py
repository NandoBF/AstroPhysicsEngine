import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

screen_center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
gravity = 10

circle_pos = screen_center

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    pygame.draw.circle(screen, "red", circle_pos, 40)

    circle_pos.y += gravity * dt

    #flip() the display to put on screen
    pygame.display.flip()

    #limit fps to 60
    #dt is delta time in seconds since last frame, used for framerate
    #independent physics
    dt = clock.tick(60) / 1000

pygame.quit()


