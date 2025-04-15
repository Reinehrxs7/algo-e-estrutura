palindromos=[]
palavras=[]
for i in range (1,6):
    palavra=input("insira palavra")
    palavras.append(palavra)
palavrareversa=""
for  palavra in palavras:
    palavrareversa=palavra[::-1]
    if palavra==palavrareversa:
        palindromos.append(palavra)    
print (palindromos)