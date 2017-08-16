/* 

A simple C program that checks whether a given string is a valid C identifier or not

*/

#include <stdio.h>
#include <ctype.h>
#define MAX_LENGTH 100
#define TRUE 1
#define FALSE 0
#define BREAK_OUT 
int main(int argc, char *argv[]) {

	char ans;
	
	do {
		char identifier_name[MAX_LENGTH];
		int is_valid = TRUE;
		printf("\nEnter the identifier name to be tested : ");
		scanf(" %[^\n]s", identifier_name);
		
		for(int i = 0; identifier_name[i] != '\0'; i++) {	
			char ch = identifier_name[i];
			
			if (i == 0) {
				if (ch == '_' || isalpha(ch))
					continue;
				else {
					is_valid = FALSE;
					break;
				}
			}
			
			else {
				if(ch == '_' || isalnum(ch))
					continue;
				else {
					is_valid = FALSE;
					break;
				}
			}
		}

		if(is_valid) {
			printf("Its a valid identifier name\n");
		}
		else {
			printf("Its not a valid identifier name\n");
		}

		printf("\nDo you want to continue?(Y/N)");
		scanf(" %c", &ans);
	} while (ans == 'Y' || ans == 'y');

	return 0;
}