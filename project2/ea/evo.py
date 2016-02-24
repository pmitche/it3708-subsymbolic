from ea.population import *
import ea.cfg as cfg
import matplotlib.pyplot as pyplot
__author__ = "paulpm"


class EA(object):
    def __init__(self, mate_selection, adult_selection, phenotype):
        self.population = Population(mate_selection, adult_selection, phenotype)
        self.data = {
            "best":      [],
            "average":   [],
            "deviation": []
        }

    def evolve(self):
        while self.population.generation < cfg.GENERATION_LIMIT and not self.population.target_reached():
            self.population.generation += 1
            self.population.breed()
            print(self.population)

            self.data["best"].append(self.population.best_fitness)
            self.data["average"].append(self.population.average_fitness)
            self.data["deviation"].append(self.population.standard_deviation)

        if self.population.target_reached():
            print("Target reached in generation: {}".format(self.population.generation))
        else:
            print("Target not reached within {} generations".format(self.population.generation))

        self.plot()

    def plot(self):
        pyplot.plot(self.data["best"], label="Best")
        pyplot.plot(self.data["average"], label="Average")
        pyplot.plot(self.data["deviation"], label="Standard deviation")
        pyplot.legend(bbox_to_anchor=(0., 1.01, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
        pyplot.xlabel("Generations")
        pyplot.ylabel("Fitness")
        pyplot.show()
