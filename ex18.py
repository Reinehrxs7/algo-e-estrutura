base=(float(input("escreva seu salario")))
hora=(float(input("escreva quantas horas extras você fez")))
extra=(float(input("escreva quanto você ganha por hora extra")))
ajuste=(hora*extra)
salario=(ajuste+base)
print(f"seu salario com ajuste das horas extras é de R$:{salario}")
