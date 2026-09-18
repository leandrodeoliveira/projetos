# Calcular Consumo-Enegia

print("--- CONSUMO-ENERGIA ---")

# Entrada dos dados pelo usuario
aparelho = input("Aparelho: ")
potencia = float(input("Potencia (em Watts): "))
horas = float(input("Horas de uso por dia: "))

# Calculo do consumo em kWh e valor final
consumo = (potencia * horas * 30) / 1000
valor_kwh = 0.75
total = consumo * valor_kwh

# Exibe o resultado
print("\n--- RESUMO ---")
print(f"Nome do aparelho: {aparelho}")
print(f"Consumo por mes: {consumo:.2f} kWh")
print(f"Custo estimado: R$ {total:.2f}")
