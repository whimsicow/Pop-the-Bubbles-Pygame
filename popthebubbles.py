import pygame
import pygame,sys
from pygame.locals import *
import random

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Pop the Bubbles!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        smallText = pygame.font.Font("freesansbold.ttt",75)
        TextSurf, TextRect = text_objects("Click on the bubbles to pop them before they fill your screen.", smallText)
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

def main():
    pygame.init()

    width = 700
    height = 700
    midnight_blue = (25, 25, 112)

    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load("underwater.jpg").convert_alpha()
    background = pygame.transform.scale(background, (1280, 800))
    pygame.display.set_caption("Pop the Bubbles!")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)
    score = 0

    class Bubble_Creation(object):
        def __init__(self):
            self.bubble_list = []
            self.number_of_bubbles = 10

        def create(self):
            for i in range(self.number_of_bubbles):
                self.bubble_list.append(Bubble("bubble.png", random.randrange(10, 690), 710, 3))
                self.number_of_bubbles += 1


    class Bubble(pygame.sprite.Sprite):
        def __init__(self, image_file, x, y, speed):
            pygame.sprite.Sprite.__init__(self)
            self.speed = speed
            self.image = pygame.image.load(image_file).convert_alpha()
            self.image = pygame.transform.scale(self.image, (75, 75))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        
        def update(self, score):
            screen.blit(self.image, (self.rect))
            if self.rect.y <= 5:
                self.rect.y = 5

            elif self.rect.y <= 750:
                self.rect.y -= self.speed
                mouse_pos = pygame.mouse.get_pos()
                mouse_clicked = pygame.mouse.get_pressed()
                if self.rect.collidepoint(*mouse_pos) and mouse_clicked[0]:
                    pop = pygame.image.load("bubblepop.png").convert_alpha()
                    pop = pygame.transform.scale(pop, (135, 125))
                    self.image = pop
                    screen.blit(pop, (mouse_pos))
                    self.kill()
                    pygame.time.delay(10)
                    self.rect.y = 1000
                    self.rect.x = 1000

    all_bubbles = Bubble_Creation()
    all_bubbles.create() 

    # Game initialization
    stop_game = False
    
    while not stop_game:

        for event in pygame.event.get():
                # Event handling
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     all_bubbles = Bubble_Creation()
            #     all_bubbles.create() 

            if event.type == pygame.QUIT:
                stop_game = True

        screen.blit(background, (0,0))
        
        # Game logic

        for i in range(len(all_bubbles.bubble_list)): 
            all_bubbles.bubble_list[i].update(score)
            # all_bubbles = Bubble_Creation()
            # all_bubbles.create()


        

        # Draw background
        # screen.fill(midnight_blue)
        # screen.blit(background, (0,0))
        

        # Game display
        # screen.blit(bubble.image, (bubble.rect))
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
