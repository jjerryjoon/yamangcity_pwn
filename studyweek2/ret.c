#include <stdio.h>
#include <unistd.h>

void hello() {
	char hello[16] = "Hello_World!\n";
	printf("%s", hello);
}

void bye() {
	char bye[16] = "Bye_Bye!\n";
	printf("%s", bye);
}
void get_shell(){
	char *cmd = "/bin/sh";
  	char *args[] = {cmd, NULL};
	execve(cmd, args, NULL);

}

int main() {
	char buf[16];
	
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
	hello();
	bye();
	printf("please get shell!!!! if you can^^\n");
	read(1, buf, 0x100);
}
