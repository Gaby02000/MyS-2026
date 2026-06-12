import numpy as np
import matplotlib.pyplot as plt

N_EXPERIMENTOS = 30
N_CORRIDAS = 100
Z_95 = 1.96
INVENTARIO_INICIAL = 1500
PUNTO_REORDEN = 15
CANTIDAD_ORDEN = 100
COSTO_MANTENIMIENTO = 450
COSTO_ORDENAR = 3800
COSTO_FALTANTE = 625
DIAS = 365
np.random.seed(42)

def generar_demanda():
    demandas = [25, 30, 40, 50, 100, 150, 200, 250, 300]
    probabilidades = [0.20, 0.04, 0.06, 0.12, 0.20, 0.03, 0.15, 0.10, 0.10]
    return np.random.choice(demandas, p=probabilidades)

def generar_tiempo_entrega():
    tiempos = [1, 2, 3, 4]
    probabilidades = [0.20, 0.30, 0.25, 0.25]
    return np.random.choice(tiempos, p=probabilidades)

def simular_anio():
    inventario = INVENTARIO_INICIAL
    costo_mantenimiento = 0
    costo_ordenar = 0
    costo_faltante = 0
    llegada_pedido = -1
    for dia in range(1, DIAS + 1):
        if dia == llegada_pedido:
            inventario += CANTIDAD_ORDEN
            llegada_pedido = -1
        demanda = generar_demanda()
        if inventario >= demanda:
            inventario -= demanda
        else:
            faltante = demanda - inventario
            inventario = 0
            costo_faltante += faltante * COSTO_FALTANTE
        costo_mantenimiento += inventario * COSTO_MANTENIMIENTO
        if inventario <= PUNTO_REORDEN and llegada_pedido == -1:
            demora = generar_tiempo_entrega()
            llegada_pedido = dia + demora
            costo_ordenar += COSTO_ORDENAR
    costo_total = (costo_mantenimiento + costo_ordenar+ costo_faltante)
    costo_mensual = costo_total / 12
    return costo_mensual

def calcular_ic(promedios):
    media = np.mean(promedios)
    desvio = np.std(promedios, ddof=1)
    error_estandar = desvio / np.sqrt(N_EXPERIMENTOS)
    ic_inferior = media - Z_95 * error_estandar
    ic_superior = media + Z_95 * error_estandar
    return media, ic_inferior, ic_superior

def mostrar_resultados(media, ic_inf, ic_sup):
    print("========================================")
    print("RESULTADOS DE LA SIMULACIÓN")
    print("========================================\n")

    print(f"Costo promedio mensual: ${media:,.2f}")

    print("\nINTERVALO DE CONFIANZA 95%")
    print(f"IC Inferior: ${ic_inf:,.2f}")
    print(f"IC Superior: ${ic_sup:,.2f}")

def graficar_histograma(datos):
    plt.figure(figsize=(10,5))
    plt.hist(datos, bins=25, color="skyblue", edgecolor="black")
    plt.title("Distribución del costo promedio mensual")
    plt.xlabel("Costo promedio mensual")
    plt.ylabel("Frecuencia")
    plt.show()

def main():
    costos_mensuales = []
    for experimento in range(N_EXPERIMENTOS):
        costos_experimento = []
        for corrida in range(N_CORRIDAS):
            costo = simular_anio()
            costos_experimento.append(costo)
        promedio = np.mean(costos_experimento)
        costos_mensuales.append(promedio)
    media, ic_inf, ic_sup = calcular_ic(costos_mensuales)
    mostrar_resultados(media, ic_inf, ic_sup)
    graficar_histograma(costos_mensuales)

main()