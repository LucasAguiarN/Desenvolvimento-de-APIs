import requests

moedas_nome = { 
    "USD": "Dólares Americanos",
    "EUR": "Euros",
    "GBP": "libras esterlinas",
    "JPY": "ienes",
    "ARS": "pesos argentinos",
    "CNY": "yuans chineses"
}

sigla = input("Digite a sigla da moeda desejada (ex: USD, EUR, GBP): ").upper().strip()

url ="https://api.exchangerate-api.com/v4/latest/BRL"

resposta = requests.get(url)
dados = resposta.json()

if sigla in dados["rates"]:
    valor = dados["rates"][sigla]
    moedas_nome = moedas_nome.get(sigla, sigla)
    print(f"1 Real vale {valor:.2f} {moedas_nome}.")
else:
    print("Moeda não encontrada na API.")