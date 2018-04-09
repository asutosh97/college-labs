#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
//typedef priority_queue<Process>

class Process {
public:
    int id, burst_time, arrival_time, waiting_time, turn_around_time,time_left;
    // Process Constructor
    Process(int id, int burst_time,int arrival_time =  0, int waiting_time = 0, int turn_around_time = 0) {
      this -> id = id;
      this -> burst_time = burst_time;
      this -> arrival_time = arrival_time;
      this -> waiting_time = waiting_time;
      this -> turn_around_time = turn_around_time;
      this -> time_left = burst_time;
    }
};

struct comparator
{
    inline bool operator() (const Process& lhs, const Process& rhs)
    {
        return (lhs.time_left > rhs.time_left);
    }
};


void setQueue(priority_queue < Process,vector<Process>,comparator>& p,vector<Process>& vec,int timer) {
    for(auto i: vec) {
      if(i.arrival_time == timer) {
        p.push(i);
      }
    }
};

vector<Process> ShortestJobFirst(vector<Process>& vec) {
    /** Algorithm for shortest remaining time first
      * Input vector of processes
    **/
    vector<Process> result;
    priority_queue < Process,vector<Process>,comparator > p;
    setQueue(p,vec,0);
    int process_left = vec.size();
    int timer = 0;

    while(process_left) {
      int old_timer = timer;
      if (!p.empty()) {
        Process p1 = p.top();
        p.pop();
        timer += p1.time_left;
        p1.time_left = 0;

        p1.turn_around_time = timer - p1.arrival_time;
        p1.waiting_time = p1.turn_around_time - p1.burst_time;
        process_left--;
        result.push_back(p1);
      }
      else
        timer++;

      for (int i = old_timer + 1; i <= timer; i++)
        setQueue(p,vec,i);
    }
    return result;
}

int main() {
  Process p1(1,6,0);
  Process p2(2,8,0);
  Process p3(3,7,0);
  Process p4(4,3,0);
  vector<Process> vec;
  vec.push_back(p1);
  vec.push_back(p2);
  vec.push_back(p3);
  vec.push_back(p4);

  vector<Process> result = ShortestJobFirst(vec);

  for(auto i:result){
    cout << "pid :" << i.id << endl;
    cout << "Waiting Time :" << i.waiting_time << endl;
    cout << "Turn Around Time :" << i.turn_around_time << endl;
    //cout << "Waiting Time :" << i.waiting_time << endl;
  }
  return 0;
}