from heapq import nlargest
from random import random, uniform, sample, choice
from numpy import std, mean
import math

__author__ = "paulpm"

#TODO: Rename individuals to adults?
#TODO: __init__ for each object
#TODO: Refactor MateSelection subclasses


class AdultSelection(object):
    def select(self, population, amount):
        """
        The adult selection routine should be defined at runtime as one of the subclasses of this class.
        :param population: the collective list of individuals in the current generation
        :param amount: the number of individuals that should be considered for selection
        :return: a new generation with parents from previous generation are possibly filtered
        """
        raise NotImplementedError


class FullGenerationalReplacement(AdultSelection):
    def select(self, population, amount):
        """
        All adults from previous generation die. All children make it to the adult pool.
        """
        return population.children


class OverProduction(AdultSelection):
    def select(self, population, amount):
        """
        All previous adults die, but m (amount) is smaller than n (population.children)
        """
        return nlargest(amount, population.children, key=lambda k: k.fitness)


class GenerationalMixing(AdultSelection):
    def select(self, population, amount):
        """
        The m adults from the previous generation do not die, so they and the n children
        compete in a free-for-all for the m adult spots in the next generation.
        """
        return nlargest(amount, population.individuals + population.children, key=lambda k: k.fitness)

ADULT_SELECTIONS = [FullGenerationalReplacement(), OverProduction(), GenerationalMixing()]





class MateSelection(object):
    def select(self, population):
        expval = self.expval(population)
        best = sum(expval)
        pick = uniform(0, best)
        current = 0
        for i in range(0, len(expval)):
            current += expval[i]
            if current > pick:
                return population.individuals[i]

    def expval(self, population):
        raise NotImplementedError


class FitnessProportionate(MateSelection):

    """def select(self, population):
        expval = self.expval(population)
        best = sum(expval)
        pick = uniform(0, best)
        current = 0
        for i in range(0, len(expval)):
            current += expval[i]
            if current > pick:
                return population.individuals[i]"""

    def expval(self, population):
        average = population.average_fitness
        return [x.fitness/average for x in population.individuals]


class SigmaScaling(MateSelection):
    def expval(self, population):
        m = mean(population.all_fitnesses)
        s = std(population.all_fitnesses)

        if s == 0:
            return list(map(lambda x: 1, population.all_fitnesses))
        else:
            return list(map(lambda x: 1 + (x - m)/(2*s), population.all_fitnesses))


class Boltzmann(MateSelection):
    def __init__(self, t):
        self.t = t

    def expval(self, population):
        x = [math.exp(x / self.t) for x in population.all_fitnesses]
        return [nom/mean(x) for nom in x]


class Tournament(MateSelection):
    def __init__(self, size, epsilon):
        self.size = size
        self.epsilon = epsilon

    def select(self, population):
        pick = sample(population.individuals, self.size)

        if uniform(0, 1) > self.epsilon:
            return max(pick, key=lambda k: k.fitness)
        else:
            return choice(pick)

    def expval(self, population):
        pass


