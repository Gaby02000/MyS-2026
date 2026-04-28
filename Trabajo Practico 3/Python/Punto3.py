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
    return - (1 / lambd) * np.log(u) #X = -(1/λ) * ln(U)

def graficar_exponencial(datos):
    plt.hist(datos, bins=20, color='red', edgecolor='black')
    plt.title("HISTOGRAMA DE UNIFORME A EXPONENCIAL EXPONENCIAL (λ = 12)")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.savefig("../graficos/histograma_punto3_python_exponencial.png")
    plt.show()

def generar_exponencial(lambd, n): #distribución exponencial   
    return np.random.exponential(scale=1/lambd, size=n) #f(x) = λ e^{-λx}

def graficar_muestras_comparacion(muestras):
    x = [100, 1000, 10000]
    plt.figure(figsize=(15, 4))
    for i in range(len(muestras)):
        plt.subplot(1, 3, i + 1)
        plt.hist(muestras[i], bins=50, color='red', edgecolor='black') #mientras mas intervalos se aprecia mejor la comparativa
        plt.title(f"HISTOGRAMA DE EXPONENCIAL (λ=3 (n={x[i]}))")
        plt.xlabel("Valores")
        plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("../graficos/histogramas_punto3_python_comparacion.png")
    plt.show()

def guardar_txt(muestras, archivo = "datos_punto3_python.txt"):
    x = [100, 1000, 10000]
    with open(archivo, "w") as f:
        for i in range(len(muestras)):
            datos = muestras[i]
            media = np.mean(datos)
            desvio = np.std(datos)
            varianza = np.var(datos)
            f.write(f"EXPONENCIAL lambda=3 (n={x[i]})\n")
            f.write("RESULTADOS\n")
            f.write(f"Media: {media}\n")
            f.write(f"Desvío estándar: {desvio}\n")
            f.write(f"Varianza: {varianza}\n")
            f.write("\nDATOS GENERADOS:\n")
            print(f"\nEXPONENCIAL lambda=3 (n={x[i]})")
            print(f"Media: {media}")
            print(f"Desvío estándar: {desvio}")
            print(f"Varianza: {varianza}")
            for valor in datos:
                f.write(f"{valor}\n")
        f.write("\n\n")

def main():
    uniforme = leer_muestras( "datos_punto2_python.txt" )
    exp_transformada = transformar_a_exponencial(uniforme, 12)
    graficar_exponencial(exp_transformada)
    e1 = generar_exponencial(3, 100)
    e2 = generar_exponencial(3, 1000)
    e3 = generar_exponencial(3, 10000)
    muestras = [e1, e2, e3]
    graficar_muestras_comparacion(muestras)
    guardar_txt(muestras)

main()