import pygame
import pygame.font
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
import subprocess

def open_game_over(score):
    subprocess.Popen(["python", "game_over.py", str(score)])


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    score = 0

    pygame.font.init()
    font = pygame.font.SysFont("Arial", 30)

    def draw_score(screen, score):
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable,)

    asteroid = Asteroid(100, 100, 30)
    asteroid.velocity = pygame.Vector2(50, 50)  # Moves diagonally
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while SCREEN_WIDTH == 1280:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # return
                sys.exit()
        
        # Get time delta
        dt = clock.tick(60) / 1000

        draw_score(screen, score)

        # Update the display
        pygame.display.flip()

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Update all updatable sprites
        updatable.update(dt)

        # Draw all drawable sprites
        for obj in drawable:
            obj.draw(screen)

        # Check for collisions between player and asteroids
        for obj in drawable:
            if isinstance(obj, Asteroid) and player.collides_with(obj):
                print("Game over!")
                open_game_over(score)
                sys.exit()
        
        # Check for collisions between shot and asteroids
        for asteroid in [obj for obj in drawable if isinstance(obj, Asteroid)]:
            for shot in shots:
                if shot.collides_with(asteroid):
                    # print("HIT!")
                    score += 1
                    asteroid.split()
                    shot.kill()

    pygame.quit()
    sys.exit()
    os._exit(0)

if __name__ == "__main__":
    main()