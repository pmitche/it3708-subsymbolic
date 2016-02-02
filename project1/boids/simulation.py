import random
import math
import numpy as np
from project1.boids.constants import *


class Boid(object):
    def __init__(self, x, y, simulation):
        self.position = self.x, self.y = x, y
        self.simulation = simulation
        self.speed = SPEED["boid"]
        self.max_speed = SPEED["max_boid"]
        self.velocity = self.vel_x, self.vel_y = random.random() * self.speed, random.random() * self.speed

    def separation(self, other_boids):
        separation = [0.0, 0.0]
        for other, dist in other_boids:
            if dist == 0:
                separation = np.subtract(separation, other.velocity)
            else:
                separation = np.subtract(separation, np.divide(np.subtract(other.position, self.position), dist))

        return separation

    def alignment(self, other_boids):
        if len(other_boids) == 0:
            return self.velocity

        # TODO: Modify to numpy
        align_x = sum([other.vel_x for other, _ in other_boids]) / len(other_boids)
        align_y = sum([other.vel_y for other, _ in other_boids]) / len(other_boids)
        return [align_x, align_y]

    def cohesion(self, other_boids):
        if len(other_boids) == 0:
            return self.position

        # TODO: Modify to numpy
        coh_x = sum([other.x for other, _ in other_boids]) / len(other_boids)
        coh_y = sum([other.y for other, _ in other_boids]) / len(other_boids)
        return [coh_x - self.x, coh_y - self.y]

    def limit_velocity(self):
        max_vel = max(abs(self.vel_x), abs(self.vel_y))
        self.vel_x = (self.vel_x / max_vel) * self.max_speed
        self.vel_y = (self.vel_y / max_vel) * self.max_speed

    def move(self):
        self.x = (self.x + self.vel_x) % WIDTH
        self.y = (self.y + self.vel_y) % HEIGHT

    def update(self, other_boids, obstacles, predators):
        sep_x, sep_y = self.separation(other_boids)
        align_x, align_y = self.alignment(other_boids)
        coh_x, coh_y = self.cohesion(other_boids)
        avoid_x, avoid_y = [-self.y, self.x] if obstacles else [0.0, 0.0]
        flee_x, flee_y = self.separation(predators) if predators else [0.0, 0.0]

        self.vel_x += sum([
            sep_x * WEIGHTS["separation"],
            align_x * WEIGHTS["alignment"],
            coh_x * WEIGHTS["cohesion"],
            avoid_x * WEIGHTS["avoidance"],
            flee_x * WEIGHTS["fleeing"]
        ])

        self.vel_y += sum([
            sep_y * WEIGHTS["separation"],
            align_y * WEIGHTS["alignment"],
            coh_y * WEIGHTS["cohesion"],
            avoid_y * WEIGHTS["avoidance"],
            flee_y * WEIGHTS["fleeing"]
        ])

        if abs(self.vel_x) > self.max_speed or abs(self.vel_y) > self.max_speed:
            self.limit_velocity()
        self.move()


class Predator(Boid):
    def __init__(self, x, y, simulation):
        super(Predator, self).__init__(x, y, simulation)
        self.speed = SPEED["predator"]
        self.max_speed = SPEED["max_predator"]
        self.velocity = self.vel_x, self.vel_y = random.random() * self.speed, random.random() * self.speed

    # TODO: Fix this
    def _update(self):
        other_boids = []
        for boid in self.simulation.boids:
            dist = distance(self.position, boid.position)
            if dist < NEARBY_RADIUS * 2:
                other_boids.append((boid, dist))

        obstacles = []
        for obstacle in obstacles:
            dist = distance(self.position, obstacle.position)
            if dist < OBSTACLE_RADIUS * 3:
                obstacles.append((obstacle, dist))

        align_x, align_y = self.alignment(other_boids) if other_boids else [0.0, 0.0]
        coh_x, coh_y = self.cohesion(other_boids) if other_boids else [0.0, 0.0]
        avoid_x, avoid_y = [-self.vel_y, self.vel_x] if obstacles else [0.0, 0.0]

        #TODO: Update velocity method
        self.vel_x += sum([
            align_x * WEIGHTS["alignment"],
            coh_x * WEIGHTS["cohesion"],
            avoid_x * WEIGHTS["avoidance"]
        ])

        self.vel_y += sum([
            align_y * WEIGHTS["alignment"],
            coh_y * WEIGHTS["cohesion"],
            avoid_y * WEIGHTS["avoidance"]
        ])

        self.limit_velocity()
        self.move()


class Obstacle(object):
    def __init__(self, x, y, radius):
        self.position = self.x, self.y = x, y
        self.radius = radius

    def intersects(self, x, y):
        return distance((x, y), self.position) <= self.radius * 2


class Simulation(object):
    def __init__(self):
        self.boids = []
        self.predators = []
        self.obstacles = []

        self.add_boids()

    @property
    def entities(self):
        return self.boids + self.predators

    def update(self):
        for boid in self.boids:
            other_boids = []
            close_obstacle = None
            predators = []

            for obstacle in self.obstacles:
                if obstacle.intersects(boid.x, boid.y):
                    close_obstacle = obstacle
                    break

            for other_boid in self.boids:
                if other_boid == boid:
                    continue #TODO: Switch this around?
                dist = distance(other_boid.position, boid.position)
                if dist < NEARBY_RADIUS:
                    other_boids.append((other_boid, dist))

            for predator in self.predators:
                dist = distance(predator.position, boid.position)
                if dist < NEARBY_RADIUS:
                    predators.append((predator, dist))

            boid.update(other_boids, close_obstacle, predators)

    def add_boids(self):
        i = NUM_BOIDS
        while i:
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            if self.free(x, y):
                self.boids.append(Boid(x, y, self))
                i -= 1

    def add_predator(self):
        while True:
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            if self.free(x, y):
                self.predators.append(Predator(x, y, self))
                break

    def add_obstacle(self):
        while True:
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            if self.free(x, y):
                self.obstacles.append(Obstacle(x, y, radius=OBSTACLE_RADIUS))
                break

    def free(self, x, y):
        for entity in self.entities:
            if entity.x == x and entity.y == y:
                return False

        for obstacle in self.obstacles:
            if obstacle.intersects(x, y):
                return False

        return True


# TODO: Move this
def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
