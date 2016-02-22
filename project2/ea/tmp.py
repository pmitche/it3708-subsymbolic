from random import randint


def individual(length):
    return [randint(0, 1) for _ in range(length)]


def population(size, length):
    return [individual(length) for _ in range(size)]


def fitness(individual):
    return sum(individual) / len(individual)


def average(population):
    return sum([fitness(x) for x in population]) / len(population)

pop = population(30, 10)
avg = average(pop)