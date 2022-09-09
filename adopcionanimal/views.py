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
            return render (request, "adopcionanimal/perros.html", {"mensaje":"Perro Cargado exitosamente!"})
    else:
        form= PerrosFormulario()
        return render(request, "adopcionanimal/perrosformulario.html", {"formulario":form})


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
            return render (request, "adopcionanimal/gatos.html", {"mensaje":"Gato Cargado exitosamente!"}) 
    else:
        form= GatosFormulario()
        return render(request, "adopcionanimal/gatosformulario.html", {"formulario":form})


def usuariosformulario(request):

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
            return render (request, "adopcionanimal/usuarios.html", {"mensaje":"Usuario Cargado exitosamente!"})
    else:
        form= UsuariosFormulario()
        return render(request, "adopcionanimal/usuariosformulario.html", {"formulario":form})


#SECCION BUSQUEDA


def perrosbuscar(request):
    return render(request, "adopcionanimal/perrosbuscar.html")

def pbuscar(request):

    if request.GET["raza"]:
        Raza=request.GET["raza"]
        Perro=Perros.objects.filter(Raza=Raza)
        return render(request, "adopcionanimal/perrosresultados.html", {"Perro":Perro})
    else:
        return render(request, "adopcionanimal/perrosbuscar.html", {"mensaje":"No se encuentra Perro"})

def gatosbuscar(request):
    return render(request, "adopcionanimal/gatosbuscar.html")

def gbuscar(request):

    if request.GET["edad"]:
        Edad=request.GET["edad"]
        Gato=Gatos.objects.filter(Edad=Edad)
        return render(request, "adopcionanimal/gatosresultados.html", {"Gato":Gato})
    else:
        return render(request, "adopcionanimal/gatosbuscar.html", {"mensaje":"No se encuentra Gato"})


def usuariosbuscar(request):
    return render(request, "adopcionanimal/usuariosbuscar.html")

def ubuscar(request):

    if request.GET["nombre"]:
        Nombre=request.GET["nombre"]
        Usuario=Usuarios.objects.filter(Nombre=Nombre)
        return render(request, "adopcionanimal/usuariosresultados.html", {"Usuario":Usuario})
    else:
        return render(request, "adopcionanimal/usuariosbuscar.html", {"mensaje":"No se encuentra Usuario"})

#Se probo que todo funcionace bien