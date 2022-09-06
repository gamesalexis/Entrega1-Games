from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

# SECCION PERROS


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
            return render (request, "Appcoder/inicio.html", {"mensaje":"Perro Cargado"})
    else:
        form= PerrosFormulario()
    # return render(request, "Appcoder/profeForm.html", {"formulario":form})


def buscarperro(request):
    if request.GET["Tamano"]:
        Tamano=request.GET["Tamano"]
        Perro=Perros.objects.filter(Tamano=Tamano)
        return render(request, "Appcoder/resultadosBusqueda.html", {"Tamano":Perro})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje":"No se encuentra Perro"})
    return HttpResponse(respuesta)



# SECCION GATOS



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
            return render (request, "Appcoder/inicio.html", {"mensaje":"Gato Cargado"})
    else:
        form= PerrosFormulario()
    # return render(request, "Appcoder/profeForm.html", {"formulario":form})


def buscargato(request):
    if request.GET["Edad"]:
        Edad=request.GET["Edad"]
        Gato=Gatos.objects.filter(Edad=Edad)
        return render(request, "Appcoder/resultadosBusqueda.html", {"Gato":Gato})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje":"No se encuentra Gato"})
    return HttpResponse(respuesta)



# SECCION ADOPTANTES



def adoptantesformulario(request):

    if request.method=="POST":
        form= AdoptantesFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Nombre= info["Nombre"]
            Apellido= info["Apellido"]
            Sueldo= info["Sueldo"]
            Edad= info["Edad"]
            Direccion= info["Direccion"]
            Email= info["Email"]
            Adoptante= Adoptantes(Nombre=Nombre, Apellido=Apellido, Sueldo=Sueldo, Edad=Edad, Direccion=Direccion, Email=Email)
            Adoptante.save()
            return render (request, "Appcoder/inicio.html", {"mensaje":"Usuario Cargado"})
    else:
        form= AdoptantesFormulario()
    # return render(request, "Appcoder/profeForm.html", {"formulario":form})


def buscaradoptante(request):
    if request.GET["Apellido"]:
        Apellido=request.GET["Apellido"]
        Adoptante=Adoptantes.objects.filter(Apellido=Apellido)
        return render(request, "Appcoder/resultadosBusqueda.html", {"Adoptante":Adoptante})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje":"No se encuentra Usuario"})
    return HttpResponse(respuesta)







#def busquedaComision(request):
#    return render(request, "Appcoder/busquedaComision.html")