import random

# Algoritmo de Optimización por Enjambre de Partículas (PSO) en Python


# Definir la función objetivo
def funcion_objetivo(x):
    return x**2

# Clase para representar una partícula
class Particula:
    def __init__(self, limite_inferior, limite_superior):
        self.posicion = random.uniform(limite_inferior, limite_superior)
        self.velocidad = random.uniform(-1, 1)
        self.mejor_posicion = self.posicion
        self.mejor_valor = funcion_objetivo(self.posicion)

    def actualizar_velocidad(self, mejor_global, c1=2.0, c2=2.0, w=0.5):
        r1 = random.random()
        r2 = random.random()
        self.velocidad = (w * self.velocidad +
                          c1 * r1 * (self.mejor_posicion - self.posicion) +
                          c2 * r2 * (mejor_global - self.posicion))

    def actualizar_posicion(self, limite_inferior, limite_superior):
        self.posicion += self.velocidad
        if self.posicion < limite_inferior:
            self.posicion = limite_inferior
        elif self.posicion > limite_superior:
            self.posicion = limite_superior

        valor = funcion_objetivo(self.posicion)
        if valor < self.mejor_valor:
            self.mejor_valor = valor
            self.mejor_posicion = self.posicion

# Función principal del algoritmo PSO
def pso(funcion_objetivo, limite_inferior, limite_superior, num_particulas, num_iteraciones):
    enjambre = [Particula(limite_inferior, limite_superior) for _ in range(num_particulas)]
    mejor_global = min(enjambre, key=lambda p: p.mejor_valor).mejor_posicion

    for _ in range(num_iteraciones):
        for particula in enjambre:
            particula.actualizar_velocidad(mejor_global)
            particula.actualizar_posicion(limite_inferior, limite_superior)

        mejor_global = min(enjambre, key=lambda p: p.mejor_valor).mejor_posicion

    return mejor_global

# Parámetros del algoritmo
limite_inferior = -10
limite_superior = 10
num_particulas = 30
num_iteraciones = 100

# Ejecutar el algoritmo PSO
mejor_solucion = pso(funcion_objetivo, limite_inferior, limite_superior, num_particulas, num_iteraciones)
print(f"La mejor solución encontrada es: {mejor_solucion} con valor {funcion_objetivo(mejor_solucion)}")