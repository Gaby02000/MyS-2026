import numpy as np
import matplotlib.pyplot as plt

N_EXPERIMENTOS = 30
N_CORRIDAS = 100
TOTAL_CORRIDAS = N_EXPERIMENTOS * N_CORRIDAS

Z_99 = 2.57

np.random.seed(42)

def generar_tiempos():
    A = np.random.uniform(1, 5)
    B = np.random.uniform(1, 3)
    C = np.random.uniform(1, 3)
    D = np.random.uniform(1, 6)
    E = np.random.uniform(6, 12)
    F = np.random.uniform(5, 10)
    G = np.random.uniform(10, 15)
    return A, B, C, D, E, F, G

def calcular_proyecto():
    A, B, C, D, E, F, G = generar_tiempos()
    acceso_superior =  A + B +C
    acceso_medio = A + D + E +F
    acceso_inferior = F +G
    ruta_vehiculo = acceso_medio + G
    tiempo_total = max(acceso_superior, ruta_vehiculo, acceso_inferior)
    return tiempo_total, acceso_superior, acceso_medio, acceso_inferior

def calcular_ic(promedios):
    media = np.mean(promedios)
    desvio = np.std( promedios, ddof=1)
    error_estandar = (desvio / np.sqrt(N_EXPERIMENTOS))
    ic_inferior = (media - Z_99 * error_estandar)
    ic_superior = (media + Z_99 * error_estandar)
    return media, ic_inferior, ic_superior

def mostrar_resultados(media, ic_inf, ic_sup, criticidad):
    print("==========================================")
    print("RESULTADOS DE LA SIMULACIÓN")
    print("==========================================\n")
    print(f"Tiempo promedio del proyecto: " f"{media:.2f}")
    print("\nINTERVALO DE CONFIANZA 99%")
    print(f"IC Inferior: "f"{ic_inf:.2f}")
    print(f"IC Superior: " f"{ic_sup:.2f}")
    print("\nPORCENTAJE DE CRITICIDAD")
    print( f"Acceso Superior: "f"{criticidad[0]:.2f}%")
    print(f"Acceso Medio: " f"{criticidad[1]:.2f}%")
    print(f"Acceso Inferior: " f"{criticidad[2]:.2f}%")

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
    plt.title("Distribución de los Promedios de los Tiempos por Experimentos",fontsize=14)
    plt.xlabel("Tiempo promedio")
    plt.ylabel("Frecuencia")
    plt.show()

def main():
    tiempos_totales = []
    promedios_experimentos = []
    criticidad = np.zeros(3)
    for experimento in range(N_EXPERIMENTOS):
        tiempos_experimento = []
        for corrida in range(N_CORRIDAS):
            tiempo_total, acceso_superior, acceso_medio, acceso_inferior = calcular_proyecto()
            tiempos_totales.append(tiempo_total)
            tiempos_experimento.append(tiempo_total)
            maximo = max(acceso_superior, acceso_medio, acceso_inferior)
            if acceso_superior == maximo:
                criticidad[0] += 1
            if acceso_medio == maximo:
                criticidad[1] += 1

            if acceso_inferior == maximo:
                criticidad[2] += 1
        promedio = np.mean(tiempos_experimento)
        promedios_experimentos.append(promedio)
    media, ic_inf, ic_sup = calcular_ic(promedios_experimentos)
    porcentaje_criticidad = criticidad /TOTAL_CORRIDAS * 100
    mostrar_resultados(media,ic_inf, ic_sup, porcentaje_criticidad)
    graficar_histograma_corridas(tiempos_totales)
    graficar_histograma_promedios(promedios_experimentos)

main()