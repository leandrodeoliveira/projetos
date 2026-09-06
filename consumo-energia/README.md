# ⚡ Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

Código feito em Python focado em calcular a conta de luz por aparelho. O script pede o nome do eletrodoméstico, a potência e as horas que ele roda no dia, entregando o gasto mensal em kWh e em reais.

---

## 📌 Como esse projeto funciona

O programa pede três dados básicos:

- Nome do aparelho
- Potência em Watts (W)
- Horas de uso diário

Depois ele faz a conta do consumo mensal e multiplica pela taxa por kWh.

---

## 🧮 Fórmula usada

Cálculo do consumo (baseado em 30 dias):
`Consumo (kWh) = (Potência * Horas * 30) / 1000`

Para achar o valor na conta (taxa fixa de R$ 0,75/kWh):
`Custo (R$) = Consumo * 0.75`

### Exemplo

Aparelho de **1000 W** ligado por **5 horas** ao dia:

- Consumo: `(1000 * 5 * 30) / 1000 = 150 kWh`
- Valor final: `150 * 0.75 = R$ 112,50`

---

## ▶️ Como rodar o projeto

1. É necessário ter o **Python 3** instalado no computador.
2. Clone o repositório:

```bash
git clone [https://github.com/leandrodeoliveira/projetos.git](https://github.com/leandrodeoliveira/projetos.git)
```
cd projeto/consumo-energia
python app.py

