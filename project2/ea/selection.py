from heapq import nlargest

__author__ = "paulpm"

#TODO: Rename individuals to adults?


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
    raise NotImplementedError
