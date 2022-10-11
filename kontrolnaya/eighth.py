N = int(input())
data = list()
for _ in range(N):
    values = tuple([int(value) if index % 2 == 0 else value
               for index, value in enumerate(input().split())])
    data.append(values)

data.sort(key=lambda item: (item[0], item[1]))

last_values = dict()

for timestamp, sensor, value in data:
    if sensor in last_values and value == last_values[sensor]:
        continue
    last_values[sensor] = value
    print(timestamp, sensor, value)
