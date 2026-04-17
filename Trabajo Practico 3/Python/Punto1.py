"""
Genere un conjunto de 100 datos numéricos para una variable imaginaria y con ayuda de los lenguajes:
Calcule la media.
Calcule el desvío estándar.
Calcule la varianza. 
¿Cómo se crean gráficos para interpretar los valores generados? Describa qué método/función se ha invocado junto con sus parámetros.
"""

import numpy as np
import matplotlib.pyplot as plt

def generar_datos(n):
    return np.random.normal(loc=100, scale=23 , size=n)    # Genera 100 datos con distribución normal (media=100, desvio=23)

def calcular_estadisticas(datos):
    media = np.mean(datos) # Calcula media 
    desvio = np.std(datos) # Calcula desvio estandar
    varianza = np.var(datos)  # Calcula varianza
    return media, desvio, varianza

def mostrar_resultados(media, desvio, varianza):
    print(f"Media: {media}")
    print(f"Desvio estandar: {desvio}")
    print(f"Varianza: {varianza}")
  
def graficar_histograma(datos):
    plt.hist(datos, bins=10, color='red', edgecolor='black') #Crea un histograma con los datos generados con 10 intervalos
    plt.title("HISTOGRAMA", fontsize=20)
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.savefig("../graficos/histograma_punto1_python.png")
    plt.show()

def guardar_txt(datos,media, desvio, varianza, archivo="datos_punto1_python.txt"): 
    with open(archivo, "w") as f:
        f.write("RESULTADOS\n")
        f.write(f"Media: {media}\n")
        f.write(f"Desvío estándar: {desvio}\n")
        f.write(f"Varianza: {varianza}\n\n")
        
        f.write( "DATOS GENERADOS\n")
        for i, valor in enumerate(datos):
            f.write(f"{valor}\n")

def main():
    datos = generar_datos(100)
    media, desvio, varianza = calcular_estadisticas(datos)
    guardar_txt(datos, media, desvio, varianza)
    mostrar_resultados(media, desvio, varianza)
    graficar_histograma(datos)

main()