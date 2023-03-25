      #include<bits/stdc++.h>

using namespace std;




int main(){
      map<char, vector<char>> graph;
      
      graph['A'] = {'B' , 'M' , 'L'};
      graph['B'] = {'k' , 'T'};
      graph['M'] = {'F' , 'C'};
      graph['L'] = {'F'};
      graph['C'] = {'N' , 'K'};
      graph['F'] = {'M' , 'C' , 'N'};
      graph['T'] = {'K' , 'E'};
      graph['K'] = {'Z' , 'E'};     
      graph['Z'] = {'N'};
      graph['N'] = {'K'};
      graph['E'] = {'='};

      vector<char> path;
      set<char> discoverd;

      stack<char> visit;
      visit.push('A');

      while(!visit.empty()){
            char current = visit.top();    visit.pop();
            bool visited = discoverd.find(current) != discoverd.end(); // check if the current node already discoverd
            
            if (visited) continue;
            cout<<current<<"-->";
            for(auto i : graph[current]){
                  if (i == '=') {
                        cout<<"EXIT\n";
                        return 0 ;
                  }
                  visit.push(i);
            }

            discoverd.emplace(current);
      }

}


