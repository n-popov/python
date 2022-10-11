text = list(input())
processed = list()
symbols = list('.,!?')
end_symbols = list('.!?')
is_beginning = True
for letter in text:
    if letter == ' ' and processed[-1] == ' ':
        continue
    elif letter in symbols:
        if processed[-1] == ' ':
            processed[-1] = letter
        else:
            processed.append(letter)
        processed.append(' ')
        if letter in end_symbols:
            is_beginning = True
    elif letter.isalpha() and is_beginning:
        processed.append(letter.upper())
        is_beginning = False
    else:
        processed.append(letter)

print(*processed, sep='')




