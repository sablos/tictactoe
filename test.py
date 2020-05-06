a = [[10] * 4] * 4

print(a)

for r in a:
    print(r)

print(a[2][1])
print(a[1][1])

a[2][1] = 5

for r in a:
    print(r)

print(a[2][1])
print(a[1][1])