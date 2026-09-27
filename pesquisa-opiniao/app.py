# =======================================================
# Empresa TudoWeb - Pesquisa de Satisfação no Atendimento
# Agenda 08 - Estruturas de Repetição
# Aluno: Leandro de Oliveira
# =======================================================

qtd_excelente = 0
qtd_ruim = 0

for entrevistado in range(1, 51):

    print("\nEntrevistado", entrevistado)

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nOpinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção desejada: "))

    if opiniao == 1:
        qtd_excelente += 1

    elif opiniao == 3:
        qtd_ruim += 1

print("\n==============================")
print(" RESULTADO DA PESQUISA")
print("==============================")
print("Quantidade de respostas EXCELENTE:", qtd_excelente)
print("Quantidade de respostas RUIM:", qtd_ruim)
print("==============================")