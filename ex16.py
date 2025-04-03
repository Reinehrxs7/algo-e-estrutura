n1=(int(input("escreva nota 1")))
n2=(int(input("escreva nota 2")))
n3=int(int(input("escreva nota 3")))
med=((n1+n2+n3)/3)
if med>=7:
    print("aprovado")
elif med<7 and med>5:
    print("recuperação")
else:
    print("reprovado")