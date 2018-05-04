#install.packages("deSolve")
  require(deSolve)
# Para la constante de emisividad del cuerpo para la ecuacion de Boltzman
# debe estar entre 0 y 1. Para este caso se trabajo con g = 0.5
  
# Condiciones iniciales
# T0 = 180K
# Te = 200k
# g ("Constante de emisividad") = 0.5
# C = 100J/(Kg/K)
  
fp = function(t,y, parms){
  s = -1.68*10^(-9)*y^4+2.6880
  return(list(s)) # ode requiere salida sea una lista
}
tiempo = seq(0,200,200/20)
# Usamos la función ode()
temp = ode(c(180), tiempo, fp, parms=NULL, method = "euler") # método Runge Kutta orden 4

# Salida
tabla = cbind(tiempo, temp[,2] )
colnames(tabla) = c("Tiempo(s)", " Temperatura(Kelvin)")
tabla
# Representación2
plot(tiempo, temp[,2],col = "blue", main = "Temperatura vs Tiempo", sub = "Calculo de la temperatura mediante el Metodo de euler", xlab = "Tiempo(S)", ylab = "Temperatura(K)")