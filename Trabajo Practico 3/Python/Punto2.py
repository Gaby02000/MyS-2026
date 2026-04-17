"""
Teniendo en cuenta el material teórico y los lenguajes investigados en el punto 1, elija uno de ellos y genere 1000 valores de números aleatorios:
Uniforme, con parámetros: Min: 0, Max: 1. 
Normal, con parámetros: Media: 0, Desvío: 1.
Poisson, con parámetro: λ = 6. 
Exponencial, con parámetro:  = 34 . 
Luego realice un histograma para observar gráficamente cómo es la distribución en cada ítem.
"""

import numpy as np
import matplotlib.pyplot as plt

def generar_datos(n):
    uniforme = np.random.uniform(0, 1, n) #Genera 1000 valores aleatorios con distribución uniforme entre 0 y 1
    normal = np.random.normal(0, 1, n) #Genera 1000 valores aleatorios con distribución normal (media=0, desvío=1)
    poisson = np.random.poisson(6, n) #Genera 1000 valores aleatorios con distribución de Poisson con λ = 6
    exponencial = np.random.exponential(scale=1/34, size=n) #Genera 1000 valores aleatorios con distribución exponencial con tasa λ = 34
    return uniforme, normal, poisson, exponencial

def graficar_histograma(datos, titulo, nombre):
    plt.hist(datos, bins=10, color='red', edgecolor='black')
    plt.title(titulo)
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.savefig(f"../graficos/histograma_punto2_python_distribucion_{nombre}.png")
    plt.show()

def set_graficos(uniforme, normal, poisson, exponencial):
    graficar_histograma(uniforme, "HISTOGRAMA DISTRIBUCIÓN UNIFORME", "uniforme")
    graficar_histograma(normal, "HISTOGRAMA DISTRIBUCIÓN NORMAL", "normal")
    graficar_histograma(poisson, "HISTOGRAMA DISTRIBUCIÓN POISSON", "poisson")
    graficar_histograma(exponencial, "HISTOGRAMA DISTRIBUCIÓN EXPONENCIAL", "exponencial")

def guardar_txt(uniforme, normal, poisson, exponencial, archivo="datos_punto2_python.txt"):
    
    with open(archivo, "w") as f:
        f.write("DISTRIBUCIÓN UNIFORME\n")
        f.write("DATOS GENERADOS:\n")
        for valor in uniforme:
            f.write(f"{valor}\n")
        f.write("\n\n")

        f.write("DISTRIBUCIÓN NORMAL\n")
        f.write("DATOS GENERADOS:\n")
        for valor in normal:
            f.write(f"{valor}\n")
        f.write("\n\n")

        f.write("DISTRIBUCIÓN POISSON\n")
        f.write("DATOS GENERADOS:\n")
        for valor in poisson:
            f.write(f"{valor}\n")
        f.write("\n\n")

        f.write("DISTRIBUCIÓN EXPONENCIAL\n")
        f.write("DATOS GENERADOS:\n")
        for valor in exponencial:
            f.write(f"{valor}\n")

def main():
    uniforme, normal, poisson, exponencial = generar_datos(1000)
    guardar_txt(uniforme, normal, poisson, exponencial)
    set_graficos(uniforme, normal, poisson, exponencial)

main()