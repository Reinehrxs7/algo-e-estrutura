palavras=[""]
for i in range(0,10):
    palavras.append(str(input(f"escreva a {i} palavra")))
contp=0
for i in range(0,10):
    if len(palavras[i]) > 5:
        contp = contp+1
print(f"{contp} palavras tem mais que 5 caracteres")