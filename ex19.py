idade=(int(input("digite sua idade:")))
sexo=(str(input("digite seu sexo: (masculino ou feminino)")))
atleta=(str(input("você é atleta?: (sim ou não)")))
if idade < 15:
    print("artigos infantís")
elif idade < 21 and idade > 15 and sexo == "feminino":
    print("maquiagens e moda")
elif idade < 32 and idade > 15 and sexo == "masculino" and atleta == "sim":
    print("artigos esportivos")
elif idade < 21 and idade > 15 and sexo == "masculino" and atleta == "não":
    print("videogames")
elif idade < 32 and idade > 21 and sexo == "masculino" and atleta == "não":
    print("livros, jardinagem e eletrodomesticos")
elif idade < 35 and idade > 22 and sexo == "feminino":
    print("artigos esportivos e itens de casa")