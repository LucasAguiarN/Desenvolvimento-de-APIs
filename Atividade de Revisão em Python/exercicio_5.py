def menu():
    print('##############################')
    print('### Cardapio da Lanchonete ###')
    print('##############################')
    print("100 - Cachorro Quente  R$ 1,20")
    print("101 - Bauru Simples    R$ 1,30")
    print("102 - Bauru com ovo    R$ 1,50")
    print("103 - Hambúrguer       R$ 1,20")
    print("104 - Cheeseburguer    R$ 1,30")
    print("105 - Refrigerante     R$ 1,00")

def calcular(cod, qtde, pedido):
    if cod == "100":
        preco = 1.2
        chave = "Cachorro Quente"
    elif cod == "101":
        preco = 1.3
        chave = "Bauru Simples"
    elif cod == "102":
        preco = 1.5
        chave = "Bauru com ovo"
    elif cod == "103":
        preco = 1.2
        chave = "Hambúrguer"
    elif cod == "104":
        preco = 1.3
        chave = "Cheeseburguer"
    else:
        preco = 1
        chave = "Refrigerante"
    if chave not in pedido:
        pedido[chave] = qtde * preco
    else:
        anterior = pedido[chave]
        pedido[chave] = anterior + (qtde * preco)
    return

pedido = dict()
while True:
    menu()
    cod = input("Informe o Código do Item: ")
    qtde = int(input("Informe a Quantidade do Item: "))
    calcular(cod, qtde, pedido)
    encerrar = input("Deseja finalizar o Pedido? (S/N)? ")
    if encerrar.upper() == "S":
        break
total = sum(pedido.values())

for item, valor in pedido.items():
    print(f'{item} R${valor:.2f}')
print(f'Total do Pedido: R${total:.2f}')