from django.contrib import admin
from django.urls import path, include

#
ROOT = 'api'

#
urlpatterns = [
    path(f'{ROOT}/dashboard/', admin.site.urls),
    path(f'{ROOT}/notes/', include('restapi.notes.urls')),
    path(f'{ROOT}/server/', include('restapi.server.urls')),
    path(f'{ROOT}/workbench/', include('restapi.workbench.urls')),
]
