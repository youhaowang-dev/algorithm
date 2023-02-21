# ask questions
Q: What features do we want to design in this meeting?
A: feature1 and feature2
Q: Can we assume we are only designing the backend of the features?
A: yes/no
Q: What is the traffic for feature1/feature2?
A: n per day/week/month
Q: any requirement for data consistency and service availability?
A: yes...
Q: any addiitonal requirements we want to add? Otherwise, we can start the high level design

# Design Consistent Hashing
* inconsistent hashing
  * id % 100 db shards
  * this requires moving a lot of data between shards if shard add/remove
* consistent hashing
  * use a range as a hashing ring [0, 2^31]
  * evenly distribute db_ids on the ring
    * hash(id) belongs to db_id that is the smallest number greater than it
    * Use Red-Black Tree(balanced binary search tree) to search db_id.
  * for uneven data distribution
    * each db_id can have some virtual db_ids, more nodes==more even
    * {db_id: [1,99,375,888...]}

# Design Rate Limiter
* can be in both client and server sides
  * client side cannot be trusted
* limiting algorithms
  * tokens to limit the rate and refill tokens
    * pros: easy to impl, less memory usage, can handle burst of traffic
    * cons: bucket size and refill rate need to be adjusted
  * sliding window log
    * {timestamp1: 2, timestamp2: 1, timestamp2: 0}
    * Remove stale timestamps for new request.
    * If the sum count < limit, add the timestamp with count of 1.
    * if not add the timestamp with count of 0.
    * pros: very accurate. In any rolling window, requests will not exceed the rate limit.
    * cons: consumes a lot of memory because even if a request is rejected, its timestamp might still be stored in memory

* Checking a day will have 86400 memcached reads. How to reduce it?

When checking by day, round the timestamp to hour, so 24 reads.
When checking by hour, round the timestamp to minute, so 60 reads.
What if we still want to know the exact time?
Save the HHMMSS, HHMM, HH for each log
sum(HH, HHMM, HHMMSS) requires less than 200 cache reads.


# Desgin Key Value Store

# Design Unique ID Generator

# Design URL Shortener

# Design Web Crawler

# Design Notification

# Design News Feed

# Design Chat

# Design Location Based Service
* Examples: Uber, Lyft, Google Map

# Design Booking System
* Examples: Airbnb, Hotel

# Design Typeahead (Autocomplete)

# Design Youtube

# Design Google Drive

# Design Data Dog

# Latency Best Practices
* Memory is fast but the disk is slow.
* Avoid disk seeks if possible.
* Simple compression algorithms are fast.
* Compress data before sending it over the internet if possible.
* Data centers are usually in different regions, and it takes time to send data between them.

# Important Concepts
Cache

