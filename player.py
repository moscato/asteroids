from circleshape import *
from constants import *
from asteroid import Shot


class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialize both parent classes
        # pygame.sprite.Sprite.__init__(self)  # Initialize pygame.sprite.Sprite
        super().__init__(x, y, PLAYER_RADIUS)  # Initialize CircleShape

        self.rotation = 0

        self.shot_cooldown = 0  # Current cooldown time
        self.shot_delay = 0.3  # Time in seconds between shots
        
        # Add the Player to its containers
        self.add(*self.containers)

    # Sprite groups relevant to player
    all_sprites = pygame.sprite.Group()  # All game objects
    shots = pygame.sprite.Group()        # Just the bullets

    # Assign containers for Shot objects
    Shot.containers = all_sprites, shots

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
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

        if keys[pygame.K_LEFT]:
            self.rotate(-dt) # rotate left
        if keys[pygame.K_RIGHT]:
            self.rotate(dt) # rotate right
        if keys[pygame.K_UP]:
            self.move(dt) # moves forward
        if keys[pygame.K_DOWN]:
            self.move(-dt) # moves down
        if keys[pygame.K_SPACE] and self.shot_cooldown <= 0:
            self.shoot()
            self.shot_cooldown = self.shot_delay

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Create a Shot at the Player's current position
        shot = Shot(self.position.x, self.position.y)
        
        # Calculate velocity based on player's rotation
        direction = pygame.Vector2(0, -1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
        # print('FIRE!')







