#!/bin/bash
function my_factorial() {
	if [ $1 -le 1 ] ; then
		echo "1"
	else
		echo $(( $1 * `my_factorial $(( $1 - 1 ))` ))
	fi
}
read -p "Enter the value whose factorial is to be printed: " value
echo "the factorial of $value is: `my_factorial $value`"

# user input: 					https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php, 
#								http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_08_02.html

# for arithematic operations: 	https://bash.cyberciti.biz/guide/Perform_arithmetic_operations

# comparision operators:		http://tldp.org/LDP/abs/html/comparison-ops.html

# if else :						http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-6.html
#								https://www.thegeekstuff.com/2010/06/bash-if-statement-examples
#								https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php

#  for functions: 				https://www.tutorialkart.com/bash-shell-scripting/bash-functions
#								https://ryanstutorials.net/bash-scripting-tutorial/bash-functions.php

# for function returning: 		http://www.linuxjournal.com/content/return-values-bash-functions

