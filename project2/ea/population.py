__author__ = "paulpm"


class Population(object):
    def __init__(self, mate_selection, adult_selection):
        self.individuals = []
        self.children = []

    @property
    def all_fitnesses(self):
        return [x.fitness for x in self.individuals]

    @property
    def average_fitness(self):
        return sum(self.all_fitnesses) / len(self.all_fitnesses)