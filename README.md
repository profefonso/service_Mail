# service_Mail
django send mail

Envio de Mensajes Python Django API REST.

  - Enviar Mensajes usando un servidor SMTP


### Tecnologias 

Desarrollado usando tecnologias:

* [Python] - Django Rest Framework - Gunicorn.
* [Docker] - Gestion de contenedores y despliegue.
* [Nginx] - Servidor de aplicaciones.

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Instalación

Para la instalación requiere [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/).

Clonar el proyecto e ingresar al directorio creado

```sh
$ git clone https://github.com/profefonso/service_Mail.git
$ cd JWT-Python
```

Descargar y construir las imagenes necesarias

```sh
$ docker-compose build
$ docker-compose up 
```

### Probar App

Ingrese a la direccion para ver la documentacion del API en swagger
[http://localhost:8085/api/](http://localhost:8085/api/)

#### Enviar Mensaje:

```sh
$ curl -X POST -H "Content-Type: application/json" \
 -d '{ "mail_list": ["mailuno@gmail.com", "maildos@yahoo.es"], "subject": "Notification Fake", "template": "notification_mail", "content_data": { "offender_name":"Alfonso", "body_message": "Cuerpo del Mensaje", "date":"12-12-12" }}' \
 http://localhost:8085/notification/
```
