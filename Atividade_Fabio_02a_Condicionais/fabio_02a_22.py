def main():
    inicio_hora = int(input('Hora inicial: '))
    inicio_min = int(input('Minuto inicial: '))
    fim_hora = int(input('Hora final: '))
    fim_min = int(input('Minuto inicial: '))

    calc_hora = fim_hora - inicio_hora
    calc_min = fim_min - inicio_min
    modulo_hora = abs(calc_hora)
    modulo_min = abs(calc_min)
    
    if inicio_hora > fim_hora:
        x = 24 - inicio_hora
        calc_hora = x + fim_hora
    else:
        if modulo_hora <= 24:
            if inicio_hora > fim_hora:

                if modulo_min >= 60:
                    modulo_hora = modulo_hora - 1
                    modulo_min = modulo_min - 60
                    print('{} horas e {} minutos.'.format(modulo_hora,modulo_min))
                else: 
                    print('{} horas e {} minutos.'.format(modulo_hora,modulo_min))

            else:
                print('invalido')    
    

if __name__ == '__main__':
    main()



