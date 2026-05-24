N, M = map(int,input("Quantidade de refeições/ Limite de calorias: ").split())

soma = 0
for i in range(N):
    print("P = proteina/ G = gordura /C = calorias")
    P, G, C = map(int, input("Adicione o P, G e C respectivamente: ").split())
    somaC = (P * 4) + (G * 9) + (C * 4)
    soma += somaC

Calorias = M - soma
print(Calorias)