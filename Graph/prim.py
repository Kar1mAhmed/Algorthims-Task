def mst_find(G, s):
      cost = [float("inf")] * len(G) # setting the cost to infinite so it be ready for the compare 
      cost[s] = 0
      itr = [False] * len(G)
      c = 0
      while True: #checking the minimum cost for the moment
            min_weight = float("inf")
            m_idx = -1
            for i in range(len(G)): # looking for all edges of node
                  if itr[i] == False:
                        if cost[i] < min_weight: 
                              min_weight = cost[i] # setting minimum to current cost
                              m_idx = i
            if m_idx == -1: # no more to visit
                  break
            c += min_weight # adding the current minimum
            itr[m_idx] = True
            for i, j in G[m_idx].items():
                  cost[i] = min(cost[i], j)
      return c


def solve(n, edges, s):
      graph = {i: {} for i in range(n)} # building the graph
      for item in edges:
            u = item[0]
            v = item[1]
            w = item[2]
            u -= 1
            v -= 1
            try: # testing if no connection
                  min_weight = min(graph[u][v], w)
                  graph[u][v] = min_weight
                  graph[v][u] = min_weight
            except KeyError:
                  graph[u][v] = w
                  graph[v][u] = w
      return mst_find(graph, s)


print(solve(4, [(1, 2, 5), (1, 3, 5), (2, 3, 7), (1, 4, 4)], 3))
