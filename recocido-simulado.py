import math
import random

def recocido_simulado(funcion_objetivo, solucion_inicial, temperatura, tasa_enfriamiento, temperatura_parada):
    solucion_actual = solucion_inicial
    valor_actual = funcion_objetivo(solucion_actual)
    mejor_solucion = solucion_actual
    mejor_valor = valor_actual

    while temperatura > temperatura_parada:
        # Generar una nueva solución candidata
        solucion_candidata = obtener_vecino(solucion_actual)
        valor_candidato = funcion_objetivo(solucion_candidata)

        # Calcular la probabilidad de aceptación
        probabilidad_aceptacion = math.exp((valor_candidato - valor_actual) / temperatura)

        # Decidir si se acepta la solución candidata
        if valor_candidato > valor_actual or random.random() < probabilidad_aceptacion:
            solucion_actual = solucion_candidata
            valor_actual = valor_candidato

            # Actualizar la mejor solución encontrada
            if valor_candidato > mejor_valor:
                mejor_solucion = solucion_candidata
                mejor_valor = valor_candidato

        # Enfriar la temperatura
        temperatura *= tasa_enfriamiento

    return mejor_solucion, mejor_valor

def obtener_vecino(solucion):
    # Generar una solución vecina (esto es específico del problema)
    # Para simplicidad, asumimos que la solución es una lista de números
    vecino = solucion[:]
    indice = random.randint(0, len(solucion) - 1)
    vecino[indice] += random.uniform(-1, 1)
    return vecino

def funcion_objetivo(solucion):
    # Definir la función objetivo (esto es específico del problema)
    # Para simplicidad, asumimos que queremos maximizar la suma de la solución
    return sum(solucion)

# Ejemplo de uso
solucion_inicial = [random.uniform(-10, 10) for _ in range(10)]
temperatura = 1000
tasa_enfriamiento = 0.95
temperatura_parada = 1e-3

mejor_solucion, mejor_valor = recocido_simulado(funcion_objetivo, solucion_inicial, temperatura, tasa_enfriamiento, temperatura_parada)
print("Mejor solución:", mejor_solucion)
print("Mejor valor:", mejor_valor)