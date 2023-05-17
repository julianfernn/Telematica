# Telematica
Proyecto final de telematica

Primero, clona nuestro repositorio en tu entorno local.

****git clone https://github.com/julianfernn/Telematica.git***

Si está ejecutando esta aplicación dentro de un entorno de nube, debe modificar el archivo web.py y cambiar la dirección localhost a su dirección IP pública, de la misma manera se recomienda utilizar direcciones IP elásticas.



Si está en un entorno de nube, habilite también el puerto 8080 y el puerto 5600 en los grupos de seguridad

Este archivo actualizará el repositorio de paquetes e instalará docker compose junto con dos imágenes, mysql y ubuntu, finalmente, ejecutará el archivo docker-compose.yml, que creará tres contenedores.

 ****sudo sh ./inicio.sh****

 