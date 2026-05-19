# FastApi y postgres

## Construir imagen de la aplicación

Se le facilita fichero `Dockerfile`.

## Desplegar aplicación y servicios necesarios

Se le facilita fichero `compose.yaml`.

## Probar en local

```sh
$ curl http://127.0.0.1
{"message":"FastAPI funcionando en Docker"}
```

```sh
$ curl http://127.0.0.1/db-check
{"status":"Conexión a la base de datos exitosa"}
```

## Probar en AWS tras devops

```sh
$ curl http://IP_AWS
{"message":"FastAPI funcionando en Docker"}
```

```sh
$ curl http://IP_AWS/db-check
{"status":"Conexión a la base de datos exitosa"}
```
