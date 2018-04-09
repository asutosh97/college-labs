#include <unistd.h>
#include <stdio.h>

int main() {
//	fork();
//	fork() && fork() || fork();
	if (fork())
		printf("parent \n");
	else
		printf("child \n");

	return 0;
}