gabarito = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
maior_acertos = 0
menor_acertos = 10
total_acertos = 0
total_alunos = 0

while True:
    print("Nova Prova!")
    respostas_aluno = []

    # Recebe as respostas do aluno
    for i in range(10):
        resposta = input(f"Digite a resposta da questão {i+1} (A, B, C, D ou E): ").upper()
        while resposta not in ['A', 'B', 'C', 'D']:
            resposta = input("Resposta inválida! Digite A, B, C ou D: ").upper()
        respostas_aluno.append(resposta)

    acertos = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            acertos += 1

    print(f"Você acertou {acertos} questões.")

    if acertos > maior_acertos:
        maior_acertos = acertos
    if acertos < menor_acertos:
        menor_acertos = acertos

    total_acertos += acertos
    total_alunos += 1

    continuar = input("Outro aluno vai fazer a prova? (S/N): ").upper()
    if continuar == 'S':
        pass
    else:
        break

media_turma = total_acertos / total_alunos if total_alunos > 0 else 0

print('RSULTADO DA PROVA')
print(f'Maior número de acertos: {maior_acertos}')
print(f'Menor número de acertos: {menor_acertos}')
print(f'Total de alunos: {total_alunos}')
print(f'Média de acertos da turma: {media_turma:.2f}')