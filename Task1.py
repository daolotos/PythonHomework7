
n = int(input("N = "))
a1 = int(input("A1 = "))
d = int(input("D = "))

array = [a1]
for i in range(n):
    array.append(array[i] + (i + 1) * d)

print(array)
