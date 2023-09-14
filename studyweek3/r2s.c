#include <stdio.h>
#include <unistd.h>

void vuln(){
	char buf[50];
	printf("buf address is %p\n", buf);
	read(0, buf, 0x100);
}

int main() {
     vuln();
}
