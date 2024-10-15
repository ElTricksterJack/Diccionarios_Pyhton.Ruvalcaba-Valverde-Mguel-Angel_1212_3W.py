from os import system
print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("----------------Python Dictionaries-----------------")
di = {
  "Pokemon": "Mimikiu",
  "Juego": "Deltarune",
  "Año": 1964
}
print(di)
print(di["Pokemon"])
print("---------------------")
print("Que es: Un dicionario:Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.")
print("Mis palabras: En otras palabras hases valores que guardan o deniminal otros valores, es como una volsa llamada canicas, y hay guardas canicas.")
print("---------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#Los diccionarios no pueden tener dos elementos con la misma clave, sino no salen.
print(len(di))#con esto puedes ver cuantas claves tiene un dicionario.
print(len(thisdict))#pero no contara valores con a misma clave.
frisk = {
  "Alma": "Determinasion",
  "Monstruo": False,
  "Fecha de estreno": 2352013,
  "Colores": ["red", "purple", "blue","yellow"]
}
print(frisk)#esto es una forma de alladir elementos.
print(type(frisk))
#----------- Otra forma de haser dicionarios
jojop7 = dict(Name = "johnny joestar", Age = 19, Nacionalidad = "Estadounidense")
print(jojop7) 
ok = input("Continuar?:") 
system("cls")
print("-----------Access Dictionary Items-----------")
FukkoIzumo = {
  "Negator": "Unluck",
  "Genero": "Femenino",
  "Edad": 20
}
x = FukkoIzumo["Negator"]
print(x)
#Como adseder a un elemento de una lista
Andy =	{
  "Negator": "Undead",
  "Genero": "Masculino",
  "Edad": "Desconosida"
}
x = Andy.get("Negator")
print(x)
#Obtener claves o Keys
NicoVorgeil = {
  "Negator": "Unforgettable",
  "Genero": "Masculino",
  "Edad": 38
}
x = NicoVorgeil.keys()
print(x)
#Con esto solo se ven las claves o la palabra si su descrision
kurohige = {
  "AkumaNoMi 1": "Yami Yami No Mi",
  "Genero": "Masculino",
  "Edad": 40
}
x = kurohige.keys()
print(x) 
kurohige["AkumaNoMi 2"] = "Gura Gura No Mi"
print(x) 
#
x = kurohige.values()
print(x)
#este es el opuesto de el keys, en resumen se be la descrision de cada palabra
x = kurohige.items()
print(x)
#con esto se ben los valores capturados tanto descrision como palabra pero no se ben unidos sino separados por una ,
if "AkumaNoMi 2" in kurohige:
  print("si kurohige tiene 2 frutas")
ok = input("Continuar?:") 
system("cls")
print("-----------Cambiar elementos del diccionario-----------")
#Cambiar valores, valorados
e = {
  "dia": 31,
  "mes": 10,
  "año": 2008
}
print(e)
e["año"] = 2020
print(e)
e.update({"año": 2024})
print(e)
print("-----------Agregar elementos del diccionario-----------")
Greem = {#Esto es un OC
  "Poder": "none",
  "Objeto Maldito": "Tetera Chashe",
  "Genero:": "Masculino",
  "Edad": 33
}
print(Greem)
Greem ["Poder"] ="Arte del Te"
print(Greem)
Greem.update({"Edad": 58})
print(Greem)
ok = input("Continuar?:") 
system("cls")
print("-----------Eliminar elementos del diccionario-----------")
Trusi = {
  "Poder": "Coral vampiro rojo",
  "Objeto Maldito": "Astilla roja",
  "Genero:": "Femenino",
  "Edad": 30
}
print(Trusi)
Trusi.pop("Objeto Maldito")
print(Trusi)
#con esto eliminas elementos elementos enteros
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#igual pero solo claves
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#esta es otra forma de borrar elementos
#usando del "nombre de lista"
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#con esto basias listas

ok = input("Continuar?:") 
system("cls")
print("-----------Diccionarios de bucles-----------")
Krikevl =	{
  "Poder": "Berserker despellejado de hielo",
  "Objeto Maldito": "Acha roja parte cielos",
  "Genero": "Masculino",
  "Edad": 36
}
for x in Krikevl:
  print(x)
#con esto puedes ver las palabras pero no la descrison, de forma progreiba
print("-)-----(-")
for x in Krikevl:
  print(Krikevl[x])
print("-)-----(-")
for x in Krikevl.values():
  print(x)
print("-)-----(-")
for x in Krikevl.keys():
  print(x)
print("-)-----(-")
for x, y in thisdict.items():
  print(x, y)
#otras ideas
ok = input("Continuar?:") 
system("cls")
print("-----------Copiar diccionarios-----------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#ideas para copiar listas
ok = input("Continuar?:") 
system("cls")
print("-----------Nested Dictionaries-----------")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])
#se podria desir que aqui son una lista de dicionarios
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
