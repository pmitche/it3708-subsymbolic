from heapq import nlargest
import numpy as np
from random import sample, choice
import ea.cfg as cfg

__author__ = "paulpm"


class AdultSelection(object):
    def select(self, population, amount):
        """
        The adult selection routine should be defined at runtime as one of the subclasses of this class.
        :param population: a Population object holding lists of adults and children
        :param amount: the number of individuals that should be considered for selection
        :return: a new generation with parents from previous generation are possibly filtered
        """
        raise NotImplementedError

    def factory(type):
        if type == "FullGenerational": return FullGenerationalReplacement()
        if type == "OverProduction": return OverProduction()
        if type == "GenerationalMixing": return GenerationalMixing()
        assert 0, "Invalid AdultSelection creation: " + type

    factory = staticmethod(factory)


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
        return nlargest(amount, population.adults + population.children, key=lambda k: k.fitness)


class MateSelection(object):
    def select(self, population):
        """
        Adapted from
        http://stackoverflow.com/questions/10324015/fitness-proportionate-selection-roulette-wheel-selection-in-python
        """
        expval = self.expval(population)
        best = sum(expval)
        pick = np.random.uniform(0, best)
        current = 0
        for i in range(len(expval)):
            current += expval[i]
            if current > pick:
                return population.adults[i]

    def expval(self, population):
        raise NotImplementedError

    def factory(type):
        if type == "FitnessProportionate": return FitnessProportionate()
        if type == "SigmaScaling": return SigmaScaling()
        if type == "Boltzmann": return Boltzmann(cfg.T)
        if type == "Tournament": return Tournament(cfg.TOURNAMENT_SIZE, cfg.EPSILON)
        assert 0, "Invalid MateSelection creation: " + type

    factory = staticmethod(factory)


class FitnessProportionate(MateSelection):
    def expval(self, population):
        average = population.average_fitness
        return [x.fitness/average for x in population.adults]


class SigmaScaling(MateSelection):
    def expval(self, population):
        avg = population.average_fitness
        sd = population.standard_deviation

        if sd == 0:
            return [1] * len(population.adults)

        return [1 + (k - avg)/(2*sd) for k in population.all_fitnesses]


class Boltzmann(MateSelection):
    def __init__(self, t):
        self.t = t

    def expval(self, population):
        x = [np.exp(k / self.t) for k in population.all_fitnesses]
        m = np.mean(x)
        return [fit/m for fit in x]


class Tournament(MateSelection):
    def __init__(self, size, epsilon):
        self.size = size
        self.epsilon = epsilon

    def select(self, population):
        chosen = sample(population.adults, self.size)

        if np.random.random_sample() > self.epsilon:
            return max(chosen, key=lambda k: k.fitness)

        return choice(chosen)

    def expval(self, population):
        pass




