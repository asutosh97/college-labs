/*
Program to demonstrate the use of fork()
*/

#include <iostream>
#include <unistd.h>
#include <cstdio>
using namespace std;

int main() {
	
	/*
	int pid = fork();
	if (pid) {
		cout << "parent process :- " << getpid() << endl;
	}
	else {
		cout << "child process :- " << getpid() << endl;
	}
	*/

	int a = 10;
	if (fork() == 0) { 
		a = a + 5; 
		printf("%d,%p\n", a, &a); 
	}
	else { 
		a = a - 5; 
		printf("%d, %p\n", a, &a); 
	}

	return 0;
}