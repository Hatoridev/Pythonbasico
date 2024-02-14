codigo = 10
salario = 1500.00
nome = 'Jose'
situacao = True

tipo = type(salario)
print(salario)
print(tipo)
print("Código:", codigo, "Nome:", nome, "O salário atual é de:", salario)
print("Código:" + str(codigo) + " Nome:" + nome + " O salário atual é de:" + str(salario))

# Explicação do código:

# - Definimos quatro variáveis: codigo, salario, nome e situacao.

# - Obtemos o tipo de dado da variável salario usando a função type().

# - Imprimimos o valor e o tipo de dado da variável salario.

# - Imprimimos as informações usando diferentes métodos de formatação: com vírgula e com concatenação de strings.

# - O método com vírgula não requer conversão de tipos, enquanto o método com concatenação requer conversão de tipos para garantir que todos os valores sejam strings.

