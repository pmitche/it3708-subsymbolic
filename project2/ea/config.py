"""
Configurations and constants to be used with the general evolutionary algorithm
"""


"""GENOTYPE_LENGTH = 10
MUTATION_RATE = 0.05
CROSSOVER_RATE = 0.6
POPULATION_SIZE = 30
GENERATION_LIMIT = 100

T = 0.01
EPSILON = 0.6
TOURNAMENT_SIZE = 8"""

MateSelector = ["FitnessProportionate", "SigmaScaling", "Boltzmann", "Tournament"]
AdultSelector = ["FullGenerational", "OverProduction", "GenerationalMixing"]
Pheno = ["OneMax", "LOLZPrefix"]

mate = MateSelector[2]
adult = AdultSelector[2]
pheno = Pheno[0]

GENERATION_LIMIT = 10000
POPULATION_SIZE = 200
CROSSOVER_RATE = 0.2

GENOTYPE_LENGTH = 40
MUTATION_RATE = 0.01

T = 0.01
EPSILON = 0.6
TOURNAMENT_SIZE = 8

PLOT = True

