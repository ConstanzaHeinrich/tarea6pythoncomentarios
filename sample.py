def ingresar_puntos_y_comentarios():
    while True:
        print('Ingrese una evaluación del 1 al 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point < 1 or point > 5:  # Condición para verificar si es menor a 1 o mayor a 5
                print('Ingrese un valor del 1 al 5')
            else:
                print('Ingrese su comentario')
                comment = input()
                post = f'Puntos: {point} Comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post} \n')
                break
        else:
            print('Ingrese el punto de evaluación como un número')

def ingresar_otros_puntos():
    while True:
        print('Ingrese una evaluación del 1 al 3')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point < 1 or point > 3:  # Condición para verificar si es menor a 1 o mayor a 3
                print('Ingrese un valor del 1 al 3')
            else:
               
                break
        else:
            print('Ingrese el punto de evaluación como un número')

def comprobar_resultados():
    print('Resultados hasta ahora')
    try:
        with open("data.txt", "r") as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print("No hay resultados aún.")

def mostrar_menu():
    print('Seleccione el proceso que desea realizar')
    print('1: Ingresar puntos de evaluación y comentarios')
    print('2: Ingresar otros puntos de evaluación')
    print('3: Verificar los resultados hasta ahora')
    print('4: Salir')

def procesar_seleccion(num):
    if num == 1:
        ingresar_puntos_y_comentarios()
    elif num == 2:
        ingresar_otros_puntos()
    elif num == 3:
        comprobar_resultados()
    elif num == 4:
        print('Saliendo')
        return True  # Señal para salir del bucle
    else:
        print('Ingrese un valor de 1 a 4')

def main():
    while True:
        mostrar_menu()
        try:
            seleccion = int(input())
            if procesar_seleccion(seleccion):
                break
        except ValueError:
            print('Ingrese un valor numérico')

if __name__ == "__main__":
    main()
