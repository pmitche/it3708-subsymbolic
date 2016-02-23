from ea.config import *
from ea import utils
from random import random, randint

__author__ = "paulpm"


class Genotype(object):
    def __init__(self, length=10, bits=None):
        self.bits = utils.random_bits(length) if bits is None else bits

    """def mutate(self):
        if random() < MUTATION_RATE:
            index = randint(0, len(self.bits)-1)
            utils.bit_flip(self.bits, index)"""

    def mutate(self):
        for i in range(0, len(self.bits)):
            if random() < MUTATION_RATE:
                self.bits[i] = 1 if self.bits[i] == 0 else 0


# Not used here
class OneMaxGenotype(Genotype):
    def __init__(self, length=10, bits=None):
        Genotype.__init__(self, length, bits)

    def mutate(self):
        if random() < MUTATION_RATE:
            index = randint(0, len(self.bits)-1)
            utils.bit_flip(self.bits, index)


