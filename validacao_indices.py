import re


regex = r"(?:(?:\-[1-9](\d+)?|\d+)(\:\-[1-9](\d+)?|\:\d+)?|(?:\'[a-zA-Z ]+\')(\:\'[a-zA-Z ]+\')?|(?:\"[a-zA-Z ]+\")(\:\"[a-zA-Z ]+\")?)"

def is_valid_pandas_index(index):
    """Função que verifica se um índice é válido baseado na expressão regular fornecida."""
    return bool(re.fullmatch(regex, index))


test_indexes = [
    "0", "-10", "2:5", "-1:2", "'Date'", "\"Column Name\"", "'Start':'End'", "\"Begin\":\"Finish\"",
    "10:-5", "1", "'Invalid : Name'", "Some random text"
]


print("Validação de índices de dataset (para os exemplos definidos):\n")
for index in test_indexes:
    is_valid = is_valid_pandas_index(index)
    print(f"Índice: {index} - Válido: {is_valid}")


print("\nDigite um índice para validar (ou 'sair' para terminar):")
while True:
    user_input = input("Índice: ").strip()
    
    if user_input.lower() == "sair":
        print("Saindo...")
        break
    
   
    if is_valid_pandas_index(user_input):
        print(f"Índice '{user_input}' é válido!")
    else:
        print(f"Índice '{user_input}' não é válido!")
