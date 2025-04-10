numeros=[]
for i in range(0,10):
    numeros.append(int(input(f"escreva o {i} numero")))
for i in range(0,10):
    print(f" o {i} numero é : {numeros[i]}")
soma=0
for i in range(0,10):
    soma += numeros[i]
print(f" a soma é = {soma}")