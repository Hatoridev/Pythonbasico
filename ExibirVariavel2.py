codigo = int(input("Digite o código do funcionário "))
nome = input("Digite o nome do funcionário ")
salario = float(input("Informe o salário "))
ativo = True

print("Código: %d "% codigo)
print("Nome: %s "% nome)
print("Salário: %.2f "% salario)
print("Ativo: %r "% ativo)

# Explicação do código:

# - Solicitamos ao usuário que digite o código, nome e salário do funcionário.

# - Convertemos o código para um número inteiro usando int() e o salário para um número de ponto flutuante usando float().

# - Imprimimos na tela o valor de cada variável utilizando formatação de string.

# - %d é usado para formatar valores inteiros, %s para formatar strings, %.2f para formatar números de ponto flutuante com duas casas decimais e %r para formatar valores booleanos.

