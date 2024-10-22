import pygame
import button
import os

def draw_text(prompt: str, font, color, x, y):
    pass

pygame.init()


vertical_list = ["sprites/start.png",
          "sprites/exit.png"]



screen_width = 800
screen_height = 800
button_scale = 10 # x times
margin = 16 # pixels
directory = os.path.dirname(os.path.realpath(__file__))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Button Demo')


startGame = False

#Menu buttons:
start_image = pygame.image.load(directory + "\\sprites\\start.png").convert_alpha()
start_button = button.Button(margin, margin, start_image, button_scale)

exit_image = pygame.image.load(directory + "\\sprites\\exit.png").convert_alpha()
exit_button = button.Button(margin, 2*margin+start_image.get_height()*button_scale, exit_image, button_scale)

arrow_left_image = pygame.image.load(directory + "\\sprites\\arrow.png").convert_alpha()
arrow_left = button.Button(margin, 3*margin+start_image.get_height()*button_scale+exit_image.get_height()*button_scale, arrow_left_image, button_scale)

arrow_right_image = pygame.transform.flip(arrow_left_image, True, False).convert_alpha()
arrow_right = button.Button(2*margin+arrow_left_image.get_width()*button_scale, 3*margin+start_image.get_height()*button_scale+exit_image.get_height()*button_scale, arrow_right_image, button_scale)



running = True
while running: 

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            running = False
    
    # Graphics
    screen.fill((202, 228, 241))

    start_button.draw(screen)
    exit_button.draw(screen)
    arrow_left.draw(screen)
    arrow_right.draw(screen)

    if start_button.pressed():
        print('START')
        startGame = True
        running = False
    if exit_button.pressed():
        print("EXIT")
        running = False
    if arrow_left.pressed():
        print("Left arrow")
    if arrow_right.pressed():
        print("Right arrow")

    pygame.display.update()

pygame.quit()