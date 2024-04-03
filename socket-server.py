import socket
import mysql.connector

def main():
    # Crear un socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar el socket a un puerto específico
    s.bind(('localhost', 12345))

    # Escuchar conexiones entrantes
    s.listen(1)

    while True:
        # Aceptar una conexión entrante
        conn, addr = s.accept()

        # Recibir el número de teléfono del cliente
        phone_number = conn.recv(1024).decode()

        # Conectar a la base de datos
        db_conn = mysql.connector.connect(
            host="socket-server-mysql",
            user="root",
            password="123456899",
            database="socket_server"
        )
        cursor = db_conn.cursor()

        # Buscar la información de la persona en la base de datos
        cursor.execute("SELECT p.dir_tel, p.dir_nombre, p.dir_direccion, c.ciud_nombre FROM personas p INNER JOIN ciudades c on c.ciud_id = p.dir_ciud_id WHERE p.dir_tel = %s", (phone_number,))
        result = cursor.fetchone()

        if result is not None:
            # Enviar la información de la persona al cliente
            conn.sendall(str(result).encode())
        else:
            # Enviar un mensaje al cliente indicando que la persona no fue encontrada
            conn.sendall('Persona dueña de ese número telefónico no existe'.encode())

        # Cerrar la conexión con la base de datos
        db_conn.close()

        # Cerrar la conexión con el cliente
        conn.close()

if __name__ == "__main__":
    main()
