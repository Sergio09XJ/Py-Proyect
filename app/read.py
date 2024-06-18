#------------------------------ conversion; de un csv, lo transforma a una lista de diccionarios. 
def conversion(path):
  diccionario = {}
  lista = []
  with open(path, "r") as files:
    clave = files.readline().strip() #files.readline() = Lee Linea por linea(En este caso la primera linea). strip() = Elimina espacios en blanco y caracteres de el inicio y final.  
    clave_f = clave.split(",")#Divide la cadena en valores de una lista de subcadenas, tomando como separación las comas del archivo. 
    # Esto lo hace con la primera linea que son los indices o claves para el diccionario. 

    for file in files: # Para cada linea del archivo..
      valores = file.strip().split(",") #strip = Elimina los espacios y caracteres al inicio y final,  split = divide cada valor cuando hay una coma; valores = guarda esta linea en valores. 
      diccionario = dict(zip(clave_f, valores)) # Con la función zip une los clave : valor de clave_F(indice) y cada linea valores(contenido). 
      lista.append(diccionario) #Agrega cada diccionario a la lista. 
    return lista #Regresa la lista
    #Se reinicia el ciclo hazta terminar. 

if __name__ == "__main__": #Con este if hacemos que read.py sea tratado como script pero tambien como modulo cuando lo usamos en main.py =  Entry point.
      conversion(path)
    
   