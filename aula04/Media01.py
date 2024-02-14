notaA = float(input("Informe a primeira nota:"))
notaB = float(input("Informe a segunda nota:"))

# Calcular média
mediafinal = (notaA + notaB) / 2

# Verificação
if mediafinal >= 7.0:
    print("A Média: %.1f - Aprovado" % mediafinal)
else:
    print("A Média: %.1f - Reprovado" % mediafinal)

# Explicação do código:

# - Solicitamos ao usuário que informe duas notas, convertendo-as para números de ponto flutuante.

# - Calculamos a média das notas.

# - Verificamos se a média é maior ou igual a 7.0.

# - Se for verdadeira, imprime "Aprovado" junto com a média.

# - Se for falsa, imprime "Reprovado" junto com a média.

