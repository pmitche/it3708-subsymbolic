from ea.population import *
__author__ = "paulpm"


class EA(object):
    def __init__(self, mate_selection, adult_selection, phenotype):
        self.population = Population(mate_selection, adult_selection, phenotype)

    def run(self):
        self.compute()
        fittest = list(filter(lambda x: x.fitness == 1, self.population.individuals))
        if len(fittest) > 0:
            print("Found in generation", self.population.generation)
        else:
            print("Did not find within", self.population.generation, "generations")

    def compute(self):
        while self.population.generation < GENERATION_LIMIT and not self.population.target_reached():
            self.population.generation += 1
            self.population.breed()
            print(self.population)


    # reporting functions
    def report(self, best, avg, sd):
        print("generation:", self.generation, "best-f:", best.fitness(), "avg-f:", avg, "sd-f:", sd,
              "best-ph:", best.phenotype_string())
