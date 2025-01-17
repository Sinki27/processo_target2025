import json

def analisar_faturamento(arquivo):
  """
  Analisa os dados de faturamento em um arquivo JSON.

  Args:
    arquivo: Nome do arquivo JSON.

  Returns:
    Uma tupla com o menor valor, o maior valor e a quantidade de dias acima da média.
  """

  with open(arquivo, 'r') as f:
    dados = json.load(f)

  # Extrai os valores de faturamento
  valores = [item['valor'] for item in dados if item['valor'] > 0]

  # Calcula a média, o menor valor e o maior valor
  media = sum(valores) / len(valores)
  menor_valor = min(valores)
  maior_valor = max(valores)

  # Conta os dias com faturamento acima da média
  dias_acima_media = sum(1 for valor in valores if valor > media)

  return menor_valor, maior_valor, dias_acima_media

# Exemplo de uso
arquivo = 'faturamento.json'
menor, maior, dias_acima = analisar_faturamento(arquivo)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Dias acima da média: {dias_acima}")