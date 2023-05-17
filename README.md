# Telematica
Proyecto final de telematica

Primero, clona nuestro repositorio en tu entorno local.

****git clone https://github.com/julianfernn/Telematica.git***

Si está ejecutando esta aplicación dentro de un entorno de nube, debe modificar el archivo web.py y cambiar la dirección localhost a su dirección IP pública, de la misma manera se recomienda utilizar direcciones IP elásticas.

![image](https://github.com/julianfernn/Telematica/assets/133823825/732eb32a-4386-47b0-a826-136d424ca221)


Si está en un entorno de nube, habilite también el puerto 8080 y el puerto 5600 en los grupos de seguridad

![image](https://github.com/julianfernn/Telematica/assets/133823825/396870e5-7397-426b-8a24-e142635ef134)

#ACTUALIZAR REPOSITORIOS
Este archivo actualizará el repositorio de paquetes e instalará docker compose junto con dos imágenes, mysql y ubuntu, finalmente, ejecutará el archivo docker-compose.yml, que creará tres contenedores.

 ****sudo sh ./Docker.sh****

 
