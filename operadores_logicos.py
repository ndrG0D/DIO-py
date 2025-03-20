# Exemplos de operadores lógicos em Python com operadores de comparação em um contexto financeiro

# Valores financeiros
saldo_conta = 1500
limite_credito = 2000
divida = 500
investimento = 3000

# Operador AND
resultado_and = (saldo_conta > divida) and (investimento > limite_credito)
print(f"Resultado de (saldo_conta > divida) and (investimento > limite_credito): {resultado_and}")

# Operador OR
resultado_or = (saldo_conta < divida) or (investimento > limite_credito)
print(f"Resultado de (saldo_conta < divida) or (investimento > limite_credito): {resultado_or}")

# Operador NOT
resultado_not = not (saldo_conta < divida)
print(f"Resultado de not (saldo_conta < divida): {resultado_not}")

# Combinação de operadores lógicos e de comparação
resultado_comb = (saldo_conta > divida) and (investimento > limite_credito) or (saldo_conta == investimento)
print(f"Resultado de (saldo_conta > divida) and (investimento > limite_credito) or (saldo_conta == investimento): {resultado_comb}")

# Comparação de igualdade
resultado_igual = (saldo_conta == 1500) and (limite_credito == 2000)
print(f"Resultado de (saldo_conta == 1500) and (limite_credito == 2000): {resultado_igual}")

# Comparação de desigualdade
resultado_desigual = (saldo_conta != divida) or (investimento != limite_credito)
print(f"Resultado de (saldo_conta != divida) or (investimento != limite_credito): {resultado_desigual}")

# Comparação maior ou igual
resultado_maior_igual = (saldo_conta >= 1500) and (limite_credito >= 2000)
print(f"Resultado de (saldo_conta >= 1500) and (limite_credito >= 2000): {resultado_maior_igual}")

# Comparação menor ou igual
resultado_menor_igual = (saldo_conta <= 1500) or (divida <= 500)
print(f"Resultado de (saldo_conta <= 1500) or (divida <= 500): {resultado_menor_igual}")