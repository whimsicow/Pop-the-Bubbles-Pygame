import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (1280, 800))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class 
def main():
    width = 800
    height = 800
    midnight_blue = (25, 25, 112)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    BG = Background("underwater.jpg", [0,0])
    pygame.display.set_caption("Pop the Bubbles!")
    clock = pygame.time.Clock()

    # Game initialization
    bubble = pygame.image.load("bubble.png")
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(midnight_blue)
        screen.blit(BG.image, BG.rect)
        

        # Game display
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
