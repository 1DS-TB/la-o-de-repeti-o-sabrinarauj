n = int(input("Digite a quantidade de números da série harmônica: \n"))
soma = 1
for i in range(1, n + 1):
    soma += 1 / i
print(f"A soma de série harmônica até {n} termos: {soma:.2f}")