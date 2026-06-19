import numpy as np
import matplotlib.pyplot as plt

CANT_EXPERIMENTOS = 60
CANT_CAMIONES = 100

MEDIA_LLEGADAS = 15

Z_95 = 1.96
Z_99 = 2.576

np.random.seed(42)

def generar_tiempo_servicio(empleado):
    if empleado == 0:
        tiempo = np.random.normal(18, 4)
        while tiempo <= 0:
            tiempo = np.random.normal(18, 4)
    elif empleado == 1:
        tiempo = np.random.exponential(15)
    elif empleado == 2:
        tiempo = np.random.exponential(16)
    elif empleado == 3:
        tiempo = np.random.normal(14, 3)
        while tiempo <= 0:
            tiempo = np.random.normal(14, 3)
    elif empleado == 4: 
        tiempo = np.random.normal(19, 5)
        while tiempo <= 0:
            tiempo = np.random.normal(19, 5)
    else:
        tiempo = np.random.exponential(15)
    return tiempo

def simular_experimento(n_surtidores):
    reloj = 0
    surtidores = [0] * n_surtidores
    tiempo_ocupado = [0] * n_surtidores
    tiempos_espera = []

    for camion in range(CANT_CAMIONES):
        llegada = np.random.exponential(MEDIA_LLEGADAS)
        reloj += llegada
        surtidor = np.argmin(surtidores)
        inicio_atencion = max(reloj, surtidores[surtidor])
        espera = inicio_atencion - reloj
        tiempos_espera.append(espera)
        servicio = generar_tiempo_servicio(surtidor)
        tiempo_ocupado[surtidor] += servicio
        surtidores[surtidor] = inicio_atencion + servicio
    tiempo_total = max(surtidores)
    ocupacion = []
    for tiempo in tiempo_ocupado:
        ocupacion.append((tiempo / tiempo_total) * 100)
    promedio_espera = np.mean(tiempos_espera)
    return promedio_espera, ocupacion

def calcular_ic(datos, z):
    media = np.mean(datos)
    desvio = np.std(datos, ddof=1)
    error_estandar = desvio / np.sqrt(len(datos))
    ic_inferior = media - z * error_estandar
    ic_superior = media + z * error_estandar
    return media, ic_inferior, ic_superior

def mostrar_resultados(promedios, ocupaciones):
    media95, ic95_inf, ic95_sup = calcular_ic(promedios, Z_95)
    media99, ic99_inf, ic99_sup = calcular_ic(promedios, Z_99)

    print("======================================")
    print("RESULTADOS DEL SISTEMA")
    print("======================================")

    print(f"\nTiempo promedio de espera: {media95:.4f} min")

    print("\nINTERVALO DE CONFIANZA 95%")
    print(f"IC Inferior: {ic95_inf:.4f}")
    print(f"IC Superior: {ic95_sup:.4f}")

    print("\nINTERVALO DE CONFIANZA 99%")
    print(f"IC Inferior: {ic99_inf:.4f}")
    print(f"IC Superior: {ic99_sup:.4f}")
    ocupaciones = np.array(ocupaciones)
    print("\nOCUPACIÓN PROMEDIO")
    for i in range(4):
        promedio = np.mean(ocupaciones[:, i])
        print(f"Surtidor {i+1}: {promedio:.2f}%")

def graficar_histograma(promedios):
    plt.figure(figsize=(10, 5))
    plt.hist(promedios, bins=10, color="skyblue", edgecolor="black")
    plt.title("Distribución del Tiempo Promedio de Espera")
    plt.xlabel("Tiempo promedio de espera (min)")
    plt.ylabel("Frecuencia")
    plt.show()

def main():
    promedios_espera = []
    ocupaciones = []
    for experimento in range(CANT_EXPERIMENTOS):
        promedio, ocupacion = simular_experimento(4)
        promedios_espera.append(promedio)
        ocupaciones.append(ocupacion)
    mostrar_resultados(promedios_espera, ocupaciones)
    graficar_histograma(promedios_espera)
    base = np.mean(promedios_espera)
    objetivo = base * 0.7


    print(f"Base: {base:.4f}",f" -  Objetivo (-30%): {objetivo:.4f}")
    print()
    for n in range(5, 11):
        promedios_temp = []
        for _ in range(CANT_EXPERIMENTOS):
            prom, _ = simular_experimento(n)
            promedios_temp.append(prom)
        media = np.mean(promedios_temp)
        cumple = "Cumple" if media <= objetivo else "No cumple"
        if media <= objetivo:
            print(f"Surtidores: {n} -> {media:.4f} {cumple}")
main()