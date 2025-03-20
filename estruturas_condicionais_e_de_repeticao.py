# Estruturas condicionais e de repetição em um contexto financeiro

# Exemplo de estrutura condicional
saldo = 1500.00
saque = 250.00

if saque <= saldo:
    saldo -= saque
    print(f"\nTransacao 1 - Saque de R${saque:.2f} realizado com sucesso!")
    print(f"Saldo 1 -Saldo atual: R${saldo:.2f}\n")
else:
    print("\nSaldo insuficiente para realizar o saque.\n")

# Exemplo de estrutura de repetição com for
transacoes = [100.00, -50.00, 200.00, -300.00, 50.00]
saldo = 1000.00

for transacao in transacoes:
    saldo += transacao
    print(f"Transacao 2 - Transacao de R${transacao:.2f} realizada.")
    print(f"Saldo 2 - Saldo atual: R${saldo:.2f}\n")

# Exemplo de estrutura de repetição com while
saldo = 1000.00
meta = 2000.00
deposito = 100.00

while saldo < meta:
    saldo += deposito
    print(f"Deposito 3 - Deposito de R${deposito:.2f} realizado.")
    print(f"Saldo 3 - Saldo atual: R${saldo:.2f}\n")

print("Meta de saldo alcancada!")