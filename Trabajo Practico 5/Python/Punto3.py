import numpy as np
import matplotlib.pyplot as plt

N_EXPERIMENTOS = 30
N_CORRIDAS = 100
TOTAL_CORRIDAS = N_EXPERIMENTOS * N_CORRIDAS

Z_99 = 2.57

np.random.seed(42)

def generar_tiempos():
    A = np.random.uniform(2, 4)
    B = np.random.uniform(3, 5)
    C = np.random.uniform(1, 2)
    D = np.random.uniform(4, 8)
    E = np.random.uniform(3, 6)
    F = np.random.uniform(2, 5)
    G = np.random.uniform(2, 4)
    H = np.random.uniform(1, 3)
    I = np.random.uniform(2, 4)
    J = np.random.uniform(2, 3)
    return A, B, C, D, E, F, G, H, I, J

def calcular_proyecto():
    A, B, C, D, E, F, G, H, I, J = generar_tiempos()
    ruta_1 = A + B + C + D + E
    ruta_2 =  F + G
    ruta_3 = H
    ruta_4 = I
    ruta_5 = max(ruta_2, ruta_3, ruta_4)
    tiempo_total = ruta_1 + ruta_5 + J
    return tiempo_total, ruta_2, ruta_3, ruta_4

def calcular_ic(promedios):
    media = np.mean(promedios)
    desvio = np.std(promedios, ddof=1)
    error_estandar = desvio / np.sqrt(N_EXPERIMENTOS)
    ic_inferior = media - Z_99 * error_estandar
    ic_superior = media + Z_99 * error_estandar
    return media, ic_inferior, ic_superior

def mostrar_resultados(media, ic_inf, ic_sup,criticidad_tareas):
    print("==========================================")
    print("RESULTADOS DE LA SIMULACIÓN")
    print("==========================================\n")
    print(f"Tiempo promedio del proyecto: "f"{media:.2f}" )
    print("\nINTERVALO DE CONFIANZA 99%")
    print(f"IC Inferior: " f"{ic_inf:.2f}")
    print(f"IC Superior: " f"{ic_sup:.2f}")
    print("\nPORCENTAJE DE CRITICIDAD")
    tareas = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J' ]
    for tarea in tareas:
        print( f"Tarea {tarea}: "f"{criticidad_tareas[tarea]:.2f}%")

def graficar_histograma_corridas(datos):
    plt.figure(figsize=(10, 5))
    plt.hist(datos, bins=30, color='skyblue', edgecolor='black')
    plt.title("Distribución del Tiempo del Proyecto", fontsize=14)
    plt.xlabel("Tiempo")
    plt.ylabel("Frecuencia")
    plt.show()

def graficar_histograma_promedios(promedios):
    plt.figure(figsize=(10, 5))
    plt.hist(promedios, bins=30, color='orange', edgecolor='black')
    plt.title("Distribución de los Promedios de los Tiempos por Experimentos", fontsize=14)
    plt.xlabel("Tiempo promedio")
    plt.ylabel("Frecuencia")
    plt.show()

def main():
    tiempos_totales = []
    promedios_experimentos = []
    criticidad_tareas = {'A': 0,'B': 0,'C': 0, 'D': 0,'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
    for x in range(N_EXPERIMENTOS):
        tiempos_experimento = []
        for i in range(N_CORRIDAS):
            tiempo_total,ruta_2, ruta_3, ruta_4 = calcular_proyecto()
            tiempos_totales.append(tiempo_total)
            tiempos_experimento.append(tiempo_total)
            criticidad_tareas['A'] += 1
            criticidad_tareas['B'] += 1
            criticidad_tareas['C'] += 1
            criticidad_tareas['D'] += 1
            criticidad_tareas['E'] += 1
            criticidad_tareas['J'] += 1
            maximo = max( ruta_2, ruta_3, ruta_4)
            if ruta_2 == maximo:
                criticidad_tareas['F'] += 1
                criticidad_tareas['G'] += 1
            if ruta_3 == maximo:
                criticidad_tareas['H'] += 1

            if ruta_4 == maximo:
                criticidad_tareas['I'] += 1
        promedio = np.mean(tiempos_experimento)
        promedios_experimentos.append(promedio)
    media, ic_inf, ic_sup = calcular_ic(promedios_experimentos)
    for tarea in criticidad_tareas:
        criticidad_tareas[tarea] = criticidad_tareas[tarea] / TOTAL_CORRIDAS * 100
    mostrar_resultados( media, ic_inf, ic_sup, criticidad_tareas)
    graficar_histograma_corridas(tiempos_totales)
    graficar_histograma_promedios(promedios_experimentos)

main()