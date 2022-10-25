from django.http import HttpResponse
import datetime
from django.shortcuts import render

def saludo(request): # las funciones son vistas

    return HttpResponse("hola mundo") 

def salcf(request):
    
    sf = """<html>
    <body>
    <h1>hola mundo</h1>
    <boby>
    </html>""" # se pueden usar etiquetas html

    return HttpResponse(sf)


class persona(object):
    def __init__(self, nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def salcp(request):

    nombrep="Miguel"
    ape="Gonzalez"

    clasep = persona("Juan", "perez")

    hora=datetime.datetime.now()

    temas_curso = ["Matematicas","Lenguaje","sociales"]
    
    #doc_extermo=open("C:/Users/DELL/Desktop/Miguel/pradjango/proyecto1/proyecto1/plantillas/plantilla1.html")
    #plt=Template(doc_extermo.read())                # plt es pantillas abreviado
    #doc_extermo.close()

    #doc_exterm=loader.get_template('plantilla1.html')

    #ctx=Context({"hora":hora,"nombre_per":nombrep, "apellido":ape, "edad":20, "direc":"San salvador", "clase":clasep.nombre, "clasea":clasep.apellido, "temas":["Matematicas","Lenguaje","sociales"], "temasc":temas_curso})

    #documento=doc_exterm.render({"hora":hora,"nombre_per":nombrep, "apellido":ape, "edad":20, "direc":"San salvador", "clase":clasep.nombre, "clasea":clasep.apellido, "temasc":temas_curso}) 

    #return HttpResponse(documento)

    return render(request, "plantilla1.html" , {"hora":hora,"nombre_per":nombrep, "apellido":ape, "edad":20, "direc":"San salvador", "clase":clasep.nombre, "clasea":clasep.apellido, "temasc":temas_curso})


def fecha(request):
    fechaa =datetime.datetime.now()

    fht = """<html>
    <body>
    <h1>fecha y hora actual %s</h1>
    <boby>
    </html>""" % fechaa

    return HttpResponse(fht)

def edadf (request, edad, agno):
    #edada = 20
    periodo = agno - 2020
    edadff = edad + periodo
    imp = """<html>
    <body>
    <h1>en el ano %s tendra %s agnos</h1>
    <boby>
    </html>""" %(agno, edadff)

    return HttpResponse(imp)
