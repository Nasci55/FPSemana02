x = input()
y = input()
conjx = set(x)
conjy = set(y)
z = conjx.intersection(conjy)
z = list(z)
s = "".join(z)
print(s)
