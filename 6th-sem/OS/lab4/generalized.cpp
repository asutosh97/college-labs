#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


int greater(int a,int b) {
    return a > b;
}

class Process {
public:
    int id, burst_time, arrival_time, waiting_time, turn_around_time, time_left, rr_priority, priority_value;
    // Process Constructor
    Process(int id, int burst_time, int arrival_time =  0, int priority_value = 0, int waiting_time = 0, int turn_around_time = 0) {
      this -> id = id;
      this -> burst_time = burst_time;
      this -> arrival_time = arrival_time;
      this -> waiting_time = waiting_time;
      this -> turn_around_time = turn_around_time;
      this -> time_left = burst_time;
      this -> rr_priority = 0;
      this -> priority_value = priority_value;
    }
};


struct comparator
{
    inline bool operator() (const Process& lhs, const Process& rhs)
    {
        /*
        for FCFS     --> arrival_time
        for SJF      --> burst_time
        for SRTF     --> time_left
        for Priority --> priority_value
        for RR       --> rr_priority
        */
        return (lhs.priority_value > rhs.priority_value);
    }
};

void insert_to_pq(priority_queue < Process,vector<Process>, comparator >& p, Process _p, int &priority_counter) {
  _p.rr_priority = ++priority_counter;
  p.push(_p);
}

void setQueue(priority_queue < Process,vector<Process>, comparator >& p, vector<Process>& vec,int timer, int &priority_counter) {
    for(auto i: vec) {
      if(i.arrival_time == timer) {
        insert_to_pq(p, i, priority_counter);
      }
    }
}

vector<Process> generalized(vector<Process>& vec, int tq, bool pre_emptive) {

    vector<Process> result;
    int priority_counter = 0;
    int timer = 0;
    priority_queue < Process,vector<Process>, comparator > p;
    
    //  initialize pqueue with processes arrived at t = 0
    setQueue(p, vec, timer, priority_counter);
    
    int process_left = vec.size();

    while(process_left) {

      //  if pqueue is not empty
      if (!p.empty()) {

        Process p1 = p.top();
        p.pop();
        
        //  if non-preemptive, run till completion, else run till minimum of time quantum and time left
        int run_time = pre_emptive? min(tq, p1.time_left) : p1.time_left;
        p1.time_left = p1.time_left - run_time;
        int old_timer = timer;
        timer += run_time;

        //  add the processes that have come while p1 was executed to the pqueue
        for (int i = old_timer + 1; i <= timer; i++)
          setQueue(p, vec, i, priority_counter);

        //  if p1 completed, add it to result
        if(p1.time_left == 0){
          p1.turn_around_time = timer - p1.arrival_time;
          p1.waiting_time = p1.turn_around_time - p1.burst_time;
          process_left--;
          result.push_back(p1);
        }
        //  if p1 not completed, insert it to pqueue again
        else {
          insert_to_pq(p, p1, priority_counter);
        }
      }
      //  if pqueue is empty, time lapse 1 unit and add the newly arrived processes
      else {
        timer++;
        setQueue(p,vec, timer, priority_counter);
      }
    }
    return result;
}

int main() {

  Process p1(1,11,0,2);
  Process p2(2,28,5,0);
  Process p3(3,2,12,3);
  Process p4(4,10,2,1);
  Process p5(5,16,9,4);
  vector<Process> vec;
  vec.push_back(p1);
  vec.push_back(p2);
  vec.push_back(p3);
  vec.push_back(p4);
  vec.push_back(p5);

  int tq = 1;
  
  bool pre_emptive = false;
  vector<Process> result = generalized(vec, tq, pre_emptive);

  for(auto i:result){
    cout << "pid :" << i.id << endl;
    cout << "Waiting Time :" << i.waiting_time << endl;
    cout << "Turn Around Time :" << i.turn_around_time << endl;
    //cout << "Waiting Time :" << i.waiting_time << endl;
  }
  return 0;
}