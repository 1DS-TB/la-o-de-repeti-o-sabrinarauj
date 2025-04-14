n = int(input("Digite um número: \n"))

for i in range(1, n + 1):
    for j in range(i):
        print("*",end="")
print()
