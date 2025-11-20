import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from logger import log_event
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        rand = random.uniform(20, 50)

        new1 = pygame.Vector2.rotate(self.velocity, rand)
        new2 = pygame.Vector2.rotate(self.velocity, -rand)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid1 =  Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid1.velocity = new1 * 1.2

        split_asteroid2 =  Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid2.velocity = new2 * 1.2

        