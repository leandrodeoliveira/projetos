# 🛒 Sistema de Desconto Progressivo

## Sobre o Projeto

Atividade da Agenda 06 da disciplina de Desenvolvimento de Sistemas I.

O programa recebe o valor total da compra e calcula o desconto final de acordo com a tabela de regras da atividade proposto.

### Regras de desconto

- Compras abaixo de R$ 200,00: 5% de desconto.
- Compras entre R$ 200,00 e R$ 299,99: 10% de desconto.
- Compras acima de R$ 300,00: 15% de desconto.

---

## Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)


---

## Linguagem Utilizada

O programa foi desenvolvido utilizando a linguagem **Python**.

---

## Fórmulas Utilizadas

### Cálculo do desconto

```python
valor_desconto = total_compra * (porcentagem / 100)
```

### Cálculo do valor final

```python
valor_final = total_compra - valor_desconto
```

---

## Como Executar

1. Abra o projeto no VS Code.
2. Execute o arquivo `app.py`.
3. Digite o valor da compra quando solicitado.
4. Pressione Enter.
5. O programa exibirá o desconto aplicado e o valor final da compra.

Exemplo:

```text
Informe o valor da compra: R$ 250

===== RESUMO DA COMPRA =====
Valor da compra: R$ 250.00
Desconto aplicado (10%): R$ 25.00
Valor final a pagar: R$ 225.00
```

---

## Estrutura de Decisão Utilizada

O programa utiliza estruturas condicionais:

```python
if
elif
else
```

Essas estruturas permitem verificar o valor da compra e determinar qual desconto será aplicado.

---

## Autor

Atividade desenvolvida por Leandro de Oliveira para a disciplina de Desenvolvimento de Sistemas I.
