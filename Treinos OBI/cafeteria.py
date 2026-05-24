A = int(input("Valor mínimo de leite(ml): "))
B = int(input("Valor maximo de leite(ml): "))
C = int(input("Capacidade da xicara: "))
D = int(input("Dose de café(ml): "))
aprovacao = False
X = 1
DF = 0
while(DF <= C):
    DF = D * X
    leite = C - DF
    if (leite >= A and leite <= B):
        aprovacao = True
        print("S")
        break
    else:
        X +=1
if (aprovacao == False):
    print("N")
            
            