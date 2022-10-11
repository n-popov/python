D, N = [int(item) if index == 1 else float(item)
        for index, item in enumerate(input().split())]
values = [float(item) for item in input().split()]

counter = 0
is_event = False
events_amount = 0

for value in values:
    if not is_event:
        if abs(value) > D:
            counter += 1
        else:
            counter = 0
        if counter == N:
            is_event = True
            events_amount += 1
            counter = 0
    else:
        if abs(value) <= D:
            counter += 1
        else:
            counter = 0
        if counter == N:
            is_event = False
            counter = 0

print(events_amount)
