from random import random

values = [random() for i in range(20)]
x = random()

values.sort()

indices = [index for index, value in enumerate(values) if value >= x]

print("Sorted values:", values)
print("x:", x)

if indices:
    print("First matching index:", indices[0])
else:
    print("No matching index found (all values < x).")