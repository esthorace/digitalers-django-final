# Django

## Crear un proyecto

    mkdir src
    cd src
    django-admin startproject config .

## Comprobar posibles problemas en el proyecto

    python manage.py check

## Ejecutar el servidor

    python manage.py runserver

## Crear una aplicación

    python manage.py startapp app

## Crear las migraciones

    python manage.py makemigrations

## Aplicar las migraciones

    python manage.py migrate

## Crear superusuario

    python manage.py createsuperuser

## Uso del shell
    
    python manage.py shell