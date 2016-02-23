from ea.evo import *

"""MateSelector = ["FitnessProportionate", "SigmaScaling", "Boltzmann", "Tournament"]
AdultSelector = ["FullGenerational", "OverProduction", "GenerationalMixing"]
Pheno = ["OneMax", "LOLZPrefix"]

mate = MateSelector[0]
adult = AdultSelector[2]
pheno = Pheno[0]

GENERATION_LIMIT = 200
POPULATION_SIZE = 20
CROSSOVER_RATE = 0.2

GENOTYPE_LENGTH = 20
MUTATION_RATE = 0.05

T = 0.01
EPSILON = 0.6
TOURNAMENT_SIZE = 8

PLOT = True"""
ea = EA(mate, adult, pheno)
ea.run()
