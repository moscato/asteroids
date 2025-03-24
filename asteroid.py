from circleshape import *
from constants import SHOT_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(*self.containers)
        # print(f"Asteroid created at x={x}, y={y}, radius={radius}")

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), [self.position.x, self.position.y], self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
      

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.velocity = pygame.Vector2(0, 0)
        self.add(*self.containers)

    def draw(self, screen):
        # Draw the shot as a small white circle
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * -dt



