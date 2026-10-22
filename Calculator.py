def calculate(a, b, op):
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    if op not in ops:
        raise ValueError("The Option is not supported")
    return ops[op](a, b)

while True:
    try:
        a = float(input("Number one: "))
        op = input(" Option(+ - * /): ")
        b = float(input("Number two : "))
        print("Result:", calculate(a, b, op))
    except ZeroDivisionError:
        print("You Cannot division by 0")
    except ValueError as e:
        print("Error:", e)
    if input("Continue (y/n): ") != "y":
        break