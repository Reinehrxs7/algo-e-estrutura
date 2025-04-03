login="adm"
senha=123
login=input("escreval login:")
senha=(int(input("escreva senha: (somente numeros).")))
if login=="adm" and senha==123:
    print("acesso liberado")
elif login!="adm" and senha!=123:
    print("acesso negado")
else:
    print("acesso negado")