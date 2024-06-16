import random 

print("\n--------- Piedra || Papel || Tijeras ----------- ")
print(" ")
print(" -- Este es un juego de piedra, papel o tijeras; -- ")
print(" -- tu eliges tu movimiento y despues la máquina,-- ")
print("        --  hasta que uno tenga 2 wins.  --      \n")


def datos_usua():
    verdadero = True
    while verdadero == True:
     eleccion_h = input("Que Eliges, ¿Piedra, Papel o Tijera? ")
     eleccion_h = eleccion_h.lower()
     if (eleccion_h == "piedra") or (eleccion_h == "papel") or (eleccion_h == "tijera"): 
        verdadero = False

    return eleccion_h        



def datos_mchne():
   eleccion_bas = random.randint(1,3)
   if eleccion_bas == 1:
      eleccion_m = "piedra"
   elif eleccion_bas == 2: 
      eleccion_m = "papel"  
   else: 
      eleccion_m = "tijera"   

   return eleccion_m


  

def combate(datos_usua, datos_mchne): 
   
   victorias_h = 0
   victorias_m = 0
   round = 1

   while (victorias_h < 2) and (victorias_m < 2): 
     
     print("\nRound " + str(round))
     punto_h = datos_usua() 
     punto_m = datos_mchne()
     print("-Elegiste: " + punto_h)
     print("-La Máquina eligió: " + punto_m)
     round += 1

     if punto_h == punto_m: 
       print(" Tu = " + str(victorias_h) + " vs " + str(victorias_m) + " = Maquina")
     elif (punto_h ==  "piedra" and punto_m == "papel") or (punto_h ==  "papel" and punto_m == "tijera") or (punto_h ==  "tijera" and punto_m == "piedra"):
       victorias_m = victorias_m + 1
       print(" Tu = " + str(victorias_h) + " vs " + str(victorias_m) + " = Maquina")
     else:
       victorias_h = victorias_h + 1  
       print(" Tu = " + str(victorias_h) + " vs " + str(victorias_m) + " = Maquina")
   
   if victorias_h == 2: 
    print("\nLe ganaste a la máquina!! Felicidades! \n")
   elif victorias_m == 2: 
      print("\nTe gano la máquina!! Lo lamento! \n")

combate(datos_usua, datos_mchne)

