vals = [[y * 3 for y in range(x)] for x in range(10)]
print(vals)

# another way
outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)




# ==============================================================================================================================



