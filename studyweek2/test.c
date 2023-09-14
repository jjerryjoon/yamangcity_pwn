#include<stdio.h>
#include<stdlib.h>

int sum(int a, int b){
	int op1, op2;
	op1 = a;
	op2 = b;
	return op1 + op2;
}

int main(void){
	int a, b, result;
	scanf("%d %d", &a, &b);
	result = sum(a, b);
	printf("%d\n", result);
	return 0;
}
