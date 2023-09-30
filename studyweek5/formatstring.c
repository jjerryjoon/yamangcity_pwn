#include <stdio.h>
int main() {
	int a, b;
	int one = 1, two = 2;

	printf("yamangcity is awesome!!!%n", &a);
	printf("%44c%n", 'q', &b);

	printf("\n%d %d\n", a, b);
	printf("%2$d %1$d", one, two);
}
