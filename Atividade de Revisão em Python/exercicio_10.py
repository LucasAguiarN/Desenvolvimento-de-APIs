import requests

print("###########################")
print("#######CONSULTA CEP########")
print("###########################")
print()

cep_input = input("Digite o cep para a Consulta: ")

if len(cep_input) != 8:
    print("Quantidade de digitos invalidá")
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

pesquisa = request.json()

if 'erro' not in pesquisa:
    print('==> CEP ENCONTRADO <==')
    print('CEP: {}'.format(pesquisa['cep']))
    print('Logradouro: {}'.format(pesquisa['logradouro']))
    print('Bairro: {}'.format(pesquisa['bairro']))
    print('Cidade: {}'.format(pesquisa['localidade']))
    print('Estado: {}'.format(pesquisa['uf']))
    print('Regiao: {}'.format(pesquisa['regiao']))
else:
    print('{}: CEP INVALIDO.'.format(cep_input))


