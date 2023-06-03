## server 46.101.199.136
```bash
openssl genrsa -out server.key 2048
openssl req -new -x509 -sha256 -key server.key -out server.crt -days 365
```

## client 209.38.227.80
```bash
openssl genrsa -out client.key 2048
openssl req -new -x509 -sha256 -key client.key -out client.crt -days 365
```

## Ubuntu
```bash
На Ubuntu хранилище SSL сертификатов обычно находится в каталоге `/etc/ssl/certs/`. В этом каталоге хранятся системные сертификаты, которым доверяет операционная система.

Чтобы добавить самоподписанный сертификат в хранилище на Ubuntu, можно выполнить следующие шаги:

1. Скопируйте файл самоподписанного сертификата (обычно это файл с расширением .crt или .pem) в каталог `/usr/local/share/ca-certificates/`. Можно использовать команду `sudo cp server.crt /usr/local/share/ca-certificates/`, замените `server.crt` на имя вашего сертификата.

2. Перейдите в каталог `/usr/local/share/ca-certificates/` с помощью команды `cd /usr/local/share/ca-certificates/`.

3. Обновите список сертификатов с помощью команды `sudo update-ca-certificates`.

   Эта команда автоматически обновит список сертификатов, добавив ваш самоподписанный сертификат в `/etc/ssl/certs/`. Файл сертификата будет скопирован в каталог `/etc/ssl/certs/` и будут созданы символические ссылки для обеспечения доступности сертификата.

После выполнения этих шагов ваш самоподписанный сертификат будет добавлен в системное хранилище сертификатов на Ubuntu. Вы можете использовать его в своих приложениях, и они смогут доверять этому сертификату при проверке SSL.
```

## Macos
```bash
На macOS сертификаты, добавленные в Keychain, автоматически доступны для использования всеми приложениями, которые используют системное хранилище сертификатов Keychain.

Если вы добавили свой самоподписанный сертификат в Keychain на macOS, то он будет автоматически доступен в любом приложении, которое использует системные сертификаты Keychain.

В этом коде клиента мы создаем SSL контекст с использованием ssl.create_default_context(ssl.Purpose.SERVER_AUTH), что позволяет использовать системное хранилище сертификатов на macOS.

Затем мы устанавливаем SSL соединение с сервером, используя ssl_context.wrap_socket(), и отправляем данные на сервер.
```

## Пример использования

```bash
tcp.flags.ack==0
tls
```

![image](https://github.com/nvinnikov/cryptographic_protocols/assets/88853518/fdca0d0f-c1f8-484c-a00a-01fb13733479)

![image](https://github.com/nvinnikov/cryptographic_protocols/assets/88853518/d4295d3b-774a-49bc-a1aa-f9dda1a06a05)

![image](https://github.com/nvinnikov/cryptographic_protocols/assets/88853518/936dce78-9847-4461-8c3f-4a09a591f031)

![image](https://github.com/nvinnikov/cryptographic_protocols/assets/88853518/f45a1447-b8c9-4490-91cc-21106382c534)

![image](https://github.com/nvinnikov/cryptographic_protocols/assets/88853518/68b50841-d436-4f7f-9a86-f90cb37d684f)


