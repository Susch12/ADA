#!/usr/bin/env python3

import random
import time

def quicksort(array):

    if (len(array) <= 1):
        return array

    pivot = array[len(array) // 2]

    lt = [i for i in array if i < pivot]
    eq = [pivot] * array.count(pivot)
    gt = [i for i in array if i > pivot]

    return quicksort(lt) + eq + quicksort(gt)

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
        lista_asc = [i for i in range(1000)]
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
        lista = [i for i in range(1000)]
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
    start_time = time.time()
    quicksort(lista_asc_or)
    end_time = time.time()
    time_sort = end_time - start_time
   # print(f"[+] Arreglo quicksort ascendente:\n {lista_asc_or}")
    print(f"[!] El tiempo de ejecución de quicksort con una lista ascendente con tamaño de {tamaño} fue de: {time_sort}, segundos\n")
    start_time = time.time()
    burbuja(lista_asc_or)
    end_time = time.time()
    time_bur = end_time - start_time
   # print(f"[+] Arreglo burbuja ascendente:\n {lista_asc_or}")
    print(f"[!] El tiempo de ejecución de burbuja con una lista ascendente con tamaño de {tamaño} fue de: {time_bur}, segundos\n")
    size = len(lista_des_or)
    start_time = time.time()
    quicksort(lista_des_or)
    end_time = time.time()
    time_sort = end_time - start_time
    print(f"[!] El tiempo de ejecución de quicksort con una lista descendente con tamaño de {tamaño} fue de: {time_sort}, segundos \n")
    start_time = time.time()
    burbuja(lista_des_or)
    end_time = time.time()
    time_bur = end_time - start_time
    print(f"[!] El tiempo de ejecución de burbuja con una lista descendente con tamaño de {tamaño} fue de: {time_bur}, segundos\n")

    size = len(lista_rand_or)
    start_time = time.time()
    quicksort(lista_rand_or)
    end_time = time.time()
    time_sort = end_time - start_time
   # print(f"[+] Arreglo quicksort ascendente:\n {lista_asc_or}")
    print(f"[!] El tiempo de ejecución de quicksort con una lista random con tamaño de {tamaño} fue de: {time_sort}, segundos\n")
    start_time = time.time()
    burbuja(lista_rand_or)
    end_time = time.time()
    time_bur = end_time - start_time
    print(f"[!] El tiempo de ejecución de burbuja con una lista random con tamaño de {tamaño} fue de: {time_bur}, segundos\n")







