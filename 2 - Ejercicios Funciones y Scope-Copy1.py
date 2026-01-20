#!/usr/bin/env python
# coding: utf-8

# # Completa las celdas vacías implementando la funcionalidad pedida
# 
# <b>Nota</b>: En el caso de las funciones, no solo se debe implementar la función, sino además probarla con distintos usos. Las funciones sin probar no se evaluan.
# 
# <b>Nota 2</b>: Poner una docstring en cada función que explique su funcionalidad, argumentos de entrada, retorno, etc.
# 
# <b>Nota 3</b>: Si el ejercicio da error al ejecutar se puntua a 0. Si solo es un caso especifico por el que da error se bajará la nota en la medida de la importancia de ese fallo
# 
# ## 1) Escribe una función que reciba como argumento un string y lo imprima

# In[23]:


def imprimir_funcion(texto):
  
    print(texto)

#probando la funcion
imprimir_funcion("hola")



# ## 2) Trabajando con listas de entrada
# Escribe una función que implemente la siguiente funcionalidad
# 
# La función recibe un solo argumento, que es una lista de números.
# 
# De esa lista la función imprime aquellos números que sean divisibles por 5 y sean pares.

# In[3]:


def imprime_pares_div_5(lista_numeros):
    for numero in lista_numeros:
        if numero % 2 == 0 and numero % 5 == 0:
            print(numero)

imprime_pares_div_5([10, 15, 20, 33, 40, 37, 100])


# ## 3) Trabajando con el retorno de una función
# 
# Reprogramar la función anterior para que en lugar de imprimir los valores, los devuelva en forma de lista.
# Imprimir los resultados fuera de la función

# In[5]:


def imprime_pares_div_5(lista_numeros):
    resultado = []
    
    for numero in lista_numeros:
        if numero % 2 == 0 and numero % 5 == 0:
            resultado.append(numero)

    return resultado

resultado = imprime_pares_div_5([10, 15, 20, 33, 40, 37, 100])
print(resultado)


# ## 4) Trabajando con múltiples argumentos
# 
# Escribe una función que implemente la siguiente funcionalidad
# 
# - La función recibe 3 argumentos que pueden ser números o strings
# 
# - La función devuelve un string con el valor de los 3 argumentos concatenados uno tras otro con el caracter "_"
# 
# - Al menos una de las pruebas tiene que ser tu nombre, apellido y tu número favorito
# 
# Ejemplo:
# 
# <b>Entrada</b>:
# <ul>
#     <li>1</li>
#     <li>"a"</li>
#     <li>72</li>
# </ul>
# 
# 
# <b>Salida</b>:
# 
# "1_a_72"

# In[7]:


def mis_tres_valores(valor1, valor2, valor3):
    return f"{valor1}_{valor2}_{valor3}"

resultado = mis_tres_valores("Mauro", "Pozzi", 1117)
print(resultado)



# ## 5) Trabajando con argumentos opcionales
# 
# Escribe una función que reciba 4 argumentos:
# 
# <ul>
#     <li> x: Un número </li>
#     <li> y: Otro número </li>
#     <li> op: Un string cuyo valor por <b>defecto</b> sea "add" </li>
#     <li> ret_type: Un string cuyo valor por <b>defecto</b> sea "int" </li>
# </ul>
# 
# Esa función debe aplicar a "x" e "y" la operación que corresponda según el valor de "op".
# <ul>
#     <li> Si op == "add" los suma </li>
#     <li> Si op == "sub" los resta </li>
#     <li> Si op == "mul" los multiplica </li>
#     <li> Si op == "div" los divide </li>
# </ul>
# 
# Y luego debe de retornar en resultado de la operación anterior:
# <ul>
#     <li> Si ret_type == "int" lo retorna en forma de número entero redondeando el resultado </li>
#     <li> Si ret_type == "float" lo retorna en forma de float </li>
#     <li> Si ret_type == "str" retorna un string con el valor del número en él diciendo: "El resultado es: {resultado}"</li>
# </ul>
# 
# Llama a la función al menos de 5 maneras diferentes y en algunos de los casos deja que los valores sean los que fija por defecto en los argumentos opcionales.
# 

# In[3]:


def calcular(x, y, op = "add", ret_type = "int"):
    if op == "add":
        resultado = x + y
    elif op == "sub":
        resultado = x - y
    elif op == "mul":
        resultado = x * y
    elif op == "div":
        resultado = x / y
    else:
        return "operacion no valida"

    if ret_type == "int":
       return round(resultado)
    elif ret_type == "float":
        return float(resultado)
    elif ret_type == "str":
        return f"el resultado es: {resultado}"
    else:
        return "tipo de retorno no valido"

#usa valores por defecto
print(calcular(5, 3))
#operacion resta, retorno entero
print(calcular(10, 4, op = "sub"))
#operacion multiplicar con el retorno float
print(calcular(10, 4, op = "mul", ret_type = "float"))
#division con retorno string
print(calcular(7, 4, op = "div", ret_type = "str"))
#suma con retorno float
print(calcular(11, 56, ret_type = "float"))


# ## 6) Trabajando con número indefinido de argumentos
# 
# Programa, una función que reciba un primer argumento llamado "op" con los valores posibles que definimos en el ejercicio anterior y luego reciba un número indeterminado de argumentos cuyo valor esperado son números
# 
# Esta función debe de aplicar esa operación deseada al resto de argumentos en el orden indicado y devolver el resultado de dicha operación.
# 
# Ejemplo de como tendría que funcionar esta función:
# 
# \>\> apply_op(op="add", 1, 1, 3)
# 
# 5
# 
# Llama a la función al menos de 5 maneras diferentes y en un caso deja que el valor sea el que fija por defecto en los argumentos opcionales.

# In[12]:


def apply_op(op = "add", *args):
    if len(args) == 0:
        return "Debe pasar al menos un numero"

    resultado = args[0]
    for num in args[1: ]:
        if op == "add":
            resultado += num
        elif op == "sub" :
            resultado -= num
        elif op == "mul":
            resultado *= num
        elif op == "div":
            resultado /= num
        else:
            return "Operacion no valida"

    return resultado

print(apply_op("add", 1, 2, 3))#1
print(apply_op("sub", 7, 12, 8))#2
print(apply_op("mul", 2, 3, 4))#3
print(apply_op("div", 50, 5, 2))#4
print(apply_op("add", 5))#5


# ## 7) Documentación de funciones
# 
# Escribe una docstring para cada una de las funciones implementadas hasta el momento.
# <br>Este es un ejemplo de docstring completo:<br>
# """
# 
# Explicación general de la función y temas a tener en cuenta como decisiones de diseño o limitaciones de uso.
# 
# :param parametro_1: explicación, tipo de dato etc..
# 
# :param parametro_2: explicación, tipo de dato etc..
# 
# ...
# 
# :return:
# 
#  Que devuelve, tipo de dato, posibles excepciones(si no lo has mencionado arriba) .Si no devuelve nada en sí pero genera un archivo, modifica una base de datos especificalo aquí
# 
# """

# In[6]:


def imprimir_funcion(texto):
    """
    Definir la funcion e imprimir el 
    string que se da como argumento

    parametro:
    texto (str) el texto que se pide imprimir.

    retorno:
    None
    """
    print(texto)

#probando la funcion
esta_funcion("Hola")



# In[5]:


def imprime_pares_div_5(lista_numeros):
    """ 
    Filtrar una lista de numeros y devuelve aquellos que sean
    pares y divisubles por 5.

    :param lista_numeros: lista de numeros enteros.
    :type lista_numeros[int]

    :return: lista de numeros que cumple ambas condiciones.
    :rtype: list[int]
    """
    resultado = []
    
    for numero in lista_numeros:
        if numero % 2 == 0 and numero % 5 == 0:
            resultado.append(numero)

    return resultado

resultado = imprime_pares_div_5([10, 15, 20, 33, 40, 37, 100])
print(resultado)


# In[24]:


def mis_tres_valores(valor1, valor2, valor3):
    """
    concatena tres valores en un unico string separados por guiones bajos.

    las valores pueden ser numeros o strings y se convierten
    a string internamente.

    :param a: primer valor
    :param b: segundo valor.
    :param c: tercer valor.

    :return: string con los valores cocatenados.
    :rtype: str
    """
    return f"{valor1}_{valor2}_{valor3}"

resultado = mis_tres_valores("Mauro", "Pozzi", 1117)
print(resultado)


# In[3]:


def calcular(x, y, op = "add", ret_type = "int"):
    """
    Aplica una operacion matematica entre dos numeros
    y devuelve el resultado segun el tipo

    :param x: Primer numero.
    :type x: int float
    :param y: segundo numero.
    :type y: int or float
    :param op: operacion a realizar ("add", "sub", "mul", "div").
    :type op: str
    :param ret_type: tipo de retorno ("int", "float", "str").
    :type ret_type: str

    :return: resultado de la operacion.
    :rtype: int, float o str
    """
    if op == "add":
        resultado = x + y
    elif op == "sub":
        resultado = x - y
    elif op == "mul":
        resultado = x * y
    elif op == "div":
        resultado = x / y
    else:
        return "operacion no valida"

    if ret_type == "int":
       return round(resultado)
    elif ret_type == "float":
        return float(resultado)
    elif ret_type == "str":
        return f"el resultado es: {resultado}"
    else:
        return "tipo de retorno no valido"

#usa valores por defecto
print(calcular(5, 3))
#operacion resta, retorno entero
print(calcular(10, 4, op = "sub"))
#operacion multiplicar con el retorno float
print(calcular(10, 4, op = "mul", ret_type = "float"))
#division con retorno string
print(calcular(7, 4, op = "div", ret_type = "str"))
#suma con retorno float
print(calcular(11, 56, ret_type = "float"))


# In[12]:


def apply_op(op = "add", *args):
    """
    Aplica una operacion matematica a un numero idefinido de argumentos.

    La operacion se aplica en el orden que se reciben los numeros.
    :param op: operacion a aplicar ("add", "sub", "mul", "div")
    :type op: str
    :param args: numeros sobre los que se aplica la oepracion.
    :type args: tuple[int | float]

    :return: resultado de la operacion.
    :rtype: int or float
    
    """
    if len(args) == 0:
        return "Debe pasar al menos un numero"

    resultado = args[0]
    for num in args[1: ]:
        if op == "add":
            resultado += num
        elif op == "sub" :
            resultado -= num
        elif op == "mul":
            resultado *= num
        elif op == "div":
            resultado /= num
        else:
            return "Operacion no valida"

    return resultado

print(apply_op("add", 1, 2, 3))#1
print(apply_op("sub", 7, 12, 8))#2
print(apply_op("mul", 2, 3, 4))#3
print(apply_op("div", 50, 5, 2))#4
print(apply_op("add", 5))#5


# ## 8) Paso por referencia vs paso por valor
# - Crea una función que reciba una lista de cadenas de texto y construya un nuevo string formado por el primer carácter de cada cadena de la lista.
# 
# Ejemplo de construcción de la cadena:
# 
# ["Paella", "yale", "tocado", "humano", "osado", "nativo"] -> "Python"
# 
# - La función debe devolver una nueva lista que incluya todos los elementos de la lista original, con el nuevo string añadido al final.
# 
# Ejemplo de salida: ["Paella", "yale", "tocado", "humano", "osado", "nativo", "Python"]
# 
# - Importante: Asegúrate de que la función no modifique ninguna variable fuera de su propio ámbito (es decir, evita efectos secundarios o colaterales).
# 
# 
# - Prueba tu función con al menos dos listas de cadenas diferentes al ejemplo proporcionado.

# In[2]:


def realizar_string(conjunto_palabras):
    nueva_lista = conjunto_palabras.copy()
    resultado = ""
    for palabra in conjunto_palabras:
        resultado += palabra[0]

    nueva_lista.append(resultado)

    return nueva_lista

lista1 = ["paella", "yale", "tocado", "humano", "osado", "nativo"]
lista2 = ["hola", "mundo", "Python"]

print(realizar_string(lista1))
print(realizar_string(lista2))

print(lista1)


# #### 2ª Parte - usa la función
# Crea una función que reciba una lista de cadenas de texto y un diccionario. La función debe realizar las siguientes acciones:
# 
# - Generar un "string secreto" tomando la primera letra de cada palabra en la lista proporcionada y concatenándolas en un nuevo string. ( ¿Te suena? Tienes que usar la función que has construido antes)
# 
# - Modificar cada cadena en la lista reemplazando todas las ocurrencias de las claves del diccionario por sus valores correspondientes. Esto significa que, para cada cadena en la lista, debes buscar las subcadenas que coincidan con las claves del diccionario y sustituirlas por el valor asociado a esa clave.
# 
# - Devolver la lista modificada
# 
# Ejemplo:<br>
# lista_strings = ["Toledo", "horcasitas", "orco", "radon"]<br>
# diccionario_cambios = {"do": "ro", "rc": "s"}<br><br>
# La salida sería:<br>
# ["Tolero", "hosasitas", "oso", "raron", "Thor"]<br>
# Si te fijas lo que se ha hecho con el diccionario de cambios ha sido sustituir cada ocurrencia de "do" por ejemplo por un "ro" en cualquier valor de la lista, por eso tienes Tolero en vez de Toledo.
# 

# In[9]:


def lista_texto(lista_strings, diccionario_cambios):
    #generamos la palabra secreta
    palabra_secreta = "" ""
    for palabra in lista_strings:
        palabra_secreta += palabra[0]

    lista_modificada = []
    #modificamos sin cambiar original
    for palabra in lista_strings:
        palabra_nueva = palabra
        for clave, valor in diccionario_cambio.items():
            palabra_nueva = palabra_nueva.replace(clave, valor)
        lista_modificada.append(palabra_nueva)                

    return lista_modificada, palabra_secreta


lista_strings = ["toledo", "horcasitas", "orco", "radon"]
diccionario_cambio = {"do": "ro", "rc": "s"}
resultado, secreto = lista_texto(lista_strings, diccionario_cambio)

print(resultado)
print("palabra secreta:", secreto)


# #### 3ª Parte - ¿Por qué no modificamos el valor de entrada?
# Vuelve a llamar a la función del ejercicio anterior, pero ahora la lista resultante debe indicar qué cadenas han sido modificadas (es decir, cuáles elementos de la lista original no están en la nueva lista).
# 
# Imprime ambas listas mostrando el valor original y el valor modificado. Además, muestra la palabra secreta por separado.
# 
# Siguiendo el ejemplo anterior, el resultado sería:<br>
# Valor Original | Valor modificado<br>
# Toledo | Tolero<br>
# horcasitas| hosasitas<br>
# orco | oso<br>
# radon | raron<br><br>
# 
# Palabra secreta:<br>
# Thor<br><br>
# 
# Observación: Si la función modificara la lista original, no podrías realizar esta verificación ni continuar utilizando la lista en el resto del programa. Suele ser más limpio desde un punto de diseño que las funciones no modifiquen ninguna variable de entrada para evitar efectos colaterales. No siempre es más óptimo no modificar las variables de entrada por lo que en esos casos siempre se debería de documentar que se va a modificar.

# In[1]:


def lista_texto(lista_strings, diccionario_cambios):
    #generamos la palabra secreta
    palabra_secreta = "" ""
    for palabra in lista_strings:
        palabra_secreta += palabra[0]

    lista_modificada = []
    #modificamos sin cambiar original
    for palabra in lista_strings:
        palabra_nueva = palabra
        for clave, valor in diccionario_cambio.items():
            palabra_nueva = palabra_nueva.replace(clave, valor)
        lista_modificada.append(palabra_nueva)                

    return lista_modificada, palabra_secreta


lista_strings = ["toledo", "horcasitas", "orco", "radon"]
diccionario_cambio = {"do": "ro", "rc": "s"}
resultado, secreto = lista_texto(lista_strings, diccionario_cambio)

print(resultado)
print("palabra secreta:", secreto)


# In[3]:


lista_original = ["toledo", "horcasitas", "orco", "randon"]

lista_modificada, palabra_secreta = procesar_lista(lista_original, diccionario_cambio)


# In[13]:


def mostrar_cambio(lista_original, lista_modificada):
    print("valor original | valor modificado")
    for original, modificada in zip(lista_original, lista_modificada):
        if original != modificada:
            print(f"{original} | {modificada}")

print("\npalabra secreta:")
print(palabra_secreta)



# ## 9) Programación funcional y List comprehension
# 1. Mediante la operación map y una función lambda programa un código que coja una lista de strings y genere una lista igual pero con el caracter exclamación añadido al final.
# 
# Ej:
# 
# ["hello", "Susan", "hi", "sugar"] -> ["hello!", "Susan!", "hi!", "sugar!"]

# In[15]:


lista = ["boca","juniors","mauro","goku"]

lista_exclamacion = list(map(lambda x: x + "!1", lista))

print(lista_exclamacion)


# 
# 2. Haz otro código que haga esto mismo pero usando una "list comprehension" (la sintaxis especial que en una sola línea y mediante corchetes crea una lista basada en una lista ya existente)

# In[16]:


lista_exclamacion_listcomprehension = [x + "!" for x in lista]
print(lista_exclamacion_listcomprehension)


# ## 10) Encapsula el código
# A continuación, tienes un código que realiza varias operaciones sobre una lista de números. Sin embargo, todo el código está escrito en un solo bloque sin usar funciones.
# 
# Tu tarea es la siguiente:
# 
# - Refactoriza el código existente creando una función para cada funcionalidad específica.
# - Cada función debe realizar una tarea única y devolver el resultado necesario.
# - Actualiza el programa principal para que utilice estas funciones y muestre los resultados finales.
# 
# Bonus: Encapsula todo en una única función cuyo único proposito sea recibir la lista de números y llamar a todas las funciones que has generado pasando los valores necesarios y recogiendo los resultados de cada una.

# In[ ]:


numeros = [15, 22, 8, 19, 31]

suma = 0
maximo = numeros[0]
minimo = numeros[0]
cuadrados = []

print("Procesando la suma ...")
for numero in numeros:
    suma += numero

print("Procesando mínimo ...")
for numero in numeros:
    if numero < minimo:
        minimo = numero

print("Procesando máximo ...")
for numero in numeros:
    if numero > maximo:
        maximo = numero

print("Procesando cuadrados ...")
for numero in numeros:
    cuadrados.append(numero ** 2)

print("Calculando promedio ...")
promedio = suma / len(numeros)

print("\nInforme final:")
print(f"Suma total: {suma}")
print(f"Promedio: {promedio}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Cuadrados: {cuadrados}")


# In[8]:


numeros = [15, 22, 8, 19, 31]

def calcular_suma(numeros):
    return sum(numeros)

def calcular_minimo(numeros):
    return min(numeros)

def calcular_maximo(numeros):
    return max(numeros)

def calcular_cuadrados(numeros):
    return [n ** 2 for n in numeros]

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

print("Procesando datos...\n")

suma = calcular_suma(numeros)
minimo = calcular_minimo(numeros)
maximo = calcular_maximo(numeros)
cuadrados = calcular_cuadrados(numeros)
promedio = calcular_promedio(numeros)

print("informe final:")
print(f"suma total: {suma}")
print(f"promedio: {suma}")
print(f"maximo: {maximo}")
print(f"minimo: {minimo}")
print(f"cuadrados: {cuadrados}")


# In[ ]:




