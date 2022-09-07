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
    path("gatosformulario/", gatosformulario, name="gatosformulario"),
    path("usuariosformulario/", usuariosformulario, name="usuariosformulario"),
   
    #BUSQUEDA
    path("perrosbuscar/", perrosbuscar, name="perrosbuscar"),

    #RESULTADOS
    path("pbuscar/", pbuscar, name="pbuscar"),
]