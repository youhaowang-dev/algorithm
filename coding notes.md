* combination
  * can reuse same num/index but cannot restart at 0
  * use start_index or start_num
  * dedup: use hash table to count the num_to_count
  * i+1 if not want to reuse, i if want to reuse
* permutation
  * cannot reuse same num/index but can restart at 0
  * use hashset for used index
  * dedup: use hash table to count the num_to_count
  * i+1 if not want to reuse, i if want to reuse
* subset
  * cannot reuse same num/index and cannot restart at 0
  * no dedup is needed for unique input
  * dedup: use hash table to count the num_to_count
  * i+1 if not want to reuse, i if want to reuse
* graph search
  * bfs use queue, get neighbors, validate neighbors, add neighbors to queue
  * dfs use stack/recursion, get neighbors, validate neighbors, add neighbors to stack/recursion calls
  * topological sort, need graph and node_to_indegree, enqueue 0 indegree node and repeat with node_to_indegree[node] -= 1