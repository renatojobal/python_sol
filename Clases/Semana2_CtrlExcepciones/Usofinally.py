# ahora hasta que ingrese un número válido
while True:
    try:
        x = int(input('Ingrese un número: '))
        break
    except ValueError:
        print('Eso no es un número')
    except (KeyboardInterrupt, EOFError):
        print('Entrada no recibida')
    finally:
        print('Intento de entrada')