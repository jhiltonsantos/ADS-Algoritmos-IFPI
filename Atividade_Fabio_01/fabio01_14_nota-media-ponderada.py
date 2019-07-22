# entrada
nota1 = float(input('Qual a primeira nota: '))
peso1 = int(input('Qual o peso da primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))
peso2 = int(input('Qual o peso da segunda nota: '))
nota3 = float(input('Qual a terceira nota: '))
peso3 = int(input('Qual o peso da terceira nota: '))

# processamento
media_ponderada = ((nota1*peso1) + (nota2*peso2) + (nota3*peso3)) / (peso1 + peso2 + peso3)

# saida
print ('A media das notas sera de: {}'.format(media_ponderada))
