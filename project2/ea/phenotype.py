__author__ = "paulpm"


class Phenotype(object):
    def __init__(self, genotype):
        self.genotype = genotype
        self.bits = self.develop(self.genotype)

    @property
    def fitness(self):
        raise NotImplementedError

    def develop(self, genotype):
        raise NotImplementedError


class OneMaxPhenotype(Phenotype):
    def __init__(self, genotype):
        Phenotype.__init__(self, genotype)

    @property
    def fitness(self):
        return sum(self.bits) / len(self.bits)

    def develop(self, genotype):
        return genotype.bits


class LolzPrefixPhenotype(Phenotype):
    def __init__(self, genotype, z):
        Phenotype.__init__(self, genotype)
        self.z = z

    @property
    def fitness(self):
        raise NotImplementedError

    def develop(self, genotype):
        return genotype.bits


"""class SurprisingSequencePhenotype(Phenotype):
    raise NotImplementedError"""