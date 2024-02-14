def lernotas():
    n = float(input('Digite uma nota para o aluno (a):'))
    return n

def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print("Média:", media, "Resultado:", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
resultado(a, b)

# Explicação do código:

# - Definimos duas funções: lernotas() para solicitar as notas do aluno e resultado() para calcular a média e determinar o resultado.

# - Na função lernotas(), solicitamos ao usuário que digite uma nota e a retornamos.

# - Na função resultado(), calculamos a média das notas recebidas e determinamos se o aluno foi aprovado ou reprovado.

# - Chamamos a função lernotas() duas vezes para obter as notas do aluno.

# - Em seguida, chamamos a função resultado() com as duas notas obtidas como argumentos.

# - O resultado da função resultado() é impresso na tela.

