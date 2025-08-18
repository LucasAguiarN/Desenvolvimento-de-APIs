n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if 9.0 <= media <= 10.0:
    status = "A"
elif 7.5 <= media < 9.0:
    status = "B"
elif 6.0 <= media < 7.5:
    status = "C"
elif 4.0 <= media < 6.0:
    status = "D"
else:
    status = "E"

if status in ["A", "B", "C"]:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print("===== SEUS RESULTADOS =====")
print(f"Nota 1: {n1}")
print(f"Nota 2: {n2}")
print(f"Média: {media:.2f}")
print(f"Conceito: {status}")
print(f"Situação: {situacao}")