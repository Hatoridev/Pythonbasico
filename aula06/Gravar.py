arquivo = open('arqText.txt', 'w')
arquivo.write('Curso python \n')
arquivo.write('Aula Prática\n')
arquivo.close()

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()



# Explicação do código:

# - Abrimos o arquivo 'arqText.txt' em modo de escrita ('w') e escrevemos duas linhas de texto.

# - Fechamos o arquivo após a escrita.

# - Em seguida, reabrimos o arquivo em modo de leitura ('r'), lemos todo o conteúdo e o imprimimos na tela.

# - Por fim, fechamos o arquivo novamente após a leitura.
