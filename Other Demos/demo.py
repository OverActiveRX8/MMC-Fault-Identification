names = locals()
for i in range(2):
    names['gg' + str(i)] = i
print(gg1)
for n in range(2):
    names['data' + str(n)] = names['gg' + str(1)]
print(data0)
