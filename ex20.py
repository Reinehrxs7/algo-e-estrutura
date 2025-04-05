ing=40
idade=(int(input("escreva sua idade")))
membro=(str(input("escreva se é membro: (sim ou não)")))
acomp=(str(input("escreva se está acompanhado com algum membro?: (sim ou não)")))
if idade < 18:
    print("entrada não permitida")
elif idade >= 18 and membro == "sim":
    print("entrada liberada")
elif idade >= 18 and membro == "não" and acomp == "não":
    print(f"você deve pagar R$: {ing}.")
    print("acesso liberado")
elif idade >= 18 and membro == "não" and acomp == "sim":
    ing = ing/2
    print(f"voce de pagar R$: {ing}.")
    print("acesso liberado")