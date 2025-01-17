def calcular_percentual_faturamento(dados):
  """Calcula o percentual de faturamento por estado.

  Args:
    dados: Um dicionário onde as chaves são os estados e os valores são os faturamentos.

  Returns:
    Um dicionário com os estados e seus respectivos percentuais de faturamento.
  """

  # Calcula o faturamento total
  faturamento_total = sum(dados.values())

  # Calcula o percentual de cada estado
  percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in dados.items()}

  return percentuais

# Dados do problema
faturamento_estados = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53
}

# Calcula os percentuais
percentuais = calcular_percentual_faturamento(faturamento_estados)

# Imprime os resultados
for estado, percentual in percentuais.items():
  print(f"O estado {estado} representou {percentual:.2f}% do faturamento total.")