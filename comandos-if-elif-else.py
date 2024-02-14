idade = int(input("Digite a idade da pessoa:"))

if idade > 18:
    print("Maior de idade")
elif idade > 16:
    print("Infanto Juvenil")
else:
    print("Menor de idade")

# Explicação do código:

# - Solicitamos ao usuário que digite a idade da pessoa e a convertemos para um número inteiro.

# - Verificamos as condições usando a estrutura if-elif-else:

#   - Se a idade for maior que 18, imprime "Maior de idade".

#   - Se a idade estiver entre 16 e 18 (inclusive), imprime "Infanto Juvenil".

#   - Caso contrário, imprime "Menor de idade".

# - A estrutura elif (abreviação de "else if") é usada para verificar múltiplas condições depois da primeira condição (if).

# - A estrutura else é usada para capturar todos os casos restantes que não foram cobertos pelas condições anteriores.

