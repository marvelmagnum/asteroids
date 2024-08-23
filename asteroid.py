import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        split_vec1 = self.velocity.rotate(split_angle)
        split_vec2 = self.velocity.rotate(-split_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid1.velocity = split_vec1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid2.velocity = split_vec2 * 1.2