# Level 3

import pygame, sys, random, time
from pygame.locals import *
import popthebubbles

width = 700
height = 700
screen = pygame.display.set_mode((width, height))
background = pygame.image.load("underwater.jpg").convert_alpha()
background = pygame.transform.scale(background, (1280, 800))
pygame.display.set_caption("Pop the Bubbles!")
clock = pygame.time.Clock()

def level3(background, score):
    pygame.init()
    # Sets up variables and font specifications
    font = pygame.font.Font(None, 100)
    smallfont = pygame.font.Font(None, 30)
    # Sets timer for new batch of bubbles to be created every 2 seconds
    bubble_drop = 25
    pygame.time.set_timer(bubble_drop, 2000)
    game_over_list = []
    game_over = False
    
    # Main game Bubble specifications
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
            # Stops bubbles once they reach the top of the screen, sets speed to 0
            if self.rect.y <= 0:
                self.rect.y = 0
                self.speed = 0
            # Indicates game is over once stopped bubbles reach the bottom of the screen
            elif self.speed == 0 and self.rect.bottom >= 690:
                game_over_list.append(True)
            # Allows bubbles to float from the bottom to the top of the screen based on specified speed
            elif self.rect.y <= 710 and self.speed != 0:
                self.rect.y -= self.speed
                # Specifies if mouse has been clicked, gets position of mouse
                mouse_pos = pygame.mouse.get_pos()
                mouse_clicked = pygame.mouse.get_pressed()
                # Collision detection: pops bubbles if they have been clicked
                if self.rect.collidepoint(*mouse_pos) and mouse_clicked[0]:
                    pop = pygame.image.load("bubblepop.png").convert_alpha()
                    pop = pygame.transform.scale(pop, (135, 125))
                    # Shows pop image once bubbles are clicked
                    self.image = pop
                    screen.blit(pop, (mouse_pos))
                    score.append(15)
                    # Removes clicked bubble from all groups
                    self.kill()
        
        # Stops bubbles once they collide with other stopped bubbles
        def collide(self, bubble_list):
            collision = pygame.sprite.spritecollide(self, bubble_list, False, pygame.sprite.collide_circle)
            for x in collision:
                if x.speed == 0:
                    self.speed = 0
    
    # Adds bubbles to sprite group
    allSprites = pygame.sprite.Group()
    bubble_list = pygame.sprite.Group()
    Bubble.containers = allSprites, bubble_list

    # Game initialization
    close_window = False

    while not close_window:
        for event in pygame.event.get():
            # Ends game if user exits screen
            if event.type == pygame.QUIT:
                close_window = True
            # Creates new batch of bubbles if 2.5 seconds have passed
            if event.type == bubble_drop:
                for i in range(random.randint(1,3)):
                    Bubble("bubble.png", random.randint(0, 670), 710, random.randint(1,4))
            # Indicates game is over once score of 900 reached
            elif sum(score) >= 3000:
                game_over = True
        # Checks to see if any bubbles have reached the bottom of the scren, if so, indicates game is over
        for x in game_over_list:
            if x == True:
                game_over = True
            
        # Draw background and score counter
        screen.blit(background, (0,0))
        scoretext = smallfont.render("Score: %d" % sum(score), True, (255, 255, 255), None)
        scoretext_rect = scoretext.get_rect()
        screen.blit(scoretext, [25, 665])

        # Game logic
        if not game_over:
            for bubble in bubble_list:
                bubble.update(score)
    # Iterates through bubble list, checks for collisions, removes bubble and adds it back to ensure it does not detect the bubble colliding with itself
            for bubble in bubble_list:
                bubble_list.remove(bubble)
                bubble.collide(bubble_list)
                bubble_list.add(bubble)

        # Reload game display
        elif game_over:
            # Stops all bubbles once game is over
            for bubble in bubble_list:
                bubble.speed = 0
            # If game over and score over 3000, draw you win
            if sum(score) >= 3000:
                text = font.render("You win!", True, (255, 255, 255), None)
                text_rect = text.get_rect()
                subtext = smallfont.render("Press any key to play again.", True, (255, 255, 255), None)
                subtext_rect = subtext.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                subtext_x = screen.get_width() / 2 - subtext_rect.width / 2
                subtext_y = text_y + text_rect.height + subtext_rect.height
                allSprites.clear(screen, background)
                allSprites.update(score)
                screen.blit(text, [text_x, text_y])
                screen.blit(subtext, [subtext_x, subtext_y])
                pygame.display.flip()
                for event in pygame.event.get():
                    # Ends game if user exits screen
                    if event.type == pygame.QUIT:
                        close_window = True
                    # Loops through game again if key pressed
                    elif event.type == pygame.KEYDOWN:
                        score = []
                        game_over_list = []
                        allSprites.empty()
                        bubble_list.empty()
                        game_over = False

            # If game over and stopped bubbles have reached bottom of screen, draw game over
            else:
                text = font.render("Game over.", True, (255, 255, 255), None)
                text_rect = text.get_rect()
                subtext = smallfont.render("Press any key to play again.", True, (255, 255, 255), None)
                subtext_rect = subtext.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                subtext_x = screen.get_width() / 2 - subtext_rect.width / 2
                subtext_y = text_y + text_rect.height + subtext_rect.height
                allSprites.clear(screen, background)
                allSprites.update(score)
                screen.blit(text, [text_x, text_y])
                screen.blit(subtext, [subtext_x, subtext_y])
                pygame.display.flip()
                for event in pygame.event.get():
                    # Ends game if user exits screen
                    if event.type == pygame.QUIT:
                        close_window = True
                  
                    # Loops through game again if key pressed
                    elif event.type == pygame.KEYDOWN:
                        score = []
                        game_over_list = []
                        allSprites.empty()
                        bubble_list.empty()
                        popthebubbles.main(background)
                        game_over = False
 
        else:
        # If game isn't over, render background and sprites.
            allSprites.clear(screen, background)
            allSprites.update(score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()