#include <stdio.h>
int main() {
	int arr[5];
	int num;
	
	for(int i=0; i<5; i++)
		arr[i] = i;

	scanf("%d", &num);
	printf("arr[%d] => %d\n", num, arr[num]);
}

