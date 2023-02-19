
n = int(input("N = "))
a = []
for i in range(n):
    a.append(int(input(f"A[{i}] = ")))
aMin = int(input("Min = "))
aMax = int(input("Max = "))

for i in range(n):
    if aMin < a[i] < aMax:
        print(f"index = {i}")

