from ea import utils
from random import random, randint
from ea.config import *

__author__ = "paulpm"


class Genotype(object):
    def __init__(self, length=GENOTYPE_LENGTH, bits=None):
        self.bits = utils.random_bits(length) if bits is None else bits

    def mutate(self):
        for i in range(0, len(self.bits)):
            if random() < MUTATION_RATE:
                utils.bit_flip(self.bits, i)

    def crossover(self, other):
        this = self.bits
        other = other.bits

        def split(gene):
            return randint(1, len(gene)-1)

        if random() < CROSSOVER_RATE:
            split_point = split(this)
            return (
                Genotype(length=len(this), bits=this[:split_point] + other[split_point:]),
                Genotype(length=len(other), bits=this[:split_point] + other[split_point:])
            )
        else:
            return (
                Genotype(length=len(this), bits=this),
                Genotype(length=len(other), bits=other)
            )

    """def mutate(self):
        if random() < MUTATION_RATE:
            index = randint(0, len(self.bits)-1)
            utils.bit_flip(self.bits, index)"""


