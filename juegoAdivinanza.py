#JUEGO DE ADIVINANZA DE PYTHON

import random



def num_aleatorio():
    #numero secreto del 1 - 100
    aleatorio = random.randint(1,100)
    intentos = 0
    estado = "Perdiste"

    #lineas de bienvenida
    print("Bienvenido al Juego de Adivinanza de Numero")
    print("Deberas adivinar un numero del 1 al 100")
    print("Iniciemos!!")

    while intentos < 5:
        #solicitud de numero del 1 al 100
        num = input("Ingrese un numero, por favor: ")

        #verificamos que sea un numero
        if num.isdigit():
            num = int(num) # de texto a entero
            if (num >= 0 and num <= 100):
                intentos += 1

                if num == aleatorio:
                    estado = "Ganaste"
                    print("Es correcto, el numero es ",num)
                elif num < aleatorio:
                    print("Debe ingresar un numero mas grande")
                else:
                    print("Debe ingresar un numero mas pequeño") 
            else:
                print("Debe ingresar un numero del 1 al 100")        
        else:
            print("Por favor introducir un valor valido!!")           
        
    finalizacion = input(f"El juego a finalizado,has {estado} quieres jugar otra vez? (si/no)").lower()

    if finalizacion == "si":
        num_aleatorio()
    else:
        return "Muchas gracias por jugar, hasta la proxima!!"    

print(num_aleatorio())






