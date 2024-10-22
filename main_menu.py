import pygame
import button



pygame.init()

screen_width = 800
screen_height = 500
button_scale = 10 # x times
margin = 16 # pixels

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Button Demo')

startGame = None

#Menu buttons:
start_image = pygame.image.load("sprites/start.png").convert_alpha()
start_button = button.Button(margin, margin, start_image, button_scale)


exit_image = pygame.image.load("sprites/exit.png").convert_alpha()
exit_button = button.Button(margin, 2*margin+start_image.get_height()*button_scale, exit_image, button_scale)


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