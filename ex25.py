numeros=[]
for i in range (1,6):
    numero=int(input("insira um numero"))
    numeros.append(numero)
maior=numeros[0]
menor=numeros[1]  
for numero in numeros:
    if numero>maior:
        maior=numero
for numero in numeros:
    if numero<menor:
        menor=numero
print(f"o menor numero é: {menor}")
print(f"o maior numero é: {maior}")