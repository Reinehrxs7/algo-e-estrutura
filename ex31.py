numero=int(input("escreva o numero qual deseja saber a tabuada:"))
def tabuada(numero):
    print(f"tabuada do {numero}:")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")
        
tabuada(numero)     