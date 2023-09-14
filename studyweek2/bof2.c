#include <stdio.h>
int main() {
	char name[10];
	int target = 0x61616161;

	printf("What is your name?\n");
	read(1, name, 0x30);
	printf("Name: %s\n", name);
}
