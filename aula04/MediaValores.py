qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor:"))

# Entrada de valores
while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite um valor:"))  # Caso digite um valor negativo o laço encerra

media = soma / qtd

print("\nTotal da soma:", soma)
print("\nQuantidade de valores digitados:", qtd)
print("\nMédia dos valores:", media)

# Explicação do código:

# - Inicializamos as variáveis qtd, soma e media.

# - Solicitamos ao usuário que digite um valor e convertemos para um número de ponto flutuante.

# - Iniciamos um loop while que continua enquanto o valor digitado for maior que 0.0.

# - Dentro do loop, somamos o valor à soma, incrementamos a quantidade de valores digitados e solicitamos ao usuário que digite outro valor.

# - Quando o usuário digitar um valor negativo, o loop encerra.

# - Calculamos a média dos valores.

# - Por fim, imprimimos a soma total, a quantidade de valores digitados e a média dos valores.

