#!/usr/bin/env python3

import random
import time

def partition(array, low, high):
 
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1


def quicksort(lista, low, high):
    if low < high:
        pi = partition(lista, low, high)
        quicksort(lista, low, pi - 1)
        quicksort(lista, pi + 1, high)


def burbuja(lista):
    n = len(lista)

    for i in range(n-1):       
        for j in range(n-1-i): 
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def generar_list_asc(tamaño):

    if tamaño == "10":
        lista_asc = [i for i in range(10)]
    elif tamaño == "100":
        lista_asc = [i for i in range(100)]
    elif tamaño == "1000":
        lista_asc = [i for i in range(10000)]
    elif tamaño == "10000":
        lista_asc = [i for i in range(10000)]
    elif tamaño == "100000":
        lista_asc = [i for i in range(100000)]

    return lista_asc 

def generar_list_des(tamaño):

    if tamaño == "10":
        lista = [i for i in range(10)]
        lista.reverse()
    elif tamaño == "100":
        lista = [i for i in range(100)]
        lista.reverse()
    elif tamaño == "1000":
        lista = [i for i in range(10000)]
        lista.reverse()
    elif tamaño == "10000":
        lista = [i for i in range(10000)]
        lista.reverse()
    elif tamaño == "100000":
        lista = [i for i in range(100000)]
        lista.reverse()

    return lista

def generar_list_rand(tamaño):
    if tamaño == "10":
        lista_rand = [random.random() for i in range(10)]
    elif tamaño == "100":
        lista_rand = [random.random() for i in range(100)]
    elif tamaño == "1000":
        lista_rand = [random.random() for i in range(10000)]
    elif tamaño == "10000":
        lista_rand = [random.random() for i in range(10000)]
    elif tamaño == "100000":
        lista_rand = [random.random() for i in range(100000)]

    return lista_rand


if __name__ == '__main__':

    print("[+] Iniciando el programa...\n")
    tamaño = input("Ingresa el tamaño (N=10, 100, 1000, 10000, 100000.): ")
    lista_asc_or = generar_list_asc(tamaño)
    lista_des_or = generar_list_des(tamaño)
    lista_rand_or = generar_list_rand(tamaño)
    size = len(lista_asc_or)
    start_time = time.time()
    quicksort(lista_asc_or,0, size-1)
    end_time = time.time()
    time_sort = end_time - start_time
    print(f"[+] Arreglo quicksort ascendente:\n {lista_asc_or}")
    print(f"[!] El tiempo de ejecución quicksort fue de: {time_sort}, segundos\n")
    start_time = time.time()
    burbuja(lista_asc_or)
    end_time = time.time()
    time_bur = end_time - start_time
    print(f"[+] Arreglo burbuja ascendente:\n {lista_asc_or}")
    print(f"[!] El tiempo de ejecución de burbuja fue de: {time_bur}, segundos")



