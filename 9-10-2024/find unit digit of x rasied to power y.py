def digita(x,y):
    total = x ** y
    convert = str(total)

    return int(convert[-1])
x = 100
y = 2
print(digita(x,y))