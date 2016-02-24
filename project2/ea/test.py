"""if s == 0:
            return list(map(lambda x: 1, population.all_fitnesses))
        else:
            return list(map(lambda x: 1 + (x - m)/(2*s), population.all_fitnesses))"""

var = [0.75, 0.5, 0.1, 0.2]
var2 = list(map(lambda x: 1, var))

print(var2)
