from ea.genotype import *
from ea.phenotype import *
from ea.selection import *
import numpy as np
import heapq

__author__ = "paulpm"


class Population(object):
    def __init__(self, mate_selection, adult_selection, phenotype):
        self.mate_selection = MateSelection.factory(mate_selection)
        self.adult_selection = AdultSelection.factory(adult_selection)
        self.phenotype = phenotype
        self.generation = 0
        self.adults = []
        self.children = []

        self.reset()

    def reset(self):
        children = []
        for _ in range(POPULATION_SIZE):
            children.append(Phenotype.factory(self.phenotype, Genotype(length=GENOTYPE_LENGTH)))
        self.children = children
        self.adults = []
        self.generation = 0

    def breed(self):
        if len(self.children) == 0:
            new_gen = []
            while len(new_gen) < POPULATION_SIZE:
                first, second = self.crossover()
                new_gen.append(first)
                if len(new_gen) < POPULATION_SIZE:
                    new_gen.append(second)

            self.children = new_gen

        elites = self.elites()
        self.select_adults(POPULATION_SIZE - len(elites))

        for adult in self.adults:
            adult.genotype.mutate()
            
        self.adults += elites

    def crossover(self):
        p1 = self.mate_selection.select(self)
        p2 = self.mate_selection.select(self)

        geno1, geno2 = p1.genotype.crossover(p2.genotype)

        return Phenotype.factory(self.phenotype, geno1), Phenotype.factory(self.phenotype, geno2)

    def select_adults(self, amount):
        self.adults = self.adult_selection.select(self, amount)
        self.children = []

    def elites(self):
        if not ELITISM:
            return []
        best = heapq.nlargest(ELITISM_SIZE, self.adults, key=lambda k: k.fitness)
        return [Phenotype.factory(self.phenotype, x.genotype) for x in best]

    @property
    def all_fitnesses(self):
        return [x.fitness for x in self.adults]

    @property
    def average_fitness(self):
        return sum(self.all_fitnesses) / len(self.all_fitnesses)

    @property
    def best_fitness(self):
        return max(self.all_fitnesses)

    @property
    def best_phenotype(self):
        return max(self.adults, key=lambda k: k.fitness)

    @property
    def standard_deviation(self):
        return np.std(self.all_fitnesses)

    def target_reached(self):
        for x in self.adults:
            if x.fitness >= 1.0:
                return True
        return False

    def __repr__(self):
        return "Generation: {} | Best phenotype: {} | Best fitness: {} | Average fitness: {} | Standard deviation: {}"\
            .format(
                self.generation,
                self.best_phenotype.genotype.bits,
                self.best_fitness,
                self.average_fitness,
                self.standard_deviation
            )
