from circleshape import *
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(*self.containers)
        # print(f"Asteroid created at x={x}, y={y}, radius={radius}")

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), [self.position.x, self.position.y], self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        import random

        random_angle = random.uniform(20, 50)
        
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2
        
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2 * 1.2


            


      

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.velocity = pygame.Vector2(0, 0)
        self.add(*self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * -dt



