import requests

print('######################')
print('### CONSULTAR PAIS ###')
print('######################')

pais_input = input('Digite o nome do país? (nome global ex: brazil com z,italy) ').strip().lower()

url = 'https://restcountries.com/v3.1/name/{}'.format(pais_input)

resultado = requests.get(url)
dados = resultado.json()
pais = dados[0]

print('==> Páis encontrado <==')
print('Nome: {}'.format(pais['name']['common']))
print('Linguagem: {}'.format(' , '.join(pais.get('languages', {}).values())))
print('Região: {}'.format(pais['region']))
print('Sub-Região: {}'.format(pais['subregion']))
print('Capital: {}'.format(pais.get('capital', ['N/A'])[0]))
print('Sigla da moeda: {}'.format(list(pais.get('currencies', {}).keys())[0]))
print('Nome da moeda: {}'.format(list(pais.get('currencies', {}).values())[0]['name']))
print('Simbolo da moeda: {}'.format(list(pais.get('currencies', {}).values())[0]['symbol']))
print('Países que fazem fronteira: {}'.format(', '.join(pais.get('borders', [])) if pais.get('borders') else 'Nenhum'))
