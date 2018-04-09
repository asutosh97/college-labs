#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
//typedef priority_queue<Process>

int greater(int a,int b) {
    return a > b;
}

class Process {
public:
    int id, burst_time, arrival_time, waiting_time, turn_around_time, time_left, priority_value;
    // Process Constructor
    Process(int id, int burst_time,int arrival_time =  0, int waiting_time = 0, int turn_around_time = 0) {
      this -> id = id;
      this -> burst_time = burst_time;
      this -> arrival_time = arrival_time;
      this -> waiting_time = waiting_time;
      this -> turn_around_time = turn_around_time;
      this -> time_left = burst_time;
      this -> priority_value = 0;
    }
};


struct comparator
{
    inline bool operator() (const Process& lhs, const Process& rhs)
    {
        return (lhs.priority_value > rhs.priority_value);
    }
};


void setQueue(priority_queue < Process,vector<Process>, comparator >& p,vector<Process>& vec,int timer, int &priority_counter) {
    for(auto i: vec) {
      if(i.arrival_time == timer) {
        i.priority_value = ++priority_counter;
        p.push(i);
      }
    }
};

vector<Process> RR(vector<Process>& vec, int tq) {
    /** Algorithm for shortest remaining time first
      * Input vector of processes
    **/
    vector<Process> result;
    int priority_counter = 0;
    int timer = 0;
    priority_queue < Process,vector<Process>, comparator > p;
    setQueue(p, vec, timer, priority_counter);
    int process_left = vec.size();


    while(process_left) {
      int old_timer = timer;

      if (!p.empty()) {
        Process p1 = p.top();
        p.pop();
        
        int min_time = min(tq, p1.time_left);
        p1.time_left = p1.time_left - min_time;
        timer += min_time;

        for (int i = old_timer + 1; i <= timer; i++)
          setQueue(p,vec, i, priority_counter);

        if(p1.time_left == 0){
          p1.turn_around_time = timer - p1.arrival_time;
          p1.waiting_time = p1.turn_around_time - p1.burst_time;
          process_left--;
          result.push_back(p1);
        }
        else {
          p1.priority_value = ++priority_counter;
          p.push(p1);
        }
      }
      else {
        timer++;
        for (int i = old_timer + 1; i <= timer; i++)
          setQueue(p,vec, i, priority_counter);
      }
      // Update priority queue
    }
    return result;
}

int main() {
  Process p1(1,5,5);
  Process p2(2,6,4);
  Process p3(3,7,3);
  Process p4(4,9,1);
  Process p5(5,2,2);
  Process p6(6,3,6);

  vector<Process> vec;
  vec.push_back(p1);
  vec.push_back(p2);
  vec.push_back(p3);
  vec.push_back(p4);
  vec.push_back(p5);
  vec.push_back(p6);

  int tq = 3;
  vector<Process> result = RR(vec, tq);

  for(auto i:result){
    cout << "pid :" << i.id << endl;
    cout << "Waiting Time :" << i.waiting_time << endl;
    cout << "Turn Around Time :" << i.turn_around_time << endl;
    //cout << "Waiting Time :" << i.waiting_time << endl;
  }
  return 0;
}