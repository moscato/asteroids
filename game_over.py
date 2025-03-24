import pygame
import pygame.font
import sys
import subprocess
import os

def get_final_score():
    if len(sys.argv) > 1:
        return int(sys.argv[1])  # Convert score from argument
    return 0

pygame.init()

# Get the score from the argument
score = get_final_score()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Over")

# Font setup
font = pygame.font.SysFont("Arial", 50)
game_over_text = font.render("GAME OVER :(", True, (255, 0, 0))

score_font = pygame.font.SysFont("Arial", 30)
score_text = score_font.render(f"Final Score: {score}", True, (255, 255, 255))

# Button setup
button_font = pygame.font.SysFont("Arial", 30)
button_text = button_font.render("Again?", True, (255, 255, 255))
button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 
                                 SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2 - 50))
    
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 
                             SCREEN_HEIGHT // 2 - score_text.get_height() // 2))

    # Draw button
    pygame.draw.rect(screen, (0, 255, 0), button_rect)
    screen.blit(button_text, (button_rect.x + 25, button_rect.y + 10))

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                subprocess.run(["python", "main.py"])
                sys.exit()
                os._exit(0)

pygame.quit()
sys.exit()
os._exit(0)



