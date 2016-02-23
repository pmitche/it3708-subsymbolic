from ea.population import *
__author__ = "paulpm"


class EA(object):
    def __init__(self, mate_selection, adult_selection, phenotype):
        self.population = Population(mate_selection, adult_selection, phenotype)

    def run(self):
        self.compute()
        fittest = list(filter(lambda x: x.fitness == 1, self.population.individuals))
        if len(fittest) > 0:
            # if logging is disabled, report the successful generation anyway
            """if not self.logging:
                best = self.population.best_individual()
                avg, sd = self.population.avg_sd_fitness()
                self.population.report(best, avg, sd)"""

            print("Found in generation", self.population.generation)
        else:
            print("Did not find within", self.population.generation, "generations")

    def compute(self):
        while self.population.generation < GENERATION_LIMIT and not self.population.target_reached():

            self.population.generation += 1
            self.population.breed()
            print(self.population.best_fitness)


    # reporting functions
    def report(self, best, avg, sd):
        print("generation:", self.generation, "best-f:", best.fitness(), "avg-f:", avg, "sd-f:", sd,
              "best-ph:", best.phenotype_string())

    def best_individual(self):
        return max(self.individuals, key=lambda x: x.fitness())

    def avg_sd_fitness(self):
        fitnesses = list(map(lambda x: x.fitness(), self.individuals))
        return numpy.mean(fitnesses), numpy.std(fitnesses)
