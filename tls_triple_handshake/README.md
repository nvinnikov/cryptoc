## server
```bash
openssl genrsa -out server.key 2048
openssl req -new -x509 -sha256 -key server.key -out server.crt -days 365
```

## client
```bash
openssl genrsa -out client.key 2048
openssl req -new -x509 -sha256 -key client.key -out client.crt -days 365
```
