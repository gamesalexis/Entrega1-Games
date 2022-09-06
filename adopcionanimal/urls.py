from django.urls import path
from adopcionanimal.views import *

urlpatterns = [
    
    #INICIO
    path("", inicio, name="inicio"),
    path("perros/", perros, name="perros"),
    path("gatos/", gatos, name="gatos"),
    path("usuarios/", adoptantes, name="usuarios"),
    #FORMULARIOS
    path("perrosformulario/", perrosformulario, name="perrosformulario"),
    #BUSQUEDA

]