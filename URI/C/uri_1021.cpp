#include<stdio.h>
#include<math.h>

int main(){
    double valor;
    scanf("%lf", &valor);
    
    int valor_int;
    valor_int = (int)valor;
    valor -= valor_int;
    
    int nota_100, resto_100, nota_50, resto_50, nota_20, resto_20, nota_10, resto_10;
    int nota_5, resto_5, nota_2;
    nota_100 = valor_int / 100;
    resto_100 = valor_int % 100;
    nota_50 = resto_100/50;
    resto_50 = resto_100%50;
    nota_20 = resto_50/20;
    resto_20 = resto_50%20;
    nota_10 = resto_20/10;
    resto_10 = resto_20%10;
    nota_5 = resto_10/5;
    resto_5 = resto_10%5;
    nota_2 = resto_5/2;
    
    int moedas, moeda_100, moeda_50, moeda_20, moeda_10, moeda_5, moeda_1;
    moeda_100 = resto_5%2;
    moedas = (valor *100);

    moeda_50 = moedas /50;
    moeda_20 = (moedas %50)/25;
    moeda_10 = (((moedas %50)%25)/10);
    moeda_5 = ((((moedas %50)%25)%10)/5);
    moeda_1 = ((((moedas %50)%25)%10)%5)/1;


    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n", nota_100);
    printf("%d nota(s) de R$ 50.00\n", nota_50);
    printf("%d nota(s) de R$ 20.00\n", nota_20);
    printf("%d nota(s) de R$ 10.00\n", nota_10);
    printf("%d nota(s) de R$ 5.00\n", nota_5);
    printf("%d nota(s) de R$ 2.00\n", nota_2);

    printf("MOEDAS:\n");
    printf("%d moeda(s) de R$ 1.00\n", moeda_100);
    printf("%d moeda(s) de R$ 0.50\n", moeda_50);
    printf("%d moeda(s) de R$ 0.25\n", moeda_20);
    printf("%d moeda(s) de R$ 0.10\n", moeda_10);
    printf("%d moeda(s) de R$ 0.05\n", moeda_5);
    printf("%d moeda(s) de R$ 0.01\n", moeda_1);

    return 0;
}
