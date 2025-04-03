item=input("escreva qual item comprou:")
quantidade=(int(input("escreva quantas unidades comprou:")))
preco=(int(input("escreva o valor unitario do item:")))
total = quantidade*preco
if total > 100:
    total = total*0.95
    print(f"total: R$:{total}")