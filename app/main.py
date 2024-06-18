import charts 
import read
import pandas as pd



def filtro1(): # ------------- Filtramos todos los países de data.csv a los del continente asiatico. 
   lista_origen = read.conversion("data.csv") # En lista_origen guardamos todos los valores; esto usando la función conversion del modulo read. 
   list_filtra = list(filter(lambda x: x["Continent"] == "South America", lista_origen))
   # En la linea 8 usamos lambda para filtrar unicamente los paises del continente asiatico, con la función filter los filter y con lista hacemos que sea una lista para guardarlos. 

   pais_filtra = [x["Country/Territory"] for x in list_filtra ] #Usando dicctionario comprenhension filtramos unicamente las claves que tengan el país para hacer una lista de estos. 
   area_filtra = [x[ "Area (km²)"] for x in list_filtra ]  #Usando dicctionario comprenhension filtramos unicamente las claves que tengan el Área para hacer una lista de estos. 
   
   return pais_filtra, area_filtra #Retornamos las listas filtradas

#labels, values = filtro1() #Guardamos las listas en cada variable. 


def filtro_pandas(): # ------------- Filtramos todos los países de data.csv a los del continente Africano, pero usando el modulo pandas. 
      df = pd.read_csv("data.csv") # con la función read.csv de pandas leemos el csv. 

      df = df[df["Continent"] == "Africa"] # Filtramos los paises que no son del continente africano 

      pais_filtra = df["Country/Territory"].values #Con pandas filtramos por la clave país y con .values = Guardamos los Paises. 
      area_filtra =  df["Area (km²)"].values # Con pandas filtramos el área de cada pais y con .values agregamos los valores a la lista. 

      return pais_filtra, area_filtra   #Retornamos las listas. 

labels, values = filtro_pandas() #Guardamos las listas en cada variable. 

charts.generate_pie_chart(labels, values) #Usando el modulo charts creamos una grafica de pastel con los paises de asia y su area total. 





   
   

   
   
