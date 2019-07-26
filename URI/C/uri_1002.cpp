#include<stdio.h>
#include <math.h>

int main(){
	double raio, area_circulo;
	scanf("%lf", &raio);

	area_circulo = 3.14159 * pow(raio,2);
	
	printf("A=%.4lf\n",area_circulo);
	return 0;

	
}


