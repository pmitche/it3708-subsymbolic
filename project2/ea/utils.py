from random import randint, random


def random_bits(length):
    return [randint(0, 1) for _ in range(length)]


def bit_flip(bitstring, index):
    bitstring[index] = int(not bitstring[index])
    return bitstring

