* combination
  * can reuse same num/index but cannot restart at 0
  * use start_index or start_num
  * dedup: use hash table to count the num_to_count
* permutation
  * cannot reuse same num/index but can restart at 0
  * use hashset for used index
  * dedup: use hash table to count the num_to_count
* subset
  * cannot reuse same num/index and cannot restart at 0