import random

# Definimos los parámetros del algoritmo genético
POPULATION_SIZE = 10
GENES = '01'  # Genes posibles (binarios)
TARGET = '1111'  # Objetivo a alcanzar
MUTATION_RATE = 0.01
GENERATIONS = 100

# Función para crear un individuo aleatorio
def create_individual(length):
    return ''.join(random.choice(GENES) for _ in range(length))

# Función para calcular la aptitud (fitness) de un individuo
def fitness(individual):
    return sum(1 for i, j in zip(individual, TARGET) if i == j)

# Función para seleccionar a los padres
def select_parents(population):
    return random.choices(population, weights=[fitness(ind) for ind in population], k=2)

# Función para cruzar (crossover) dos padres y crear un hijo
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

# Función para mutar un individuo
def mutate(individual):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random.choice(GENES)
    return ''.join(individual)

# Inicializamos la población
population = [create_individual(len(TARGET)) for _ in range(POPULATION_SIZE)]

# Evolucionamos la población
for generation in range(GENERATIONS):
    population = sorted(population, key=fitness, reverse=True)
    if fitness(population[0]) == len(TARGET):
        break
    next_generation = population[:2]  # Elitismo: conservamos los mejores dos individuos
    for _ in range(POPULATION_SIZE - 2):
        parent1, parent2 = select_parents(population)
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_generation.append(child)
    population = next_generation
    print(f'Generación {generation + 1}: Mejor individuo = {population[0]}, Aptitud = {fitness(population[0])}')

# Resultado final
print(f'Resultado final: {population[0]} con aptitud {fitness(population[0])}')