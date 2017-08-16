/*
A C++ program that parses through a C source code file and lists down the keywords used in the file
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;
const string KEYWORDS[] = {	"auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", 
							"enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", 
							"short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", 
							"unsigned", "void", "volatile", "while"};

vector<string> tokenizer(string line) {
	vector<string> tokens;
	istringstream ss(line);
	string token;
	while(ss >> token)
		tokens.push_back(token);

	return tokens;
}

vector<string> filterTokens(vector<string> tokens) {
	vector<string> filteredTokens;
	bool exists;
	for(int i = 0; i < tokens.size(); i++) {
		exists = find(begin(KEYWORDS), end(KEYWORDS), tokens[i]) != end(KEYWORDS);
		if(exists)
			filteredTokens.push_back(tokens[i]);
	}

	return filteredTokens;
}

int main() {
	string filePath, readString;
	vector <string> tokens, filteredTokens;
	vector < pair< int, vector<string> > > answer;
	int lineNo = 1;

	cout<<"Enter absolute path of the file to be parsed :- ";
	getline(cin, filePath);
	ifstream in(filePath, ios_base::in);
	if (!in) {
		cerr<<"Unable to open file"<<endl;
		exit(1);
	}
	
	while(!in.eof()) {
		getline(in, readString);
		tokens = tokenizer(readString);
		filteredTokens = filterTokens(tokens);
		if (filteredTokens.size() > 0)
			answer.push_back(make_pair(lineNo, filteredTokens));
		lineNo++;
	}

	for(int i = 0; i < answer.size(); i++) {
		cout<<"Line "<<answer[i].first<<": ";
		for(int j = 0; j < answer[i].second.size(); j++) {
			cout<<answer[i].second[j]<<", ";
		}
		cout<<endl;
	}

	return 0;
}