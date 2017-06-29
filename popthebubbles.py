import pygame
import time
import random


class Bubble(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        # self.speed_x = speed
        self.speed_y = speed
        self.image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        # self.radius = radius
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.pressed = False
    
    def update(self):
        if self.rect.y <= 750:
            self.rect.y -= self.speed_y
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        if self.rect.collidepoint(*mouse_pos) and mouse_clicked:
            self.kill()

def main():
    width = 700
    height = 700
    midnight_blue = (25, 25, 112)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
   #  background = pygame.image.load("underwater.jpg").convert_alpha()
    # background = pygame.transform.scale(background, (1280, 800))
    pygame.display.set_caption("Pop the Bubbles!")
    clock = pygame.time.Clock()

    bubble_list = pygame.sprite.RenderPlain()
    # bubble = Bubble("bubble.png", random.randrange(700), 700, 5)
    # bubble_list.append(bubble)

    # Game initialization
    stop_game = False
    
    while not stop_game:
        for event in pygame.event.get():
            for i in range(50):
                # bubble.update()
                bubble = Bubble("bubble.png", random.randrange(10, 690), 710, 5)
                bubble_list.add(bubble)
                # Event handling
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #      bubble.update()

            if event.type == pygame.QUIT:
                stop_game = True
        for bubble in bubble_list:
            bubble.update()


        # Game logic

        # Draw background
        screen.fill(midnight_blue)
        # screen.blit(background, (0,0))
        

        # Game display
        screen.blit(bubble.image, (bubble.rect))
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
