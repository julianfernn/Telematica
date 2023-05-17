#Actualiazaciones
sudo apt update
# Instalar docker
sudo apt install -y docker-compose
#Descargar las imagenes
sudo docker pull ubuntu:latest
sudo docker pull mysql:latest
# lanzar los contenedores
sudo docker-compose up