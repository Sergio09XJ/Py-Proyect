import csv 
import charts

def filtracion():
  diccionario = {}
  pais = []
  total_p = []
  
  with open("data.csv", "r") as files:
     clave = files.readline().strip()
     clave_f = clave.split(",")

     for file in files: 
       valores = file.strip().split(",")
       diccionario = dict(zip(clave_f, valores))
       pais.append(diccionario["CCA3"])
       total_p.append(float(diccionario["World Population Percentage"]))
  
  return pais, total_p

paises, poblacion = filtracion()

charts.generate_bar_chart(paises, poblacion)


