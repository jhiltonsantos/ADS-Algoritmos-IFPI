def main():
	a, b, c = map(float, input().split())
	lista = [a,b,c]
	ordem = sorted(lista, reverse=True)
	A,B,C = ordem[0],ordem[1],ordem[2]
	
	if A != B and B != C:
		print('{}'.format(valida_triangulo(A,B,C)))
	else:
		print('{}'.format(valida_triangulo(A,B,C)))
		print('{}'.format(tipo_triangulo(A,B,C)))


def valida_triangulo(A,B,C):
	if A >= B+C:
		return 'NAO FORMA TRIANGULO'
	elif (A**2) == (B**2)+(C**2):
		return 'TRIANGULO RETANGULO'
	elif (A**2) > (B**2)+(C**2):
		return 'TRIANGULO OBTUSANGULO'
	elif (A**2) < (B**2)+(C**2):
		return 'TRIANGULO ACUTANGULO'

def tipo_triangulo(A,B,C):	
	if A == B and B == C:
		return 'TRIANGULO EQUILATERO'
	elif A == B or B == C or C == A:
		return 'TRIANGULO ISOSCELES'


if __name__ == '__main__':
	main()