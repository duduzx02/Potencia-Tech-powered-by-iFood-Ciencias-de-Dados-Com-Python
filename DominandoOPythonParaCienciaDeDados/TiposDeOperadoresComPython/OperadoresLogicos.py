saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
print(saque <= limite)

# Operador E(and)
print(saldo >= saque and saque <= limite)

# Operador OU(or)
print(saldo >= saque or saque <= limite)

# Operador de negação (not)
print(not True)
print(not False)

print((saldo >= saque and saque <= limite) or (saldo >= saque and limite <= saque))
