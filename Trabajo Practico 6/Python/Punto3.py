import numpy as np
import matplotlib.pyplot as plt

CANT_ANIOS = 30
DIAS = 365
INVENTARIO_INICIAL = 150
CANTIDAD_PEDIDO = 100
LAMBDA_DEMANDA = 37
TIEMPO_ENTREGA = 3
COSTO_COMPRA = 450
COSTO_ORDEN = 93
COSTO_MANTENIMIENTO = 35
COSTO_FALTANTE = 20
PUNTOS_REORDEN = [15, 30, 40]
Z_95 = 1.96
np.random.seed(42)

def generar_demanda():
    return np.random.poisson(LAMBDA_DEMANDA)

def simular_anio(punto_reorden):
    inventario = INVENTARIO_INICIAL
    costo_compra = 0
    costo_ordenar = 0
    costo_mantenimiento = 0
    costo_faltante = 0
    pedidos_pendientes = []
    for dia in range(1, DIAS + 1):
        pedidos_recibidos = []
        for llegada in pedidos_pendientes:
            if llegada == dia:
                inventario += CANTIDAD_PEDIDO
                pedidos_recibidos.append(llegada)
        for llegada in pedidos_recibidos:
            pedidos_pendientes.remove(llegada)
        demanda = generar_demanda()
        if inventario >= demanda:
            inventario -= demanda
        else:
            faltante = demanda - inventario
            costo_faltante += (faltante * COSTO_FALTANTE)
            inventario = 0
        costo_mantenimiento += (inventario * COSTO_MANTENIMIENTO)
        if inventario <= punto_reorden:
            pedidos_pendientes.append(dia + TIEMPO_ENTREGA)
            costo_ordenar += (CANTIDAD_PEDIDO * COSTO_ORDEN)
            costo_compra += (CANTIDAD_PEDIDO * COSTO_COMPRA)
    costo_total = (costo_compra+ costo_ordenar + costo_mantenimiento + costo_faltante)
    costo_mensual = costo_total / 12
    return costo_mensual

def calcular_ic(costos):
    media = np.mean(costos)
    desvio = np.std(costos, ddof=1)
    error_estandar = (desvio / np.sqrt(CANT_ANIOS))
    ic_inferior = (media - Z_95 * error_estandar)
    ic_superior = (media + Z_95 * error_estandar)
    return media, ic_inferior, ic_superior

def mostrar_resultados(punto_reorden, promedio_costo, ic_inf, ic_sup):
    print("==========================================")
    print(f"PUNTO DE REORDEN = {punto_reorden}")
    print("==========================================")

    print(f"Costo mensual promedio: ${promedio_costo:,.2f}")
    print("\nINTERVALO DE CONFIANZA 95%")
    print(f"IC Inferior: ${ic_inf:,.2f}")
    print(f"IC Superior: ${ic_sup:,.2f}")
    print()

def graficar_histograma(costos, punto_reorden):
    plt.figure(figsize=(10, 5))
    plt.hist(costos, bins=15, color="skyblue", edgecolor="black")
    plt.title(f"Distribución del Costo Mensual\nPunto de Reorden = {punto_reorden}")
    plt.xlabel("Costo mensual")
    plt.ylabel( "Frecuencia")
    plt.show()

def main():
    for punto_reorden in PUNTOS_REORDEN:
        costos_mensuales = []
        for anio in range(CANT_ANIOS):
            costo_mensual = simular_anio(punto_reorden)
            costos_mensuales.append(costo_mensual)
        promedio_costo, ic_inf, ic_sup = (calcular_ic(costos_mensuales))
        mostrar_resultados(punto_reorden, promedio_costo, ic_inf, ic_sup)
        graficar_histograma(costos_mensuales, punto_reorden)

main()