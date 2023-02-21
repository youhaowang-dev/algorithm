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

Let's desgin for single server first. Then we can use other techniques to handle bigger traffics.

Client=>Server=>DB
Client=>LB Cluster=>Server Cluster=>Cache Cluster=>DB Cluster

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
    * When checking by day, round the timestamp to hour, so 24 reads.
    * When checking by hour, round the timestamp to minute, so 60 reads.
    * What if we still want to know the exact time?
    * Save the HHMMSS, HHMM, HH for each log
    * sum(HH, HHMM, HHMMSS) requires less than 200 cache reads.

# Desgin Key Value Store
* hash table
* A lot of data need to be evenly distributed to different dbs.
  * use consistent hashing
* hot data push to cache, rest stay in db
* Replication is for high availability and consistency.

# Design Unique ID Generator
* UUID
  * pros: simple, no need to handle distributed system
  * cons: 128 bits long, cannot be sorted by time, not numeric
* Sequential ID from one server
  * pros: sorted numeric IDs, work for small medium scale
  * cons: single point of failure
* Twitter snowflake approach
  * Sign bit + Timestamp + Datacenter ID + Machine ID + Sequence ID
  * Sign bit: 1 bit. It will always be 0. This is reserved for future uses. It can potentially be used to distinguish between signed and unsigned numbers.
  * Timestamp: 41 bits. Milliseconds since the epoch or custom epoch. We use Twitter snowflake default epoch 1288834974657, equivalent to Nov 04, 2010, 01:42:54 UTC.
  * Datacenter ID: 5 bits, which gives us 2 ^ 5 = 32 datacenters.
  * Machine ID: 5 bits, which gives us 2 ^ 5 = 32 machines per datacenter.
  * Sequence number: 12 bits. For every ID generated on that machine/process, the sequence number is incremented by 1. The number is reset to 0 every millisecond.
* Clock synchronization. In our design, we assume ID generation servers have the same clock. This assumption might not be true when a server is running on multiple cores. The same challenge exists in multi-machine scenarios. Solutions to clock synchronization are out of the scope of this book; however, it is important to understand the problem exists. Network Time Protocol is the most popular solution to this problem. For interested readers, refer to the reference material [4].
* Section length tuning. For example, fewer sequence numbers but more timestamp bits are effective for low concurrency and long-term applications.
* High availability. Since an ID generator is a mission-critical system, it must be highly available.

# Design URL Shortener
* hash table
* read
  * client=>server: get_long(short_url)
  * server=>db: find long url
  * server=>client: redirect to long_rul
* write
  * client=>server: get_short(long_url)
  * server=>db: hash the long_url to short, save in db
  * server=>client: return short_url
* 26*2 + 10 = 62 available chars, so 62^6=56B is enough
* hash
  * md5 suffix can have conflict, we can retry to resolve
  * Base62 <=> auto incremental ID
    * 62^6 * n + 62^5 * n + ... + 62^0 * n = auto incremental ID
* 301/302
  * 301: moved permanently, so the browser caches the response
  * 302: moved temporarily, no cache
  * Each redirection method has its pros and cons. If the priority is to reduce the server load, using 301 redirect makes sense as only the first request of the same URL is sent to URL shortening servers. However, if analytics is important, 302 redirect is a better choice as it can track click rate and source of the click more easily.
* Rate limiter: A potential security problem we could face is that malicious users send an overwhelmingly large number of URL shortening requests. Rate limiter helps to filter out requests based on IP address or other filtering rules. If you want to refresh your memory about rate limiting, refer to “Chapter 4: Design a rate limiter”.
* Web server scaling: Since the web tier is stateless, it is easy to scale the web tier by adding or removing web servers.
* Database scaling: Database replication and sharding are common techniques.
* Analytics: Data is increasingly important for business success. Integrating an analytics solution to the URL shortener could help to answer important questions like how many people click on a link? When do they click the link? etc.

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



## CAP theorem
* CAP theorem states it is impossible for a distributed system to simultaneously provide more than two of these three guarantees: consistency, availability, and partition tolerance. 
* Consistency: consistency means all clients see the same data at the same time no matter which node they connect to.
* Availability: availability means any client which requests data gets a response even if some of the nodes are down.
* Partition Tolerance: a partition indicates a communication break between two nodes. Partition tolerance means the system continues to operate despite network partitions.

## Consistency models
* Consistency model is other important factor to consider when designing a key-value store. A consistency model defines the degree of data consistency, and a wide spectrum of possible consistency models exist:
* Strong consistency: any read operation returns a value corresponding to the result of the most updated write data item. A client never sees out-of-date data.
* Weak consistency: subsequent read operations may not see the most updated value.
* Eventual consistency: this is a specific form of weak consistency. Given enough time, all updates are propagated, and all replicas are consistent.
* Strong consistency is usually achieved by forcing a replica not to accept new reads/writes until every replica has agreed on current write. This approach is not ideal for highly available systems because it could block new operations. Dynamo and Cassandra adopt eventual consistency, which is our recommended consistency model for our key-value store. From concurrent writes, eventual consistency allows inconsistent values to enter the system and force the client to read the values to reconcile. The next section explains how reconciliation works with versioning.