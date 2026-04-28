"""
Genere una muestra de 1000 valores que siga la distribución Normal, con media 5 y desvío estándar igual a 3. Codifique una función o método que permita calcular un intervalo de confianza para estimar el valor de la media poblacional. Deberá obtener el coeficiente z para un 99% de confiabilidad y retornar el resultado contemplando  2 desvíos estándar en la fórmula. 
Para el cálculo del coeficiente z, utilice la tabla disponible en la bibliografía.
Ejemplo: para un 95% de confiabilidad, z=1.96.
El intervalo de confianza se conforma de la siguiente manera:

Donde X, representa la media muestral,  es el desvío estándar de dicha muestra y n, es el número de elementos de la muestra. Se dice entonces que:
X - 1.96 n   X + 1.96 n      
Donde   es la media poblacional.
"""

import numpy as np

def generar_datos(media, desvio, n):
    return np.random.normal(loc=media, scale=desvio, size=n)

def calcular_estadisticas(datos):
    media = np.mean(datos)
    desvio = np.std(datos, ddof=1)  
    return media, desvio

def intervalo_confianza(media, desvio, n, z):
    margen = z * (desvio / np.sqrt(n)) 
    li = media - margen
    ls = media + margen
    return li, ls

def guardar_txt(datos, media, desvio, li, ls, archivo="datos_punto5_python.txt"):
    with open(archivo, "w") as f:

        f.write("RESULTADOS\n")
        f.write(f"Media: {media:.4f}\n")
        f.write(f"Desvío estándar: {desvio:.4f}\n")

        f.write("\nINTERVALO DE CONFIANZA (99%)\n")
        f.write(f"{li:.4f} <= mu <= {ls:.4f}\n")

        f.write("\nVALORES GENERADOS:\n")
        for valor in datos:
            f.write(f"{valor}\n")

def mostrar_resultados(media, desvio, li, ls):
    print("RESULTADOS")
    print(f"Media: {media:.4f}")
    print(f"Desvío estándar: {desvio:.4f}")

    print("\nINTERVALO DE CONFIANZA (99%)")
    print(f"{li:.4f} <= mu <= {ls:.4f}")

def verificar_intervalo(li, ls, media_real=5):
    if li <= media_real <= ls:
        print("\nLa media poblacional (mu=5) está dentro del intervalo")
    else:
        print("\nLa media poblacional (mu=5) NO está dentro del intervalo")

def main():
    m = 5 # Media
    d = 3 # Desvio
    n = 1000
    datos = generar_datos(m, d, n)
    media, desvio = calcular_estadisticas(datos)
    z = 2.576 # Coeficiente z para 99%
    li, ls = intervalo_confianza(media, desvio, n, z)
    mostrar_resultados(media, desvio, li, ls)
    verificar_intervalo(li, ls, m)
    guardar_txt(datos, media, desvio, li, ls)

main()