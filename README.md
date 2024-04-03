#Proyecto de Socket con Docker

Este proyecto es una implementación básica de un servidor y un cliente socket utilizando Docker para la gestión de los contenedores.

##Requisitos previos

Asegúrate de tener Docker instalado en tu sistema antes de comenzar. Puedes descargar Docker desde [este enlace](https://www.docker.com/get-started).

##Instrucciones de Uso

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd tu-repositorio
    ```

3. Ejecuta el siguiente comando para construir la imagen Docker y levantar los contenedores:

    ```bash
    docker build -t image-socket . && docker-compose up -d && docker exec -it server-socket-socket-client-1 python3 socket-client.py
    ```

    Esto construirá la imagen Docker, levantará los contenedores en segundo plano y ejecutará el cliente socket.

4. Si deseas ejecutar el cliente socket nuevamente después de la primera ejecución, puedes utilizar el siguiente comando:

    ```bash
    docker exec -it server-socket-socket-client-1 python3 socket-client.py
    ```

    Esto ejecutará el cliente socket dentro del contenedor.

## Notas Adicionales

- Asegúrate de que los puertos necesarios estén disponibles en tu máquina local para evitar conflictos con otros servicios.
- Puedes modificar los archivos `socket-server.py` y `socket-client.py` para personalizar la lógica del servidor y del cliente según tus necesidades.

¡Disfruta explorando el proyecto!
