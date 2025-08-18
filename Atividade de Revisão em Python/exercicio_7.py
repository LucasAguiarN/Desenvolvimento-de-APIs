qtde = 0
lista = []
lista_invertida = []
soma = 0
qtde_maior_media = 0

while True:
    numero = int(input("Informe um numero: "))
    if numero == -1:
        break
    qtde += 1
    lista.append(numero)

lista_invertida = lista[::-1]

for n in lista:
    soma += n
if qtde > 0:
    media = soma / qtde
else:
    media = 0

for n in lista:
    if n > media:
        qtde_maior_media += 1

print(f'Quantidade de Numeros Digitados: {qtde}')
print(lista)
print(lista_invertida)
print(f'Soma da Lista: {soma}')
print(f'Media da Lista: {media}')
print(f'Quantidade de Numeros Maior que Media: {qtde_maior_media}')