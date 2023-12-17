MAX_OPTION = 5
MIN_OPTION = 1
ADD_OPTION = '1'
SUB_OPTION = '2'
MUL_OPTION = '3'
DIV_OPTION = '4'
POW_OPTION = '5'


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def power(num1, num2):
    return num1 ** num2


def menu():
    print("-------- CALCULATOR MENU --------")
    print("Enter 1: Addition")
    print("Enter 2: Subtraction")
    print("Enter 3: Multiplication")
    print("Enter 4: Division")
    print("Enter 5: Power")


if __name__ == '__main__':
    menu()
    option = input()
    while option.isalpha() or int(option) > MAX_OPTION or int(option) < MIN_OPTION:
        print("Enter only numbers between 1 and 5")
        option = input()

    print("Enter first number:")
    num1 = input()
    while num1.isalpha():
        print("Enter only numbers")
        num1 = input()

    print("Enter second number:")
    num2 = input()
    while num2.isalpha():
        print("Enter only numbers")
        num2 = input()

    while (option == DIV_OPTION and num2 == '0') or (option == DIV_OPTION and num2 == '-0'):
        print("Cannot divide by 0, Enter second number")
        num2 = input()

    num1 = int(num1)
    num2 = int(num2)

    if option == ADD_OPTION:
        print("Result of", num1, " + ", num2, "is: ", add(num1, num2))

    if option == SUB_OPTION:
        print("Result of", num1, " - ", num2, "is: ", sub(num1, num2))

    if option == MUL_OPTION:
        print("Result of", num1, " * ", num2, "is: ", mul(num1, num2))

    if option == DIV_OPTION:
        print("Result of", num1, " / ", num2, "is: ", div(num1, num2))

    if option == POW_OPTION:
        print("Result of", num1, " ** ", num2, "is: ", power(num1, num2))
