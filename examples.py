import operations
print("Elige una opción")

options = """
    1.- Factorial de un numero
    2.- Serie Fibonacci
    3.- Convert a any list to a Set
    4.- Oper a String
"""

print(options)

def main():
    option = input()
    if option == '1':
        print('Ingresa un valor')
        number = input()
        print(operations.factorial(number))
    elif option == '2':
        print('Ingresa un numero')
        number = input()
        print(operations.fibonacci(number))
    elif option == '3':
        print('The result is: ')
        print(operations.convert_to_uniques())
    else:
        print('The result is: ')
        print(operations.string_apart())


main()
