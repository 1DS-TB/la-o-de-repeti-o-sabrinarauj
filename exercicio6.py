num = int(input("Digite o número para a sequência de Fibonacci: \n"))
a = 0
b = 0
contador = 0

while contador < num:
    print(a, end=" ")
    proximo_termo = a + b
    a = b
    b = proximo_termo
    contador += 1