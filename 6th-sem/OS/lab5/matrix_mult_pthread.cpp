/*
Program to calculate matrix multiplication using pthreads
*/

#include <iostream>
#include <cstdlib>
#include <vector>
#include <pthread.h>

using namespace std;
vector< vector<int> > result;

struct thread_data {
	vector<int> row, col;
	int row_index, col_index;
};

void *Multiply(void *threadarg) {
	struct thread_data *my_data = (struct thread_data *) threadarg;
	for (int i = 0; i < my_data->row.size(); i++)
		result[my_data->row_index][my_data->col_index] += my_data->row[i] * my_data->col[i];	
	pthread_exit(NULL);
}

int main() {
	int r1, c1, r2, c2;
	vector< vector<int> > m1, m2; 
	cout << "Enter the dimensions of the 1st matrix :- ";
	cin >> r1 >> c1;
	cout << "Enter the dimensions of the 2nd matrix :-";
	cin >> r2 >> c2;

	if (c1 != r2) {
		cout << "Matrices are not multiplication compatible" << endl;
		return 0;
	}
	m1.resize(r1 , vector<int>(c1 , 0));
	m2.resize(c2 , vector<int>(r2 , 0));
	result.resize(r1, vector<int>(c2 , 0));

	cout << "Enter the values of the 1st matrix :- " << endl;
	for (int i = 0; i < r1; i++)
		for (int j = 0; j < c1; j++)
			cin >> m1[i][j];


	cout << "Enter the values of the 2nd matrix :- " << endl;
	for (int i = 0; i < r2; i++)
		for (int j = 0; j < c2; j++)
			cin >> m2[j][i];


	int n_threads = r1 * c2;
	int thread_counter = 0;
	pthread_t threads[n_threads];
	struct thread_data td[n_threads];

	for (int i = 0; i < r1; i++) {
		for (int j = 0; j < c2; j++) {

			td[thread_counter].row_index = i;
			td[thread_counter].col_index = j;
			td[thread_counter].row = m1[i];
			td[thread_counter].col = m2[j];
			
			int rc = pthread_create(&threads[thread_counter], NULL, Multiply, (void *)&td[thread_counter]);
			if (rc) {
				cout << "Error:unable to create thread," << rc << endl;
				exit(-1);
			}
			thread_counter++;
		}
	}

	for (int i = 0; i < n_threads; i++)
		pthread_join(threads[i], NULL);
	
	cout << "The result matrix is :- " << endl;
	for (int i = 0; i < r1; i++) {
		for (int j = 0; j < c2; j++) {
			cout << result[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}