SIZE = WIDTH, HEIGHT = 1000, 600

COLORS = {
    "white":    (255, 255, 255),
    "black":    (0, 0, 0),
    "gray":     (160, 160, 160),
    "red":      (250, 0, 0),
    "green":    (0, 250, 0)
}

SPEED = {
    "boid":         4,
    "max_boid":     6,
    "predator":     6,
    "max_predator": 8
}

WEIGHTS = {
    "separation":   70,
    "alignment":    35,
    "cohesion":     20,
    "avoidance":    500,
    "fleeing":      500
}

NUM_BOIDS = 50
BOID_RADIUS = 5
PREDATOR_RADIUS = 10
NEARBY_RADIUS = BOID_RADIUS * 12
OBSTACLE_RADIUS = 20