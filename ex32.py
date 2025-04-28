base=int(input("escreva o numero base qual deseja saber a tabuada:"))
inicio=int(input("escreva o numero qual deseja iniciar a tabuada:"))
fim=int(input("escreva o numero qual deseja terminar a tabuada:"))
def tabuada_personalizada(base,inicio,fim):
    print(f"tabuada do {base} de {inicio} a {fim}:")
    for j in range(inicio, fim + 1):
        print(f"{base} x {j} = {base*j}")
    print()

tabuada_personalizada(base,inicio,fim)