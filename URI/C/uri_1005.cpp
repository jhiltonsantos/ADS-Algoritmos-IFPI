#include <stdio.h>

int main(){
	double numero_1, numero_2, media;
	scanf("%lf", &numero_1);
	scanf("%lf", &numero_2);

	media = ((numero_1*3.5)+(numero_2*7.5)) / 11;

	printf("MEDIA = %.5lf\n", media);
	return 0;
}