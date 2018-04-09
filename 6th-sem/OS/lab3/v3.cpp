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

void baseSchedulingAlgo(vector<Process>& vec, bool pre_emptive, string parameter) {
    /** Algorithm for shortest remaining time first
      * Input vector of processes
    **/
    
    auto comparator  = [&](const Process& lhs, const Process& rhs)
    {
      if (parameter == "time_left")
        return (lhs.time_left > rhs.time_left);
      else
        return (lhs.arrival_time > rhs.arrival_time);
    };

    auto setQueue = [](priority_queue < Process,vector<Process>, comparator >& p,vector<Process>& vec,int timer) {
      for(auto i: vec) {
        if(i.arrival_time == timer) {
          p.push(i);
        }
      }
    };

    priority_queue < Process,vector<Process>, comparator > p;
    setQueue(p,vec,0);
    int process_left = vec.size();
    int timer = 0;

    while(process_left) {
      Process p1 = p.top();
      p.pop();
      p1.time_left = p1.time_left - 1;
      timer += 1;
      if(p1.time_left == 0 ){
        p1.turn_around_time = timer - p1.arrival_time;
        p1.waiting_time = p1.turn_around_time - p1.burst_time;
        process_left--;
        vec.push_back(p1);
      } else {
        p.push(p1);
      }

      // Update priority queue
      setQueue(p,vec,timer);
    }
}

void ShortestRemainingTimeFirst(vector<Process> &vec) {
  baseSchedulingAlgo(vec, true, "time_left");
}

int main() {
  Process p1(1,8,0);
  Process p2(2,4,1);
  Process p3(3,9,2);
  Process p4(4,5,3);
  vector<Process> vec;
  vec.push_back(p1);
  vec.push_back(p2);
  vec.push_back(p3);
  vec.push_back(p4);

  ShortestRemainingTimeFirst(vec);

  for(auto i:vec){
    cout << "pid :" << i.id << endl;
    cout << "Waiting Time :" << i.waiting_time << endl;
    cout << "Turn Around Time :" << i.turn_around_time << endl;
    //cout << "Waiting Time :" << i.waiting_time << endl;
  }
  return 0;
}