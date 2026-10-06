contrasena ="mimamamemima"
longitud_minima =8
longitud_maxima =20

longitud = len(contrasena)

if longitud <longitud_minima:
    print("muy corta")
elif longitud >longitud_maxima:
    print("muy larga")
elif longitud >longitud_minima and longitud <longitud_maxima:
    print("Valida")

#Bucles
colores = ["rojo", "verde", "azul", "amarillo"]
for color in colores:
    print(color)

#Bucle while
numeros = [7,8,9,10,11]
contador =7
while contador < 11:
    print(contador)
    contador +=1