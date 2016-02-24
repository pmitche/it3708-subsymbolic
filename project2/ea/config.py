from ea.evo import *

"""
Configurations and constants to be used with the general evolutionary algorithm
"""

MateSelector = ["FitnessProportionate", "SigmaScaling", "Boltzmann", "Tournament"]
AdultSelector = ["FullGenerational", "OverProduction", "GenerationalMixing"]
Pheno = ["OneMax", "LOLZPrefix"]

MATE = MateSelector[1]
ADULT = AdultSelector[2]
PHENO = Pheno[0]

GENERATION_LIMIT = 10000
POPULATION_SIZE = 300
CROSSOVER_RATE = 0.9

GENOTYPE_LENGTH = 40
MUTATION_RATE = 0.005
Z = 21

T = 1
EPSILON = 0.6
TOURNAMENT_SIZE = 8

PLOT = True


def main():
    ea = EA(MATE, ADULT, PHENO)
    ea.evolve()

if __name__ == "__main__":
    main()

