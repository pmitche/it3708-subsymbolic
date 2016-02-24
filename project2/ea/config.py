from ea.evo import *

"""
Configurations and constants to be used with the general evolutionary algorithm
"""

MateSelector = ["FitnessProportionate", "SigmaScaling", "Boltzmann", "Tournament"]
AdultSelector = ["FullGenerational", "OverProduction", "GenerationalMixing"]
Pheno = ["OneMax", "LOLZPrefix"]

mate = MateSelector[2]
adult = AdultSelector[2]
pheno = Pheno[1]

GENERATION_LIMIT = 10000
POPULATION_SIZE = 100
CROSSOVER_RATE = 0.2

GENOTYPE_LENGTH = 40
MUTATION_RATE = 0.01
Z = 21

T = 0.01
EPSILON = 0.6
TOURNAMENT_SIZE = 8

PLOT = True


def main():
    ea = EA(mate, adult, pheno)
    ea.evolve()

if __name__ == "__main__":
    main()

