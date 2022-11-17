from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def print_result(num1, operation, num2, result):
    print(f"{num1} {operation} {num2} = {result}")


def calculator():
    print(logo)
    result = 0

    # if operation == "+":
    #     result = add(first_num, second_num)
    # elif operation == "-":
    #     result = sub(first_num, second_num)
    # elif operation == "*":
    #     result = mult(first_num, second_num)
    # elif operation == "/":
    #     result = div(first_num, second_num)
    # else:
    #     print("Invalid Operation")

    # Simplify logic
    operations = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": div
    }

    first_num = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    continue_with_result = True
    while continue_with_result:

        operation = input("Pick an operation: ").lower()

        second_num = float(input("What's the next number?: "))
        result = operations[operation](first_num, second_num)
        print_result(first_num, operation, second_num, result)

        use_result = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if use_result == "exit":
            return

        if use_result == "y":
            continue_with_result = True
            first_num = result
        elif use_result == "n":
            continue_with_result = False
            calculator()
        else:
            print("Invalid input")


calculator()
