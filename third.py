number = input()
dot_position = number.find('.')
if dot_position == -1:
    print(int(number) - 1)
else:
    digits = len(number) - dot_position - 1
    print(f'{float(number) - 10 ** -digits :.{digits}f}')