/*
A C++ program that takes in an arithematic expression and outputs the operators and the operands on which the operator was operated.

NOTES:-
(i) assignment operator has the lowest precedence
(ii) ! = pre-inc, @ = pre-dec, # = post-inc, $ = post-dec
*/

#include <iostream>
#include <stack>
#include <vector>

using namespace std;

string removeSpaces(string str) {
	string ans;
	for(int i = 0; i < str.size(); i++) {
		if(str[i] == ' ')
			continue;
		ans += str[i];
	}
	return ans;
}

//	returns the precedence value of a given operator
int precedence(char c) {
    if(c == '+'||c == '-')
        return 1;

    else if(c == '*'||c == '/')
        return 2;

    else if(c == '^')
        return 3;

    else if(c == '(' || c == '=')
        return 0;
}

char unaryMapping(char unaryOperator, bool isPrevOperand) {
	
	char ans;

	// pre-inc
	if (unaryOperator == '+' && !isPrevOperand) {
		ans = '!';
	}
	//	pre-dec
	else if (unaryOperator == '-' && !isPrevOperand) {
		ans = '@';
	}
	//	post-inc
	else if (unaryOperator == '+' && isPrevOperand) {
		ans = '#';
	}
	//	post-dec
	else if (unaryOperator == '-' && isPrevOperand) {
		ans = '$';
	}

	return ans;
}

string infixToPostfix (string infixString) {
	
	stack <char> operators;
	string postfixString;
	bool isPrevOperand = false;
	
	for (int index = 0; index < infixString.size(); index++) {
		switch (infixString[index]) {

			case '+':    case '-': 

				if ((infixString[index + 1] == infixString[index]) && (infixString[index + 2] != infixString[index])) {
					if (isPrevOperand) {
						postfixString += unaryMapping(infixString[index], isPrevOperand);
						index++;
					}
					else {
						postfixString += infixString[index + 2];
						postfixString += unaryMapping(infixString[index], isPrevOperand);
						index += 2;
					}
					isPrevOperand = false;
					break;
				}

			case '*':    case '/':    case '^':   case '=':

				if(!operators.empty()) {
					while(!operators.empty() && (precedence(operators.top()) > precedence(infixString[index]))) {
						postfixString += operators.top();
						operators.pop();
					}
				}
				operators.push(infixString[index]);
                isPrevOperand = false;
                break;

            case '(':
                operators.push(infixString[index]);
                isPrevOperand = false;
                break;

            case ')':
				while (operators.top() != '(') {
					postfixString += operators.top();
					operators.pop();
				}
				operators.pop();
				isPrevOperand = false;
				break;

            default:
				postfixString += infixString[index];
                isPrevOperand = true;
                break;
        }
	}

	while (!operators.empty()) {
		postfixString += operators.top();
		operators.pop();
	}

	return postfixString;
}


vector<string> postfixEval(string postfixString) {
	vector<string> evals, lateEvals;
	stack <string> operands;

	string upperOperand, lowerOperand, pushString, _operator, _operand;
	for(int index = 0; index < postfixString.size(); index++) {
		switch(postfixString[index]) {

			case '+':	case '-':	case '*':	case '/':	case '^':	case '=':
				
				upperOperand = operands.top();
				operands.pop();
				lowerOperand = operands.top();
				operands.pop();

				_operator = "";
				_operator += postfixString[index];
				
				pushString = lowerOperand + " " + _operator + " " + upperOperand;
				operands.push(pushString);

				if (_operator == "=") 
					pushString = upperOperand + " is assigned to " + lowerOperand;
				else
					pushString = "Operator " + _operator + " operates on " + lowerOperand + " and " + upperOperand;
				evals.push_back(pushString);
				break;
			
			case '!':	case '@':

				if(postfixString[index] == '!')
					_operator = "incremented";
				else
					_operator = "decremented";

				upperOperand = operands.top();
				pushString = "Operand " + upperOperand + " is pre-" + _operator;
				evals.push_back(pushString);
				break;
			
			case '#':	case '$':

				if(postfixString[index] == '#')
					_operator = "incremented";
				else
					_operator = "decremented";

				upperOperand = operands.top();
				pushString = "Operand " + upperOperand + " is post-" + _operator;
				lateEvals.push_back(pushString);
				break;

			default:
				_operand = "";
				_operand += postfixString[index];
				operands.push(_operand);
				break;
		}
	}

	for(int i = 0; i < lateEvals.size(); i++) {
		evals.push_back(lateEvals[i]);
	}

	return evals;
}


int main() {

	// get input and filter it
	string inputString;
	getline(cin, inputString);
	string filteredInput = removeSpaces(inputString);

	// convert to postfix
	string postfixString = infixToPostfix(filteredInput);

	// postfixEvaluation
	vector<string> evaluations = postfixEval(postfixString);

	//	print the evaluations
	cout<<"The evaluations are :- "<<endl;
	for (int i = 0; i < evaluations.size(); i++) {
		cout<<evaluations[i]<<endl;
	}

	return 0;
}