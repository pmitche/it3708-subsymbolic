import pygame
import math
import sys
from project1.boids.tmphelp import heading, rotate_polygon
from project1.boids.simulation import Simulation
from project1.boids.constants import *


class Triangle(object):
    def __init__(self, color, x, y, radius, rotation):
        self.color = color
        self.position = self.x, self.y = x, y
        self.radius = radius
        self.rotation = rotation

    def rotate(self, dr):
        self.rotation += dr
        self.rotation %= 2 * math.pi
        return self.rotation

    @property
    def polygon(self):
        return rotate_polygon(
            polygon=[
                (
                    self.x - self.radius,
                    self.y - self.radius
                ),
                (
                    self.x,
                    self.y + self.radius
                ),
                (
                    self.x,
                    self.y + self.radius
                ),
                (
                    self.x + self.radius,
                    self.y
                )

            ],
            r=self.rotation + (3.0 / 4.0) * math.pi,
            around=self.position
        )


def run(simulation):
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        screen.fill(COLORS["white"])
        simulation.update()
        for predator in simulation.predators:
            predator._update()

        for obstacle in simulation.obstacles:
            pygame.draw.circle(screen, COLORS["gray"], obstacle.position, obstacle.radius)

        for boid in simulation.boids:
            triangle = Triangle(
                color=COLORS["black"],
                x=boid.x,
                y=boid.y,
                radius=BOID_RADIUS,
                rotation=heading(boid.vel_x, boid.vel_y),
            )
            pygame.draw.polygon(screen, triangle.color, triangle.polygon)

        for predator in simulation.predators:
            triangle = Triangle(
                color=COLORS["red"],
                x=predator.x,
                y=predator.y,
                radius=PREDATOR_RADIUS,
                rotation=heading(predator.vel_x, predator.vel_y),
            )
            pygame.draw.polygon(screen, triangle.color, triangle.polygon)

        pygame.display.update()

        clock.tick(24)


def main():
    simulation = Simulation()
    simulation.add_obstacle()
    simulation.add_boids()
    simulation.add_predator()
    run(simulation)

if __name__ == "__main__":
    main()
