import socket

def main():
    # Crear un socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    s.connect(('localhost', 12345))

    # Solicitar el número de teléfono
    phone_number = input('Introduce el número de teléfono: ')

    # Enviar el número de teléfono al servidor
    s.sendall(phone_number.encode())

    # Recibir la respuesta del servidor
    response = s.recv(1024).decode()

    # Imprimir la respuesta
    print(response)

    # Cerrar el socket
    s.close()

if __name__ == "__main__":
    main()