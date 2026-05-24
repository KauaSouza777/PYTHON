E = int(input("Dígite a número da escola: "))
S = int(input("Dígite a número da super-mercado: "))
L = int(input("Dígite a número da lojinha: "))

D1 = max(S, E) - min(S, E)
D2 = max(S, L) - min(S, L)
D3 = max(L, E) - min(L, E)

Soma = D1 + D2 + D3
print(Soma)