from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.Workbenches.as_view()),
    path('<str:pk>/', views.Workbench.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
