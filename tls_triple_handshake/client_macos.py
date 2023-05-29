import socket
import ssl

# Создание TCP/IP сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('46.101.199.136', 8090)

try:
    # Создание SSL контекста без проверки сертификата
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Установка SSL соединения с сервером
    ssl_client_socket = ssl_context.wrap_socket(client_socket, server_hostname="46.101.199.136")
    ssl_client_socket.connect(server_address)

    # Отправка данных на сервер
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    request_data = f"POST /login HTTP/1.1\r\nHost: 46.101.199.136\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(username) + len(password) + 13}\r\n\r\nusername={username}&password={password}"
    ssl_client_socket.sendall(request_data.encode())

    # Получение и вывод ответа от сервера
    response = ssl_client_socket.recv(4096)
    print(response.decode())

except Exception as e:
    print(f"Ошибка при подключении к серверу: {e}")

finally:
    # Закрытие соединения
    ssl_client_socket.close()
