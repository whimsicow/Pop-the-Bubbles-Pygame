import pygame
import pygame,sys
from pygame.locals import *
import random
import time

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
    bubble_time = 0
    # font = pygame.font.Font(None, 36)
    # score = 0

    def tick_tock():
        last_time_ms = int(round(time.time() * 1000))
        while True:
            diff_time_ms = int(round(time.time() * 1000)) - last_time_ms
            if(diff_time_ms >= 4000):
                bubble_time += 1
                last_time_ms = int(round(time.time() * 1000))
            else:
                pass

    class Bubble_Creation(object):
        def __init__(self):
            self.bubble_list = []
            self.number_of_bubbles = 10
            # random.randint(1,4)

        def create(self):
            for i in range(self.number_of_bubbles):
                self.bubble_list.append(Bubble("bubble.png", random.randint(10, 690), 710, 3))
                self.number_of_bubbles += 1



    class Bubble(pygame.sprite.Sprite):
        def __init__(self, image_file, x, y, speed):
            pygame.sprite.Sprite.__init__(self, self.containers)
            self.speed = speed
            self.image = pygame.image.load(image_file).convert_alpha()
            self.image = pygame.transform.scale(self.image, (75, 75))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.radius = 20
        
        def update(self):
            screen.blit(self.image, (self.rect))
            if self.rect.y <= 0:
                self.rect.y = 0
                self.speed = 0

            elif self.rect.y <= 750 and self.speed != 0:
                self.rect.y -= self.speed
                mouse_pos = pygame.mouse.get_pos()
                mouse_clicked = pygame.mouse.get_pressed()
                
                if self.rect.collidepoint(*mouse_pos) and mouse_clicked[0]:
                    pop = pygame.image.load("bubblepop.png").convert_alpha()
                    pop = pygame.transform.scale(pop, (135, 125))
                    self.image = pop
                    screen.blit(pop, (mouse_pos))
                    self.kill()
        
        def collide(self, bubble_list):
            collision = pygame.sprite.spritecollide(self, bubble_list, False, pygame.sprite.collide_circle)
            for x in collision:
                if x.speed == 0:
                    self.speed = 0


    # all_bubbles = [Bubble_Creation(), Bubble_Creation()]
    # all_bubbles.create() 
    allSprites = pygame.sprite.Group()
    bubble_list = pygame.sprite.Group()

    Bubble.containers = allSprites, bubble_list

    max_bubbles = 500
    bubble_delay = 60
    bubble_cooldown = 0

    # Game initialization
    stop_game = False
    
    while not stop_game:

        for event in pygame.event.get():
            # Event handling
            # if event.type == pygame.MOUSEBUTTONDOWN:
        
            if event.type == pygame.QUIT:
                stop_game = True
        
        # Draw background
        screen.blit(background, (0,0))

        # Game logic
        for bubble in bubble_list:
            bubble.update()

        for bubble in bubble_list:
            bubble_list.remove(bubble)
            bubble.collide(bubble_list)
            bubble_list.add(bubble)

        bubble_cooldown -= 1
        if len(bubble_list) < max_bubbles and bubble_cooldown <= 0:
            for i in range(random.randint(1,3)):
                Bubble("bubble.png", random.randint(5, 670), 680, random.randint(2,5))
                bubble_cooldown = bubble_delay

            # for i in range(len(all_bubbles.bubble_list)): 
            #     all_bubbles.bubble_list[i].update()
            # # all_bubbles = Bubble_Creation()
            # all_bubbles.create()
        

        # Reload game display
        allSprites.clear(screen, background)
        allSprites.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
