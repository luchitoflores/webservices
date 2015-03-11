# -*- encoding: utf-8 -*-
#Activamos los imports absolutos para evitar conflictos entre packages
from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

#indicamos el Django settings module por defecto para nuestro programa celery (no es necesario pero asi evitamos tener que pasarle siempre al programa celery nuestro módulo settings) 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webservices.settings')

app = Celery('webservices')

#Añadimos el Django settings module como fuente de configuración de Celery (nos permite configurar Celery directamente desde el Django settings). Al pasarlo como string nos ahorramos un problema si trabajasemos con windows. 
app.config_from_object('django.conf:settings')

# Si tenemos nuestras tareas en un fichero de nombre tasks.py, esto nos permite indicarle a celery que encuentre automáticamente dicho módulo dentro del proyecto. De este modo no tenemos que añadirlo a la variable CELERY_IMPORTS del settings 
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

