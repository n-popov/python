expression = input()

try:
    a, op, b = expression.split()
    a, b = int(a), int(b)
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '^':
        print(a ** b)
    else:
        print('Bad input')
except:
    print('Bad input')
    exit()
