# operadores_de_identidade.py

# Exemplo de operadores de identidade em um contexto financeiro

# Definindo algumas variáveis financeiras
saldo_conta_corrente = 1500.00
saldo_conta_poupanca = 1500.00
saldo_investimento = 3000.00

# Usando o operador 'is' para verificar se duas variáveis apontam para o mesmo objeto
mesma_conta = saldo_conta_corrente is saldo_conta_poupanca
print(f"Conta corrente e conta poupanca sao a mesma conta? {mesma_conta}")

# Usando o operador 'is not' para verificar se duas variáveis não apontam para o mesmo objeto
conta_diferente = saldo_conta_corrente is not saldo_investimento
print(f"Conta corrente e conta de investimento sao contas diferentes? {conta_diferente}")

# Criando uma nova variável que referencia o mesmo objeto que saldo_conta_corrente
saldo_conta_corrente_ref = saldo_conta_corrente

# Verificando se saldo_conta_corrente e saldo_conta_corrente_ref são o mesmo objeto
mesma_referencia = saldo_conta_corrente is saldo_conta_corrente_ref
print(f"Saldo da conta corrente e sua referencia sao o mesmo objeto? {mesma_referencia}")