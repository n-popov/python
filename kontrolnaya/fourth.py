N = int(input())
temperature_array = list()
pressure_array = list()
for _ in range(N):
    temperature, pressure = tuple([float(value) for value in input().split()])
    temperature_array.append(temperature)
    if -70 <= temperature <= 80:
        pressure_array.append(pressure)

print(f'{sum(temperature_array) / len(temperature_array) :.4f} {sum(pressure_array) / len(pressure_array) :.4f}')
