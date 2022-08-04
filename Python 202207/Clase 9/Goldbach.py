#!/usr/bin/env python
# coding: utf-8

# ## Conjetura de Goldbach
# 
# 1. Escribir una función para generar una lista de números primos menores o iguales a n
# 2. Escribir una función para guardar una lista en un archivo
# 3. Escribir una función que lea el archivo genrado por la función anterior
# 4. Escribir una función que verifique si se cumple la conjetura de Goldbach para un número ingresado, para ello deberpa reotrna las lista de números primos que cumpla con el enunciado
# 5. Escribir un programa que permita ingresar un número y permita presentar en pantalla la conjetura de goldbach para todos los números menores o iguales al ingresado

# In[2]:


def list_primos(n):
    lista = []
    if n >= 2:
        for i in range(2, n+1):
            primo = True
            for j in lista:
                if i % j == 0:
                    primo = False
                    break
            if primo:
                lista.append(i)
    return lista


# In[3]:


def guardar(lista, nombre):
    if not nombre.endswith('.txt'):
        nombre = nombre + '.txt'
    archivo = open(nombre, 'w')
    for i in lista:
        archivo.write(str(i) + '\n')
    archivo.close()


# In[14]:


def leer_lista(nombre):
    try:
        archivo = open(nombre, 'r')
        lista = []
        for i in archivo:
            aux = i.replace('\n', '')
            lista.append(int(aux))
        return lista
    except FileNotFoundError:
        print('No existe el archivo')
        return []


# In[30]:


def goldbach_fuerte(lista, n):
    for i in lista:
        if i > n:
            continue
        for j in lista:
            if j > n:
                continue
            if i + j == n:
                return [i, j]
    return []
def goldbach_debil(lista, n):
    for i in lista:
        if i > n:
            continue
        for j in lista:
            if j > n:
                continue
            for k in lista:
                if k > n:
                    continue
                if i + j + k == n:
                    return [i, j, k]
    return []

def Goldbach(lista, n):
    if n % 2 == 0 and n > 2:
        return goldbach_fuerte(lista, n)
    elif n % 2 == 1 and n > 5:
        return goldbach_debil(lista, n)
    raise ValueError('El número no cumple las condiciones.')

