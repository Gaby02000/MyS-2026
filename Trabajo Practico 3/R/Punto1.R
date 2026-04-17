#Genere un conjunto de 100 datos numéricos para una variable imaginaria y con ayuda de los lenguajes:
#Calcule la media.
#Calcule el desvío estándar.
#Calcule la varianza. 
#¿Cómo se crean gráficos para interpretar los valores generados? Describa qué método/función se ha invocado junto con sus parámetros.


generar_datos <- function() {
  rnorm(100, mean=100, sd=23)  # Genera 100 datos con distribución normal
}

calcular_estadisticas <- function(datos) {
  media <- mean(datos)        # Calcula media
  desvio <- sd(datos)         # Calcula desvío estándar
  varianza <- var(datos)      # Calcula varianza
  return(list(media, desvio, varianza))
}

mostrar_resultados <- function(media, desvio, varianza) {
  cat("Media:", media, "\n")
  cat("Desvío estándar:", desvio, "\n")
  cat("Varianza:", varianza, "\n")
}

graficar_histograma <- function(datos) {
  pdf("../graficos/histograma_punto1_R.pdf")  
  
  hist(datos,breaks=10, col="red", border="black", main="HISTOGRAMA", xlab="Valores",ylab="Frecuencia")

  dev.off()
}

guardar_txt <- function(datos, media, desvio, varianza, archivo="datos_punto1_R.txt") {
  fileConn <- file(archivo, open = "w")
  
  writeLines("RESULTADOS", fileConn)
  writeLines(paste("Media:", media), fileConn)
  writeLines(paste("Desvío estándar:", desvio), fileConn)
  writeLines(paste("Varianza:", varianza), fileConn)
  writeLines("", fileConn)
  writeLines("DATOS GENERADOS", fileConn)
  writeLines(as.character(datos), fileConn)
  
  close(fileConn)
}

main <- function() {
  datos <- generar_datos()
  resultados <- calcular_estadisticas(datos)
  media <- resultados[[1]]
  desvio <- resultados[[2]]
  varianza <- resultados[[3]]
  
  guardar_txt(datos, media, desvio, varianza)
  mostrar_resultados(media, desvio, varianza)
  graficar_histograma(datos)
}

main()