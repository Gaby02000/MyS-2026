import numpy as np
import matplotlib.pyplot as plt

CANT_ANIOS = 30
CANT_DIAS = 250
INVENTARIO_INICIAL = 90
PRODUCCION_DIARIA = 130
DEMANDA_MEDIA = 150
DESVIO_ESTANDAR = 25
COSTO_MANTENIMIENTO = 70
PUNTOS_REORDEN = [60, 70, 80]
Z_95 = 1.96
np.random.seed(42)

def generar_demanda():
    
    return max(0, np.random.normal(DEMANDA_MEDIA, DESVIO_ESTANDAR))

def simular_anio(punto_reorden):
    inventario = INVENTARIO_INICIAL
    costo_anual = 0
    turnos_adicionales = 0
    turno_extra = False
    for dia in range(CANT_DIAS):
        produccion = PRODUCCION_DIARIA
        if turno_extra:
            produccion += PRODUCCION_DIARIA
        inventario += produccion
        demanda = generar_demanda()
        inventario -= demanda
        if inventario < 0:
            inventario = 0
        costo_anual += inventario * COSTO_MANTENIMIENTO
        if inventario <= punto_reorden:
            turno_extra = True
            turnos_adicionales += 1
        else:
            turno_extra = False
    return costo_anual, turnos_adicionales

def calcular_ic(costos):
    media = np.mean(costos)
    desvio = np.std(costos, ddof=1)
    error_estandar = desvio / np.sqrt(CANT_ANIOS)
    ic_inferior = media - Z_95 * error_estandar
    ic_superior = media + Z_95 * error_estandar
    return media, ic_inferior, ic_superior

def mostrar_resultados(punto_reorden, promedio_costo, promedio_turnos, ic_inf,ic_sup):

    print("==========================================")
    print(f"PUNTO DE REORDEN = {punto_reorden}")
    print("==========================================")

    print(f"Costo anual promedio: ${promedio_costo:,.2f}")
    print(f"Turnos adicionales promedio: {promedio_turnos:.2f}")

    print("\nINTERVALO DE CONFIANZA 95%")
    print(f"IC Inferior: ${ic_inf:,.2f}")
    print(f"IC Superior: ${ic_sup:,.2f}")
    print()

def graficar_histograma(costos, punto_reorden):
    plt.figure(figsize=(10, 5))
    plt.hist(costos, bins=30, color="skyblue",edgecolor="black")
    plt.title(f"Distribución del Costo Anual\nPunto de Reorden = {punto_reorden}")
    plt.xlabel("Costo anual")
    plt.ylabel("Frecuencia")
    plt.show()

def main():
    for punto_reorden in PUNTOS_REORDEN:
        costos_anuales = []
        turnos_anuales = []
        for anio in range(CANT_ANIOS):
            costo_anual, turnos_adicionales = simular_anio(punto_reorden)
            costos_anuales.append(costo_anual)
            turnos_anuales.append(turnos_adicionales)
        promedio_turnos = np.mean(turnos_anuales)
        promedio_costo, ic_inf, ic_sup = calcular_ic(costos_anuales)
        mostrar_resultados(punto_reorden, promedio_costo, promedio_turnos,ic_inf,ic_sup)
        graficar_histograma(costos_anuales,punto_reorden)

main()