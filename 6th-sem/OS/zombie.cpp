/*
Program to create a zombie process
*/

#include <iostream>
#include <unistd.h>

int main() {
	int pid = fork();

	// Parent process 
	if (pid > 0) {
		sleep(10);
		system("ps aux | grep 'Z'");
	}

	// Child process
	else       
		exit(0);

	return 0;
}

/*

REFERENCES:-

What Is a “Zombie Process” on Linux? - https://www.howtogeek.com/119815/htg-explains-what-is-a-zombie-process-on-linux/

*/