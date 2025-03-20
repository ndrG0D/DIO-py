# Exemplos de métodos úteis com a classe string em Python

# Maiúsculas
texto = "exemplo de texto"
texto_maiusculas = texto.upper()
print("Maiusculas:", texto_maiusculas)

# Minúsculas
texto_minusculas = texto.lower()
print("Minusculas:", texto_minusculas)

# Títulos (primeira letra de cada palavra em maiúscula)
texto_titulo = texto.title()
print("Titulo:", texto_titulo)

# Remover espaços em branco
texto_com_espacos = "   exemplo de texto   "
texto_sem_espacos = texto_com_espacos.strip()
print("Sem espacos em branco:", texto_sem_espacos)

# Junções (concatenar strings com um delimitador)
lista_de_palavras = ["exemplo", "de", "texto"]
texto_junto = " ".join(lista_de_palavras)
print("Texto junto:", texto_junto)

# Centralizações
texto_centralizado = texto.center(30, '-')
print("Texto centralizado:", texto_centralizado)