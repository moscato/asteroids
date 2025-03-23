import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable)
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
                return
        
        # get time delta
        dt = clock.tick(60) / 1000

        # Update the display
        pygame.display.flip()

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the player
        for obj in drawable:
            obj.draw(screen)

        # moves player
        updatable.update(dt)

if __name__ == "__main__":
    main()