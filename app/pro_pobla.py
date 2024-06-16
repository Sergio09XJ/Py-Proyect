import matplotlib.pyplot as plt
import csv

#------------------------------ conversion; de un csv, lo transforma a una lista de diccionarios. 
def conversion(path):
  diccionario = {}
  lista = []
  with open(path, "r") as files:
    clave = files.readline().strip()
    clave_f = clave.split(",")
    
    for file in files: 
      valores = file.strip().split(",")
      diccionario = dict(zip(clave_f, valores))
      lista.append(diccionario)
    return lista 

lista_g = conversion("data.csv")

# .............................. eleccion; elige el país a graficar. 
def eleccion(lista_g): 
  while True:

    pais = input("Elige un País del cual quieras graficar su población: ")
    pais = pais.capitalize()

    for elemento in lista_g: 
      if pais == elemento["Country/Territory"]:
        return elemento 

    pais = input("Tu país esta mal, damelo de nuevo: ")
  
pais = eleccion(lista_g)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,, grafica; grafica la población
def grafica(pais):

  valores = ["2022 P.", "2020 P.", "2015 P.", "2010 P.", "2000 P.", "1990 P", "1980 P", "1970 P"]
  
  altura = [int(pais["2022 Population"]),int(pais["2020 Population"]), int(pais["2015 Population"]), int(pais["2010 Population"]), int(pais["2000 Population"]), int(pais["1990 Population"]), int(pais[ "1980 Population"]),int(pais["1970 Population"])]
  

  print(valores)
  print(altura)
   
  fig, ax = plt.subplots()
  ax.bar(valores, altura)
  plt.show()


if __name__ == "__main__":
  grafica(pais)