salario_inicial = float(input("Digite o salario inicial do funcionario: R$"))
salario = salario_inicial * 1.015
aumento = 0.015
for i in range(1997, 2025+1):
    salario = salario * (1 + aumento)
    aumento = aumento * 2
print(f'Salario em 2025: R${salario:.2f}')