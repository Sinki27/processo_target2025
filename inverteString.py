def inverter_string(string):
    """Inverte os caracteres de uma string.

    Args:
        string: A string a ser invertida.

    Returns:
        A string invertida.
    """

    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

# Exemplo de uso:
minha_string = "Python"
string_invertida = inverter_string(minha_string)
print(string_invertida)  # Saída: nohtyP