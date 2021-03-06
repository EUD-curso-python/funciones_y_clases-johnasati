global1 = 34

def cambiar_global(a):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    pass

    global global1
    global1 = a
    print(global1)

    
print(global1)
cambiar_global(12)
print(global1)

def anio_bisiesto(año):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    
    if año % 400 == 0 or (año % 100 != 0 and año % 4 == 0):
      return True
    else:
      return False
    pass
    
anio_bisiesto(2020)


def contar_valles(*args):
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    #conteo = 0
    #n = 0
    
    #for el in lista:
      #print('n',n)
      #print('el',el)
      #if el == -1 and lista[n-1] > -1:
        #conteo += 1
      #n +- 1
    #return conteo
    #pass
    #contar_valles([-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1])

    conteo = 0
    for i in args:
      for e in args+1:
        if i == 1 and e == -1:
          conteo += 1
        else:
          conteo
      print(conteo)
      
args = [1,-1,1,1,-1,0,0,1,-1,1,1,-1,-1]
pass


def saltando_rocas():
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    pass

def pares_medias(t1):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''

    pares = {}
    for n in t1:
        #print(n)
        i = int(t1.count(n)/2)
        #print(i)
        if i > 0:
            pares[n] = i
    #print(pares)
    return pares

pares_medias([2,3,5,6,6,7,3,2,5,5,5])


    #Val1 = {}
    #no_pares = []
    #print['colores']
    #for el in ti:
      #Val1.setdefault[el,0]
      #print(Val1)
    #print['medias']
    #for el in ti:
      #Val1[el] += 1
      #print(Val1)
    #print['pares']
    #for el2 in Val1:
      #Val1[el2] = Val1[el2]//2
    #print[Val1]
    #for el2 in Val1:
      #if Val1[el2] == 0:
        #no_pares.append[el2]
    #print['no pares']
    #print[no_pares]
    #for el3 in no_pares:
      #del Val1[el3]
    #return Val1
    #pass
  #test = [1,2,3,4,1,3,6,2,3,3,6]
  #print[test]
  #print[pares_medias(test)]


    #pares = {}
    #lista = []
    #for i in args:
        #lista.append(i)
        #pares [1] = int(lista.count(i)/2)
        #if pares [i] == 0:
          #del pares[i]
          
    #print(pares)
    #return pares
  #pares_medias(1,1,2,2,3,3,4,4,5,5,2,1,3,6,3)



# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'




# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#



# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'





# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.



#class Persona1(personas):
  #def __init__(self,nombres,apellidos,fecha_nacimiento):
    #super().__init__(nombres,apellidos)
    #self.fecha_nacimiento = fecha_nacimiento
  
  #def edad(self):
    #delta = datetime.datetime.today[] - self.fecha_nacimiento
    #print(delta)
    #dias = delta / datetime.tinedelta(1)
    #print(dias)
    #salida = int[dias/365)
    #salida = delta.years()
    #print[salida]
    #return salida

#fecha = datetime.datetime.strptime('1991-03-06', '%Y-%m-%d')
#personas = Persona1(['john','alexander','jose'],['sanchez','tirado','amadeo'],fecha)
#print(personas.edad)
  



