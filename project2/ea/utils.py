from random import randint, random


def random_bits(length):
    return [randint(0, 1) for _ in range(length)]


def bit_flip(bits, index):
    bits[index] = int(not bits[index])
    return bits

