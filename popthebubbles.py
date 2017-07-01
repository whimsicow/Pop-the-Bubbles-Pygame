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
    font = pygame.font.Font(None, 100)

    max_bubbles = 100
    bubble_delay = 60
    bubble_cooldown = 0
    # pygame.mixer.music.load("bubblepop.wav")
    # font = pygame.font.Font(None, 36)
    score = []
    game_over = False

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
            self.radius = 25
        
        def update(self, score):
            screen.blit(self.image, (self.rect))
            if self.rect.y <= 0:
                self.rect.y = 0
                self.speed = 0

            elif self.rect.y >= 700 and self.speed == 0:
                game_over = True

            elif self.rect.y <= 710 and self.speed != 0:
                self.rect.y -= self.speed
                mouse_pos = pygame.mouse.get_pos()
                mouse_clicked = pygame.mouse.get_pressed()
                
                if self.rect.collidepoint(*mouse_pos) and mouse_clicked[0]:
                    pop = pygame.image.load("bubblepop.png").convert_alpha()
                    pop = pygame.transform.scale(pop, (135, 125))
                    self.image = pop
                    screen.blit(pop, (mouse_pos))
                    score.append(15)
                    self.kill()
                    print sum(score)

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

    # Game initialization
    close_window = False
    
    while not close_window:

        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                close_window = True
            
            elif game_over:
                game_over = True
        
        # Draw background
        screen.blit(background, (0,0))

        # Game logic
        if not game_over:
            for bubble in bubble_list:
                bubble.update(score)

            for bubble in bubble_list:
                bubble_list.remove(bubble)
                bubble.collide(bubble_list)
                bubble_list.add(bubble)

            bubble_cooldown -= 1
            if len(bubble_list) < max_bubbles and bubble_cooldown <= 0:
                for i in range(random.randint(1,3)):
                    Bubble("bubble.png", random.randint(5, 670), 710, random.randint(1,4))
                    bubble_cooldown = bubble_delay

        # Reload game display
        elif game_over:
        # If game over is true, draw game over
            print "Game over."
            text = font.render("Game over.", True, (midnight_blue), None)
            text_rect = text.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            allSprites.clear(screen, background)
            allSprites.update(score)
            screen.blit(text, [text_x, text_y])
            pygame.display.flip()
 
        else:
        # If game isn't over, draw this stuff.
            allSprites.clear(screen, background)
            allSprites.update()
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
