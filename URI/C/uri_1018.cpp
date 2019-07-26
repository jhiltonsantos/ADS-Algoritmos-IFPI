#include<stdio.h>
#include<math.h>

int main(){
    int valor;
    scanf("%d", &valor);
    
    int nota_100, resto_100, nota_50, resto_50, nota_20, resto_20, nota_10, resto_10;
    int nota_5, resto_5, nota_2, nota_1;
    
    nota_100 = valor / 100;
    resto_100 = valor % 100;
    nota_50 = resto_100/50;
    resto_50 = resto_100%50;
    nota_20 = resto_50/20;
    resto_20 = resto_50%20;
    nota_10 = resto_20/10;
    resto_10 = resto_20%10;
    nota_5 = resto_10/5;
    resto_5 = resto_10%5;
    nota_2 = resto_5/2;
    nota_1 = resto_5%2;
    
    printf("%d\n", valor);
    printf("%d nota(s) de R$ 100,00\n", nota_100);
    printf("%d nota(s) de R$ 50,00\n", nota_50);
    printf("%d nota(s) de R$ 20,00\n", nota_20);
    printf("%d nota(s) de R$ 10,00\n", nota_10);
    printf("%d nota(s) de R$ 5,00\n", nota_5);
    printf("%d nota(s) de R$ 2,00\n", nota_2);
    printf("%d nota(s) de R$ 1,00\n", nota_1);
    
    return 0;
}
