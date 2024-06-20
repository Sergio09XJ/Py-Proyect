FROM python:3.10
#Le decimes de que versión de python partir. 

# Instalar zsh esto para usar este shell en vez de bash 
RUN apt-get update && apt-get install -y \
    zsh \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /web-dock 
#Creamos una carpeta donde guardar todo lo de docker
COPY requirements.txt /web-dock/requirements.txt
# Iquierda = Lado del Local / Derecha = Lado del Contendor

RUN pip install --no-cache-dir --upgrade -r /web-dock/requirements.txt
# Gracias a la versión de python va a saber que pip usar. 
# --no-cache-dir = NO aplica el cache a la instalación
# --upgrade = Nos permite actualizar el gestor de paquetes, si hay una.

COPY . /web-dock
#Todo el código lo llevamos a la carpeta de docker. 

#Con el archivo docker-compose.yml corremos el servidor en docker

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"] 
#Este comando nos permite mantener en ejecución constante este contendor.
#Hacerlo entre corchetes solo es otra forma de escribirlo.
#Y el contenido cambia porque en este caso no es para scripts si no para servidores. 
