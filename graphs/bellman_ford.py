# bellman ford is single source shortest path algo
# not ideal, worst time complexity than dijkstra
# Djikstra will fail with negative cycles, bellman can detect them


#### Set every node in dist to infinity same as djikstra
### Set first node to dist[s] = 0
### Relax each edge V-1 times


### We just run the algo 2 times, if after first iteration there is any change
### in dist value of any node we can say that node is in negative cycle
## ideal no. of iterations will be V-1 to check if negative cycle impact is properly propagated
