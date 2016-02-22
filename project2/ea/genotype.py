from ea.config import *
from ea.utils import *

__author__ = "paulpm"


class Genotype(object):
    def __init__(self, length=10, bits=None):
        self.bits = random_bits(length) if bits is None else bits

    def mutate(self):
        if random() < MUTATION_RATE:
            index = randint(0, len(self.bits)-1)
            bit_flip(self.bits, index)


# Not used here
class OneMaxGenotype(Genotype):
    def __init__(self, length=10, bits=None):
        super().__init__(length, bits)

    def mutate(self):
        if random() < MUTATION_RATE:
            index = randint(0, len(self.bits)-1)
            bit_flip(self.bits, index)


