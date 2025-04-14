inicio = int(input("Digite o início do intervalo: \n"))
fim = int(input("Digite o fim do intervalo: \n"))

print(f"Número de Kaprekar entre {inicio} e {fim}: ")

for num in range(inicio, fim + 1):
    quadrado = str(num ** 2)
    d = len(str(num))
    esquerda = quadrado[:-d] or 0
    direita = quadrado[:-d]

    if esquerda + direita == num:
        print(num)

#Lembrar que o [:-d] no código serve para pegar todos os caracteres da string até os últimos dígitos (d)