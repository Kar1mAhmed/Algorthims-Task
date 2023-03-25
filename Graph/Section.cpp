#include <bits/stdc++.h>

using namespace std;

int main(){
    priority_queue<int> p;
    vector<vector<int>> g;

    char goal = 'g';
    char current_node = 'A';

    bool reached  = false;
    int total_cost = 0;

    vector<char> path;

    while(!reached){
        int min_cost = 9999999;
        char next_node;
        for(auto neighbor : current_node){
            if (neighbor.cost < min_cost){
                next_node = neighbor;
                min_cost = neighbor.cost;
            }
        }
        path.push_back(current_node);
        current_node = next_node;
        if (current_node == goal) reached = true;
    }


}

int x = 1 while x < 8 x++ int main == 30 while 30 < 20 do main-- print(x) cout<<hl<<endl

.while 
    .if
        .do
            
        .
    .
.   