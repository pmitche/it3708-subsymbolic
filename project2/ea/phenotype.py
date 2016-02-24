import ea.cfg as cfg

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
        if type == "LOLZPrefix": return LolzPrefixPhenotype(genotype, cfg.Z)
        assert 0, "Invalid Phenotype creation: " + type

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
        first = self.genotype.bits[0]
        count = 0
        for bit in self.genotype.bits:
            if bit == first and (bit or (not bit and self.z > count)):
                count += 1
            else: break

        return count / len(self.genotype.bits)

    def develop(self, genotype):
        return genotype




"""class SurprisingSequencePhenotype(Phenotype):
    raise NotImplementedError"""