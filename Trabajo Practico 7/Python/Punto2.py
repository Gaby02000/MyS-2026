import numpy as np
import matplotlib.pyplot as plt

CANT_DIAS = 365
MINUTOS_DIA = 480

MEDIA_LLEGADAS = 10

Z_95 = 1.96

np.random.seed(42)

def generar_tiempo_servicio(caja):
    if caja == 0:
        t = np.random.normal(15, 3)
        while t <= 0:
            t = np.random.normal(15, 3)
        return t
    elif caja == 1:
        return np.random.exponential(12)
    else:
        return np.random.exponential(13)

def simular_dia(n_cajas):
    reloj = 0
    cajas = [0] * n_cajas
    tiempos_espera = []
    ocupacion = [0] * n_cajas
    while True:
        llegada = np.random.exponential(MEDIA_LLEGADAS)
        if reloj + llegada > MINUTOS_DIA:
            break
        reloj += llegada
        caja = np.argmin(cajas)
        inicio = max(reloj, cajas[caja])
        espera = inicio - reloj
        tiempos_espera.append(espera)
        servicio = generar_tiempo_servicio(caja)
        ocupacion[caja] += servicio
        cajas[caja] = inicio + servicio
    return np.mean(tiempos_espera), ocupacion

def simular_sistema(n_cajas):
    promedios = []
    ocupaciones = []
    for dia in range(CANT_DIAS):
        prom, occ = simular_dia(n_cajas)
        promedios.append(prom)
        ocupaciones.append(occ)
    promedios = np.array(promedios)
    ocupaciones = np.array(ocupaciones)
    media = np.mean(promedios)
    desvio = np.std(promedios, ddof=1)
    ic_inf = media - Z_95 * desvio / np.sqrt(CANT_DIAS)
    ic_sup = media + Z_95 * desvio / np.sqrt(CANT_DIAS)
    return media, ic_inf, ic_sup, promedios, ocupaciones

def mostrar_resultados(n_cajas, media, ic_inf, ic_sup, ocupaciones):
  
    print("======================================")
    print("RESULTADOS DEL SISTEMA")
    print("======================================")


    print(f"Tiempo promedio de espera: {media:.4f} min")
    print("\nINTERVALO DE CONFIANZA 95%")

    print(f"IC Inferior: {ic_inf:.4f}")
    print(f"IC Superior: {ic_sup:.4f}")
    print("\nOCUPACIÓN PROMEDIO")
    for i in range(n_cajas):
        print(f"Caja {i+1}: {np.mean(ocupaciones[:, i]):.2f}%")
#def graficar_histograma(promedios, n_cajas):
 #   plt.figure(figsize=(10, 5))
  #  plt.hist(promedios, bins=10, color="skyblue", edgecolor="black")
  #  plt.title(f"Distribución del tiempo de espera")
  #  plt.xlabel("Tiempo promedio de espera (min)")
  #  plt.ylabel("Frecuencia")
  #  plt.show()

def main():  
    media, ic_inf, ic_sup, promedios, ocupaciones = simular_sistema(2)
    mostrar_resultados(2, media, ic_inf, ic_sup, ocupaciones)
   # graficar_histograma(promedios, 2)
    objetivo = media * 0.75 
    print(f"Base (2 cajas): {media:.4f}")
    print(f"Objetivo: {objetivo:.4f}\n")
    for n in range(2, 8):
        media, _, _, _, _ = simular_sistema(n)
        cumple = "Cumple" if media <= objetivo else "No cumple"
        if media <= objetivo:
            print(f"Cajas: {n} -> {media:.4f} {cumple}")

main()