import pygame
import time
import random

def main():
    width = 700
    height = 700
    midnight_blue = (25, 25, 112)
    number_of_bubbles = 30

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load("underwater.jpg").convert_alpha()
    background = pygame.transform.scale(background, (1280, 800))
    pygame.display.set_caption("Pop the Bubbles!")
    clock = pygame.time.Clock()

    class Bubble_Creation(object):
        def __init__(self):
            self.bubble_list = []

        def create(self, number_of_bubbles):
            for i in range(number_of_bubbles):
                self.bubble_list.append(Bubble("bubble.png", random.randrange(10, 690), 710, 3))

    class Bubble(pygame.sprite.Sprite):
        def __init__(self, image_file, x, y, speed):
            pygame.sprite.Sprite.__init__(self)
            self.speed = speed
            self.image = pygame.image.load(image_file).convert_alpha()
            self.image = pygame.transform.scale(self.image, (75, 75))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        
        def update(self):
            screen.blit(self.image, (self.rect))
            if self.rect.y == 10:
                self.rect.y = 10

            elif self.rect.y <= 750:
                self.rect.y -= self.speed
                mouse_pos = pygame.mouse.get_pos()
                mouse_clicked = pygame.mouse.get_pressed()[0]
                if self.rect.collidepoint(*mouse_pos) and mouse_clicked:
                    pop = pygame.image.load("bubblepop.png").convert_alpha()
                    pop = pygame.transform.scale(pop, (135, 125))
                    self.image = pop
                    screen.blit(pop, (mouse_pos))
                    self.rect.y = -200
                    self.rect.x = -200

    all_bubbles = Bubble_Creation()
    all_bubbles.create(number_of_bubbles) 

    # Game initialization
    stop_game = False
    
    while not stop_game:

        for event in pygame.event.get():
                # Event handling
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #      bubble.update()

            if event.type == pygame.QUIT:
                stop_game = True

        screen.blit(background, (0,0))

        for i in range(len(all_bubbles.bubble_list)):
            all_bubbles.bubble_list[i].update()


        # Game logic

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
