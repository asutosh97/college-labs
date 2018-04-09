#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class Process {
public:
	string name;
	int arrival_time;
	int burst_time;
	
	friend bool operator < (const Process& lhs, const Process& rhs) {
		return lhs.arrival_time < rhs.arrival_time;
	}
    
    friend bool operator > (const Process& lhs, const Process& rhs) {
		return lhs.arrival_time > rhs.arrival_time;
	}

	Process(string name, int arrival_time, int burst_time): name(name), arrival_time(arrival_time), burst_time(burst_time) {

	}

};

struct comparator
{
    inline bool operator() (const Process& lhs, const Process& rhs)
    {
        return (lhs.arrival_time > rhs.arrival_time);
    }
};

int main() {
	vector<Process> processVector =
    {
       	Process("Process 1", 3, 1),
        Process("Process 2", 1, 2),
        Process("Process 3", 4, 3),
        Process("Process 4", 5, 4),
        Process("Process 5", 2, 5)
    };

    cout << "======== Less Priority Queue ======= " << endl;

    priority_queue<Process, vector<Process>, less<vector<Process>::value_type> > pqueue_less;

    //fill pqueue_less
    for (auto it = processVector.cbegin(); it!=processVector.cend(); it++)
    {
        pqueue_less.push(*it);
    }

    //iterate,display and pop
    while (!pqueue_less.empty())
    {
        Process value = pqueue_less.top();
        cout << value.name << endl;
        pqueue_less.pop();
    }
    //	idle op:- p2, p5, p1, p3, p4

    cout << endl << endl;

    
    cout << "======== Greater Priority Queue ======= " << endl;

     priority_queue<Process, vector<Process>, greater<vector<Process>::value_type> > pqueue_greater;

    //fill pqueue_less
    for (auto it = processVector.cbegin(); it!=processVector.cend(); it++)
    {
        pqueue_greater.push(*it);
    }

    //iterate,display and pop
    while (!pqueue_greater.empty())
    {
        Process value = pqueue_greater.top();
        cout << value.name << endl;
        pqueue_greater.pop();
    }
    cout << endl << endl;
	
    cout << "======== Custom Priority Queue ======= " << endl;

    priority_queue<Process, vector<Process>, comparator > pqueue_custom;

    //fill pqueue_less
    for (auto it = processVector.cbegin(); it!=processVector.cend(); it++)
    {
        pqueue_custom.push(*it);
    }

    //iterate,display and pop
    while (!pqueue_custom.empty())
    {
        Process value = pqueue_custom.top();
        cout << value.name << endl;
        pqueue_custom.pop();
    }
    //	idle op:- p2, p5, p1, p3, p4

    cout << endl << endl;

	return 0;
}