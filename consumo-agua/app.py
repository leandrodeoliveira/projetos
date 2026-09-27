# Agenda 07
# Sistema de classificação do consumo de água

# Solicita ao usuário o tipo de imóvel
tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ")

# Solicita o consumo mensal de água em metros cúbicos
consumo = float(input("Digite o consumo mensal de água em m³: "))

# Verifica se o imóvel é comercial
if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

# Verifica se é apartamento e se o consumo é menor que 10 m³
elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

# Verifica se é apartamento ou casa e se o consumo é até 25 m³
elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

# Qualquer outra situação será considerada consumo excessivo
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
