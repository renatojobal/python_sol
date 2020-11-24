26# inicializa la lista vacía para contener la entrada del usuario 
# y el valor de suma en cero
user_list = []
list_sum = 0

# busca la entrada del usuario para 10 números
for i in range(10):
    userInput = input("Enter any 2-digit number: ")
    
# verifica si el número es par y, en caso de ser afirmativo lo agrega a la lista list_sum
# imprime la advertencia de valor incorrecto cuando se produce la excepción ValueError
    try:
        number = int(userInput) # Transformando a int
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Valor incorrecto. ¡Eso no es un int!")
    
print("user_list: {}".format(user_list))
print("La suma de los números pares en user_list es: {}.".format(list_sum))