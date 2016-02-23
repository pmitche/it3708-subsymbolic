from ea.genotype import *
from ea.phenotype import *
from ea.selection import *

__author__ = "paulpm"


class Population(object):
    def __init__(self, mate_selection, adult_selection, phenotype):
        self.mate_selection = MateSelection.factory(mate_selection)
        self.adult_selection = AdultSelection.factory(adult_selection)
        self.phenotype = phenotype
        self.individuals = []
        self.children = []
        self.generation = 0

        self.init_population()

    def init_population(self):
        children = []
        for _ in range(POPULATION_SIZE):
            children.append(Phenotype.factory(self.phenotype, Genotype(length=GENOTYPE_LENGTH)))
        self.children = children
        self.individuals = []
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

        self.select_adults(POPULATION_SIZE)

        for individual in self.individuals:
            individual.genotype.mutate()

    def crossover(self):
        p1 = self.mate_selection.select(self)
        p2 = self.mate_selection.select(self)

        geno1, geno2 = p1.genotype.crossover(p2.genotype)

        return Phenotype.factory(self.phenotype, geno1), Phenotype.factory(self.phenotype, geno2)
        #geno1, geno2 = crossover(p1.genotype.bits, p2.genotype.bits)
        #return OneMaxPhenotype(Genotype(length=GENOTYPE_LENGTH, bits=geno1)), OneMaxPhenotype(Genotype(length=GENOTYPE_LENGTH, bits=geno2))

    def select_adults(self, amount):
        self.individuals = self.adult_selection.select(self, amount)
        self.children = []

    @property
    def all_fitnesses(self):
        return [x.fitness for x in self.individuals]

    @property
    def average_fitness(self):
        return sum(self.all_fitnesses) / len(self.all_fitnesses)

    @property
    def best_fitness(self):
        return max(self.all_fitnesses)

    def target_reached(self):
        for x in self.individuals:
            if x.fitness >= 1.0:
                return True
        return False
