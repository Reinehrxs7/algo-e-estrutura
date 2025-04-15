valores=[]
novovalor=[]
for i in range(1,5):
    valor=int(input("insira valor"))
    valores.append(valor)
adicional=int(input("insira o numero para multiplicar "))
for valor in valores:
    novovalor.append(valor*adicional)
print(f"os valores são {novovalor}")