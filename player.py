from circleshape import *
from constants import *

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialize both parent classes
        # pygame.sprite.Sprite.__init__(self)  # Initialize pygame.sprite.Sprite
        super().__init__(x, y, PLAYER_RADIUS)  # Initialize CircleShape

        self.rotation = 0
        
        # Add the Player to its containers
        self.add(*self.containers)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) # rotate left
        if keys[pygame.K_d]:
            self.rotate(dt) # rotate right
        if keys[pygame.K_w]:
            self.move(dt) # rotate right
        if keys[pygame.K_s]:
            self.move(-dt) # rotate right

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt







