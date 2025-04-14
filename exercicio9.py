print("Números perfeitos de 1 até 1000: \n")

for num in range(1, 1001): 
    soma = 0
    for i in range(1, num): 
        if num % i == 0: 
            soma += i  
            if soma == num:
                print(num)
                
#Para cada número verificar seus divisores 
#1 até num-1
#somar os divisores