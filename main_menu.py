import pygame
import button



pygame.init()

screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Button Demo')

startGame = None

#Menu buttons:
start_image = pygame.image.load("sprites/vincentFlint.jpg").convert_alpha()
start_button = button.Button(10, 10, start_image, 0.1)

exit_image = pygame.image.load("sprites/min_mamma_uhh.png").convert_alpha()
exit_button = button.Button(300, 10, exit_image, 0.4)


running = True
while running: 

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            running = False
    
    # Graphics
    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        print('START')
        startGame = True
        running = False
    if exit_button.draw(screen):
        running = False



    pygame.display.update()

pygame.quit()