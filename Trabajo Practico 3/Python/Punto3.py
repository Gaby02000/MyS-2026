"""
A partir de la muestra obtenida de 1000 valores en el punto 2.a, realice:
Una función de transformación para que la variable aleatoria tenga una distribución de probabilidad Exponencial con parámetro λ = 12.
Un gráfico adecuado para la variable aleatoria del inciso anterior.
Genere tres muestras con 100, 1000 y 10000 valores aleatorios pero esta vez siguiendo una distribución Exponencial con parámetro λ = 3.
Grafique las muestras del inciso c. ¿Qué diferencia visual encuentra entre los gráficos?
"""

import numpy as np
import matplotlib.pyplot as plt

def leer_muestras(archivo): #leo y guardo los datos de la distribucion uniforme en las muestras
    uniforme = []
    en_uniforme = False
    with open(archivo, "r") as f:
        for linea in f:
            linea = linea.strip()
            if linea == "DISTRIBUCIÓN UNIFORME":
                en_uniforme = True
                continue
            if linea.startswith("DISTRIBUCIÓN") and linea != "DISTRIBUCIÓN UNIFORME":
                en_uniforme = False
            if en_uniforme and linea and linea != "DATOS GENERADOS:":
                uniforme.append(float(linea))
    return np.array(uniforme)

def transformar_a_exponencial(u, lambd): #transformo la distribucion uniforme a exponencial, en este caso λ = 12
    return - (1 / lambd) * np.log(u)

def graficar_exponencial(datos):
    plt.hist(datos, bins=20, color='red', edgecolor='black')
    plt.title("HISTOGRAMA DE EXPONENCIAL (λ = 12)")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.savefig("../graficos/histograma_punto3_python_exponencial.png")
    plt.show()

def generar_exponencial(lambd, n):
    return np.random.exponential(scale=1/lambd, size=n)

def main():
    uniforme = leer_muestras( "datos_punto2_python.txt" )
    exp_transformada = transformar_a_exponencial(uniforme, 12) 
    graficar_exponencial(exp_transformada)

main()