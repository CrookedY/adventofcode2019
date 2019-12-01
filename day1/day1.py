f = open('day1.txt')
lines = f.read().split("\n")
f.close()

result = []

def findfuel(fuel):
    a= int(fuel) // 3
    b = a - 2
    return b

for i in lines:
    fuel1 = findfuel(i)
    result.append(fuel1)
    fuel2 = findfuel(fuel1)
    if fuel2 >= 0:
        result.append(fuel2)
    if fuel2 > 8:
        lines.append(fuel2)

print(sum(result))