from pygame.locals import *
import pygame
pygame.init()
running=True
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
screen=pygame.display.set_mode((640,240))
# while running:
#     for event in pygame.event.get():
#         print(event)
#         if event.type==pygame.QUIT:
#             running=False
#     screen.fill(YELLOW)
#     pygame.display.update() 

# EXAMPLE: Using render() method for text
# Create a font object
font = pygame.font.Font(None, 36)  # None uses default font, 36 is size

# Render text to a surface
text_surface = font.render("Hello PacMan!", True, MAGENTA)  # True = anti-aliasing, MAGENTA = color

# Get a rect for positioning
text_rect = text_surface.get_rect(center=(320, 120))

# Blit (draw) the text surface onto the screen
screen.blit(text_surface, text_rect)

# Update display to show the text
pygame.display.update()

# Keep window open for 3 seconds to see the text
pygame.time.wait(3000)
        
pygame.quit()