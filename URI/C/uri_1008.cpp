#include<stdio.h>
#include <math.h>

int main(){
	int n_func, hora_func;
	double valor_hora;

	scanf("%d", &n_func);
	scanf("%d", &hora_func);
	scanf("%lf", &valor_hora);

	double salario;
	salario = hora_func * valor_hora;
	
	printf("NUMBER = %d\n", n_func);
	printf("SALARY = U$ %.2lf\n", salario);

	return 0;
	
}


