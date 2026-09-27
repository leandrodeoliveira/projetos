# Atividade de DS1 - Agenda 06
# Sistema de Desconto Progressivo

# Entrada de dados
# Solicita ao usuário o valor total da compra
total_compra = float(input("Informe o valor da compra: R$ "))

# Estrutura de decisão para definir o desconto
if total_compra < 200:
    porcentagem = 5
elif total_compra < 300:
    porcentagem = 10
else:
    porcentagem = 15

# Cálculo do valor do desconto
valor_desconto = total_compra * (porcentagem / 100)

# Cálculo do valor final da compra
valor_final = total_compra - valor_desconto

# Exibição dos resultados
print("\n===== RESUMO DA COMPRA =====")
print(f"Valor da compra: R$ {total_compra:.2f}")
print(f"Desconto aplicado ({porcentagem}%): R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
