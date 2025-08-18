def saque (valor):
    notas = [100, 50, 10, 5, 1]
    resultado = {}

    restante = valor

    for nota in notas:
        qtd_notas = restante // nota
        if qtd_notas > 0:
            resultado[nota] = qtd_notas
            restante %= nota

    print(f"Notas fornecidas para R$ {valor}:")
    for nota in notas:
        if nota in resultado:
            print(f"{resultado[nota]} nota(s) de R$ {nota}")    

valor = int(input("Digite o valor do saque (entre 10 e 600 reais): "))
if valor < 10 or valor > 600:
    print("Valor inválido. O saque deve ser entre 10 e 600 reais.")
else:
    saque(valor)