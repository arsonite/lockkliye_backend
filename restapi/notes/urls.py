from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import ressource, ressources

urlpatterns = [
    path('', ressources.Notes.as_view()),
    path('<str:pk>/', ressource.Note.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
