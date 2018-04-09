/*
Program to calculate sum upto n using k threads.
*/

#include <iostream>
#include <cstdlib>
#include <pthread.h>

using namespace std;

struct thread_data {
	int beg, end, sum;
};

void *PrintHello(void *threadarg) {
   struct thread_data *my_data;
   my_data = (struct thread_data *) threadarg;

   for (int i = my_data->beg; i <= my_data->end; i++)
   	my_data->sum += i;
   
   pthread_exit(NULL);
}

int main () {
   int rc;
   int n, n_threads;

   cout << "Enter the amount to be summed to :- ";
   cin >> n;

   cout << "Enter the number of threads :- ";
   cin >> n_threads;

   int range = n / n_threads;
   pthread_t threads[n_threads];
   struct thread_data td[n_threads];

   for(int i = 0; i < n_threads; i++ ) {
      td[i].beg = i * range + 1;
      td[i].end = (i + 1) * range;
      td[i].sum = 0;

      rc = pthread_create(&threads[i], NULL, PrintHello, (void *)&td[i]);
      
      if (rc) {
         cout << "Error:unable to create thread," << rc << endl;
         exit(-1);
      }

   }

   for (int i = 0; i < n_threads; i++)
   	pthread_join(threads[i], NULL);

   int sum = 0;
   for (int i = 0; i < n_threads; i++) {
   	sum += td[i].sum;
   }
   cout << "sum = " << sum << endl;
   pthread_exit(NULL);

}


/*
REFERENCES :-

for thread_creation :- https://www.tutorialspoint.com/cplusplus/cpp_multithreading.htm
for synchronization :- http://www.cs.cmu.edu/afs/cs/academic/class/15492-f07/www/pthreads.html

*/