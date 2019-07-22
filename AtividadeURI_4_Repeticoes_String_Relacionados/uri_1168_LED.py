def main():
    quant_n = int(input())
    i = 0
    while i < quant_n:
        numero = input()
        print('%d leds' % quantidade_led(numero))
        i += 1

def quantidade_led(numero):
    quant_led_total = 0
    for i in range(len(numero)):
        if numero[i] == '0':
            quant_led_total += 6
        elif numero[i] == '1':
            quant_led_total += 2
        elif numero[i] == '2':
            quant_led_total += 5
        elif numero[i] == '3':
            quant_led_total += 5
        elif numero[i] == '4':
            quant_led_total += 4
        elif numero[i] == '5':
            quant_led_total += 5
        elif numero[i] == '6':
            quant_led_total += 6
        elif numero[i] == '7':
            quant_led_total += 3
        elif numero[i] == '8':
            quant_led_total += 7
        elif numero[i] == '9':
            quant_led_total += 6
   
    return quant_led_total


if __name__ == '__main__':
    main()