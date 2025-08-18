litros = float(input("Quantos Litros: "))
combustivel = input("Gasolina ou Alcool? (G/A): ")
combustivel = combustivel.upper()

if litros <= 20:
    if combustivel == "A":
        total = (litros * 1.9)*0.97
    elif combustivel == "G":
        total = (litros * 2.5)*0.96
    else:
        print("Tipo Invalido!")
else:
    if combustivel == "A":
        total = (litros * 1.9)*0.95
    elif combustivel == "G":
        total = (litros * 2.5)*0.94
    else:
        print("Tipo Invalido!")
print(f'Total a ser pago: R${total:.2f}')