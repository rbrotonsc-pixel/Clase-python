lista_edades = [15, 22, 17, 30, 65, 45, 70, 19]
numero_maximo = 65
for edad in lista_edades:
     if edad >=65:
            break
     if edad > 18:
        print(edad)


intentos = 0

while intentos < 5:
    try:
        numero = int(input("Introduce un número: "))
        print("Número válido")
        break
    except ValueError:
        print("Eso no es un número")
        intentos += 1
                    
          
     
