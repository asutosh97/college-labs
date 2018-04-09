/*
Program to demonstrate the use of fork()
*/

#include <iostream>
#include <unistd.h>
using namespace std;

int main() {
	int pid = fork();
	if (pid) {
		cout << "parent process :- " << getpid() << endl;
	}
	else {
		cout << "child process :- " << getpid() << endl;
	}
	return 0;
}