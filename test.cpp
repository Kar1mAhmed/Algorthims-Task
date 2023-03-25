#include <bits/stdc++.h>

using namespace std;

void build(int key, vector<int> &track, map<int, int> &G, int n, vector<vector<int>> &ans)
{
      if (key == n)
      {
            ans.push_back(track);
            return;
      }

      vector<int> taker;
      for (auto i : G[key])
      {
            track.push_back(i);
            taker = track;
            build(i, taker, G, n, ans);
            trak.pop_back();
      }

      int main()
      {
            int graph[]
            map<int, int> G;
            vector<vector<int>> ans;
            for (auto i : graph)
                  G[i[0]] += i[1];
            int n = G.rbegin()->first;
            vector<int> track;

            build(0, track, G, n, ans);

            return ans;
      }