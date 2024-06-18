import matplotlib.pyplot as plt  #Importamos el módulo de maplotlib

#------------------- Creamos la función generate... esto con el objetivo de crear graficas de barras. 
def generate_bar_chart(labels,values):
  
  fig, ax = plt.subplots() #La función subplots crea tanto la figura como los ejes de la gráfica. 
  ax.bar(labels, values)#Creamos la gráfica bar con labels y values. 
  plt.savefig("bar.png") #Guardamos la grafica en bar.png
  plt.close()#Cerramos la figura para liberar recursos de la memoria. 

# ------------- Creamos la función generate... esto con el objetivo de crear graficas de pastel. 
def generate_pie_chart(labels,values):
  
  fig, ax = plt.subplots() #La función subplots crea tanto la figura como los ejes de la gráfica. 
  ax.pie(values, labels = labels)#Creamos la gráfica pie con labels y values. 
  ax.axis("equal") #Esta función hace que los ejes tengan una escala igualitaria, con el objetivo de que no se distorcionen. 
  plt.savefig("pais_porcent.png") #Guardamos la grafica en pais_porcent.png
  plt.close()#Cerramos la figura para liberar recursos de la memoria. a

if __name__ == "__main__": #Permite que el archivo sea tratado como main y tambien como modulo cuando lo usamos con main.py  = Entry-point
  generate_pie_chart(labels, values)
  
