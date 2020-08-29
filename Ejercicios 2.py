from calendar import isleap


def ejercicio1():
    tuplaEdades = (45, 20, 23, 50, 78, 40, 21, 56, 81, 15, 20, 21, 22, 25, 27)
    print("Edades Mayores de 40 en la tupla:")
    for edad in tuplaEdades:
        if edad > 40:
            print(edad)


def ejercicio2_3():
    listaNombres = []
    for i in range(0, 10):
        print('Ingrese el nombre '+str(i+1))
        listaNombres.append(input())

    print('-----------------')
    print(listaNombres[2])


def ejercicio4():
    year = int(input("Introduzca un año para comprobar si es bisiesto :"))
    if isleap(year) == True:
        print('El año '+str(year) + " ES un año bisiesto ")
    else:
        print('El año '+str(year) + " NO es un año bisiesto ")


def ejercicio5():
    listaNumeros = []
    pares = ""
    impares = ""
    for i in range(0, 10):
        print('Ingrese el numero '+str(i+1))
        listaNumeros.append(int(input()))

    for num in listaNumeros:
        if num % 2 == 0:
            pares += str(num)+" "
        else:
            impares += str(num)+" "
    print('Pares : '+pares)
    print('Impares : '+impares)


def Seleccionar():
    print('---------------------------------------------------------------------------------------')
    print('# 1. Hacer una tupla con 15 edades de personas e imprimir las personas mayores de 40.')
    print('# 2. Pedir 10 nombres, almacenarlos en una lista/ # 3. Buscar en la lista uno de los nombres almacenados.')
    print('# 4.Pedir que digite un año y que el sistema diga si es bisiesto o no.')
    print('# 5. Pedir 10 numeros y almaecnarlos en una lista e imprimir en una linea cuales son pares y en otra cuales son impares')
    print('---------------------------------------------------------------------------------------')
    print()

    switcher = {
        '1': ejercicio1, 
        '2': ejercicio2_3,
        '4': ejercicio4, 
        '5': ejercicio5,
        '6': exit
        }
    option=input('Selccione el ejercicio a ejecutar:')
    switcher.get(option)()
    Seleccionar()



Seleccionar()