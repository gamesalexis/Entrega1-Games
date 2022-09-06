from django.shortcuts import render
from adopcionanimal.models import *
from django.http import HttpResponse
from adopcionanimal.forms import *

# INICIO

def inicio(request):
    return render (request, "adopcionanimal/inicio.html")
def perros(request):
    return render (request, "adopcionanimal/perros.html")
def gatos(request):
    return render (request, "adopcionanimal/gatos.html")
def adoptantes(request):
    return render (request, "adopcionanimal/usuarios.html")


# SECCION FORMULARIOS


def perrosformulario(request):

    if request.method=="POST":
        form= PerrosFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Nombre= info["Nombre"]
            Raza= info["Raza"]
            Tamano= info["Tamano"]
            Edad= info["Edad"]
            Perro= Perros(Nombre=Nombre, Raza=Raza, Tamano=Tamano, Edad=Edad)
            Perro.save()
            return render (request, "adopcionanimal/perros.html", {"mensaje":"Perro Cargado"})
    else:
        form= PerrosFormulario()
    return render(request, "adopcionanimal/perrosformulario.html", {"formulario":form})

'''
    def gatosformulario(request):

    if request.method=="POST":
        form= GatosFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Nombre= info["Nombre"]
            Raza= info["Raza"]
            Tamano= info["Tamano"]
            Edad= info["Edad"]
            Gato= Gatos(Nombre=Nombre, Raza=Raza, Tamano=Tamano, Edad=Edad)
            Gato.save()
            return render (request, "adopcionanimal/gatos.html", {"mensaje":"Gato Cargado"})
    else:
        form= GatosFormulario()
    #return render(request, "Appcoder/profeForm.html", {"formulario":form})


def Usuariosformulario(request):

    if request.method=="POST":
        form= UsuariosFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Nombre= info["Nombre"]
            Apellido= info["Apellido"]
            Sueldo= info["Sueldo"]
            Edad= info["Edad"]
            Direccion= info["Direccion"]
            Email= info["Email"]
            Usuario= Usuarios(Nombre=Nombre, Apellido=Apellido, Sueldo=Sueldo, Edad=Edad, Direccion=Direccion, Email=Email)
            Usuario.save()
           #return render (request, "adopcionanimal/usuarios.html", {"mensaje":"Usuario Cargado"})
    else:
        form= UsuariosFormulario()
    # return render(request, "Appcoder/profeForm.html", {"formulario":form})

'''
#SECCION BUSQUEDA

'''
def buscarperro(request):

    if request.GET["Tamano"]:
        Tamano=request.GET["Tamano"]
        Perro=Perros.objects.filter(Tamano=Tamano)
        return render(request, "Appcoder/resultadosBusqueda.html", {"Tamano":Perro})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje":"No se encuentra Perro"})
    return HttpResponse(respuesta)


def buscargato(request):

    if request.GET["Edad"]:
        Edad=request.GET["Edad"]
        Gato=Gatos.objects.filter(Edad=Edad)
        #return render(request, "Appcoder/resultadosBusqueda.html", {"Gato":Gato})
    else:
        #return render(request, "Appcoder/busquedaComision.html", {"mensaje":"No se encuentra Gato"})
        #return HttpResponse(respuesta)

def buscarusuario(request):

    if request.GET["Apellido"]:
        Apellido=request.GET["Apellido"]
        Usuario=Usuarios.objects.filter(Apellido=Apellido)
        #return render(request, "Appcoder/resultadosBusqueda.html", {"Usuario":Usuario})
    else:
       # return render(request, "Appcoder/busquedaComision.html", {"mensaje":"No se encuentra Usuario"})
  #  return HttpResponse(respuesta)

'''
#OTRO CODIGO SIN DEFINIR
#def busquedaComision(request):
#return render(request, "Appcoder/busquedaComision.html")