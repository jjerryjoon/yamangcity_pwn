#include <stdio.h>
int changeme;

int main() {
	char name[64];
	read(0, name, 64);
	printf(name);

	if (changeme == 1000)
		printf("Hacking Successful..!\n");
}
