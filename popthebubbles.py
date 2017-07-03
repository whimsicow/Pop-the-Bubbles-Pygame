import pygame, sys, random, time
from pygame.locals import *

width = 700
height = 700
screen = pygame.display.set_mode((width, height))
background = pygame.image.load("underwater.jpg").convert_alpha()
background = pygame.transform.scale(background, (1280, 800))
pygame.display.set_caption("Pop the Bubbles!")
clock = pygame.time.Clock()

def game_intro(background):
    font = pygame.font.Font(None, 100)
    smallfont = pygame.font.Font(None, 25)
    intromax_bubbles = 15
    
    class IntroBubble(pygame.sprite.Sprite):
        def __init__(self, image_file, x, y, speed):
            pygame.sprite.Sprite.__init__(self, self.containers)
            self.speed = speed
            self.image = pygame.image.load(image_file).convert_alpha()
            self.image = pygame.transform.scale(self.image, (75, 75))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        
        def update(self):
            screen.blit(self.image, (self.rect))
            if self.rect.y <= 0:
                self.kill()

            elif self.rect.y <= 710 and self.speed != 0:
                self.rect.y -= self.speed
                
    intro = True
    introbubble_list = pygame.sprite.Group()
    IntroBubble.containers = introbubble_list
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                intro = False

        screen.blit(background, (0,0))

        if len(introbubble_list) < intromax_bubbles:
                for i in range(random.randint(1,3)):
                    IntroBubble("bubble.png", random.randint(0, 680), 710, random.randint(1,4))
                
        text = font.render("Pop the Bubbles", True, (255, 255, 255), None)
        text_rect = text.get_rect()
        subtext = smallfont.render("Click on the bubbles to pop them before they reach the top of your screen.", True, (255, 255, 255), None)
        subtext_rect = subtext.get_rect()
        instructions = smallfont.render("Press any key to begin.", True, (255, 255, 255), None)
        instructions_rect = instructions.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2 - subtext_rect.height - instructions_rect . height
        subtext_x = screen.get_width() / 2 - subtext_rect.width / 2
        subtext_y = text_y + text_rect.height + subtext_rect.height
        instructions_x = screen.get_width() / 2 - instructions_rect.width / 2
        instructions_y = 650

        introbubble_list.update()
        screen.blit(text, [text_x, text_y])
        screen.blit(subtext, [subtext_x, subtext_y])
        screen.blit(instructions,[instructions_x, instructions_y] )
        pygame.display.flip()
        clock.tick(15)

def main(background):
    pygame.init()
    bubble_time = 0
    font = pygame.font.Font(None, 100)
    smallfont = pygame.font.Font(None, 30)
    max_bubbles = 100
    bubble_delay = 90
    bubble_cooldown = 0
    # pygame.mixer.music.load("bubblepop.wav")
    score = []
    game_over_list = []
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

            elif self.speed == 0 and self.rect.bottom >= screen.get_height():
                print "Game over."
                game_over_list.append(True)

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

        def collide(self, bubble_list):
            collision = pygame.sprite.spritecollide(self, bubble_list, False, pygame.sprite.collide_circle)
            for x in collision:
                if x.speed == 0:
                    self.speed = 0
    
    allSprites = pygame.sprite.Group()
    bubble_list = pygame.sprite.Group()
    Bubble.containers = allSprites, bubble_list
    # ScoreText.containers = allSprites

    # Game initialization
    close_window = False
    game_intro(background)

    while not close_window:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                close_window = True
            
            elif sum(score) >= 900:
                game_over = True
        
        for x in game_over_list:
                if x == True:
                    game_over = True
            
        # Draw background
        screen.blit(background, (0,0))
        scoretext = smallfont.render("Score: %d" % sum(score), True, (255, 255, 255), None)
        scoretext_rect = scoretext.get_rect()
        screen.blit(scoretext, [25, 665])

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
                    Bubble("bubble.png", random.randint(0, 670), 710, random.randint(1,4))
                    bubble_cooldown = bubble_delay

        # Reload game display
        elif game_over:
            # If game over and score over 900, draw you win.
            for bubble in bubble_list:
                bubble.speed = 0

            if sum(score) >= 900:
                text = font.render("You win!", True, (255, 255, 255), None)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                allSprites.clear(screen, background)
                allSprites.update(score)
                screen.blit(text, [text_x, text_y])
                pygame.display.flip()

            # If game over and bubbles have reached bottom of screen, draw game over
            else:
                text = font.render("Game over.", True, (255, 255, 255), None)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                allSprites.clear(screen, background)
                allSprites.update(score)
                screen.blit(text, [text_x, text_y])
                pygame.display.flip()
 
        else:
        # If game isn't over, render background and sprites.
            allSprites.clear(screen, background)
            allSprites.update(score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main(background)
