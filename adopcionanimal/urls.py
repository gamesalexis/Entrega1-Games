from django.urls import path
from adopcionanimal.views import *

urlpatterns = [
    
    path("", inicio),
    path("perros/", perros, name="perros"),
    path("gatos/", gatos, name="gatos"),
    path("usuarios/", adoptantes, name="usuarios"),
]