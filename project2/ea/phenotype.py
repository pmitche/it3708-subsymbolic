__author__ = "paulpm"


class Phenotype(object):
    def __init__(self, genotype):
        self.genotype = self.develop(genotype)

    @property
    def fitness(self):
        raise NotImplementedError

    def develop(self, genotype):
        raise NotImplementedError

    def factory(type, genotype):
        if type == "OneMax": return OneMaxPhenotype(genotype)
        if type == "LOLZPrefix": return LolzPrefixPhenotype(genotype)
        assert 0, "Bad Phenotype creation: " + type

    factory = staticmethod(factory)


class OneMaxPhenotype(Phenotype):
    def __init__(self, genotype):
        Phenotype.__init__(self, genotype)

    @property
    def fitness(self):
        return sum(self.genotype.bits) / len(self.genotype.bits)

    def develop(self, genotype):
        return genotype


class LolzPrefixPhenotype(Phenotype):
    def __init__(self, genotype, z):
        Phenotype.__init__(self, genotype)
        self.z = z

    @property
    def fitness(self):
        raise NotImplementedError

    def develop(self, genotype):
        return genotype


"""class SurprisingSequencePhenotype(Phenotype):
    raise NotImplementedError"""