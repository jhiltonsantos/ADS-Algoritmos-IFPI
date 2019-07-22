def main():
   altura = float(input('Altura (em metros): '))
   peso = float(input('Peso (em quilogramas): '))

   calc_imc = peso / (altura**2)

   if calc_imc < 25:
       print('Peso Normal')
   elif 25 <= calc_imc <= 30:
       print('Obeso')
   elif calc_imc > 30:
       print('Obesidade morbida')
        

if __name__ == '__main__':
    main()
