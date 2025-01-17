## Desafios

Este repositório contém a minha resolução para diversos desafios de programação. Os desafios foram realizados em Python.

### Desafio: Analisando o Código e Calculando o Valor Final de SOMA

**Descrição:**
Declaração de variáveis:

INDICE: Define o valor limite da soma (13).
SOMA: Inicializa a variável que irá armazenar o resultado da soma (0).

Condição: O loop continua enquanto K for menor que INDICE.
Corpo do loop:
O laço for K in range(1, INDICE+1) percorre os valores de K no intervalo de 1 a 13, incluindo 13 (o valor INDICE + 1 torna o limite superior inclusivo).
SOMA += K: Adiciona o valor atual de K à variável SOMA.
Impressão:

imprimir(SOMA): Após o término do loop, o valor final de SOMA é impresso.

**Código:**
```python
INDICE = 13
SOMA = 0

for K in range(1, INDICE+1):
    SOMA += K

print(SOMA)
#resultado = 91
```

### Desafio: Verificar Números na Sequência de Fibonacci

**Descrição:**
Este desafio consiste: 

Função pertence_fibonacci(num):

a, b = 0, 1: Inicializa as duas primeiras variáveis da sequência.
while b <= num: Enquanto o valor atual (b) for menor ou igual ao número informado, o loop continua.
if b == num: Se o valor atual for igual ao número informado, o número pertence à sequência.
a, b = b, a + b: Atualiza os valores de a e b para os próximos termos da sequência.
Entrada do Usuário:

numero = int(input("Digite um número: ")): Lê o número informado pelo usuário e converte para inteiro.
Verificação e Saída:

if pertence_fibonacci(numero): Chama a função para verificar se o número pertence à sequência.
print(...) Imprime a mensagem correspondente ao resultado.

**Código:**
```python
def pertence_fibonacci(num):
  """Verifica se um número pertence à sequência de Fibonacci.
  Args:
    num: O número a ser verificado.
  Returns:
    True se o número pertence à sequência, False caso contrário.
  """
  a, b = 0, 1
  while b <= num:
    if b == num:
      return True
    a, b = b, a + b
  return False
# Entrada do usuário
numero = int(input("Digite um número: "))
# Verificação e saída
if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")
```

