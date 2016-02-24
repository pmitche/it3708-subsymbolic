import ea.cfg as cfg

"""
Configurations and constants to be used with the general evolutionary algorithm.
NOTE: This class is going to be retarded.
"""

MateSelector = ["FitnessProportionate", "SigmaScaling", "Boltzmann", "Tournament"]
AdultSelector = ["FullGenerational", "OverProduction", "GenerationalMixing"]
Pheno = ["OneMax", "LOLZPrefix"]

#TODO: Add ELITISM and ELITISM_SIZE parameters
def main():
    def inputs():
        phen = int(input("Select problem: 0: OneMax, 1: LOLZPrefix: "))
        if phen == 1:
            cfg.Z = int(input("Choose zero threshold for LOLZPrefix (21): "))

        cfg.GENOTYPE_LENGTH = int(input("Choose genotype length (40): "))

        cfg.PHENO = Pheno[phen]

        mate = int(input("Select a mate selection method. 0: FitnessProp, 1: SigmaScaling, 2: Boltzmann, 3: Tournament: "))
        if mate == 2:
            cfg.T = float(input("Select Boltzmann temperature (1): "))
        elif mate == 3:
            cfg.TOURNAMENT_SIZE = int(input("Choose tournament size (8): "))
            cfg.EPSILON = float(input("Choose epsilon for tournament (0.6): "))

        cfg.MATE = MateSelector[mate]
        cfg.ADULT = AdultSelector[int(input("Select an adult selection method. 0: FullGenerational, 1: OverProd, 2: GenerationalMixing: "))]

        cfg.GENERATION_LIMIT = int(input("Choose a generation limit: "))
        cfg.POPULATION_SIZE = int(input("Choose a population size: "))

        cfg.MUTATION_RATE = float(input("Choose mutation rate (0.005): "))
        cfg.CROSSOVER_RATE = float(input("Choose crossover rate (0.9): "))

    while True:

        inputs()

        from ea.evo import EA
        ea = EA(cfg.MATE, cfg.ADULT, cfg.PHENO)
        ea.evolve()

        cont = input("Continue with new parameters: y. Only modify crossover and mutation: c. Break: exit: ")
        if cont == "y":
            continue
        else:
            break


if __name__ == "__main__":
    main()

