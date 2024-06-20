FROM python:3.9 
#Le decimes de que versión de python partir. 

# Instalar zsh esto para usar este shell en vez de bash 
RUN apt-get update && apt-get install -y \
    zsh \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app-dock 
#Creamos una carpeta donde guardar todo lo de docker
COPY requirements.txt /app-dock/requirements.txt
# Iquierda = Lado del Local / Derecha = Lado del Contendor

RUN pip install --no-cache-dir --upgrade -r /app-dock/requirements.txt
# Gracias a la versión de python va a saber que pip usar. 
# --no-cache-dir = NO aplica el cache a la instalación
# --upgrade = Nos permite actualizar el gestor de paquetes, si hay una.

COPY . /app-dock
#Todo el código lo llevamos a la carpeta de docker. 

#Con el archivo docker-compose.yml corremos los scripts en docker

CMD zsh -c "while true; do sleep 1; done"
#Este comando nos permite mantener en ejecución constante este contenderor. 
