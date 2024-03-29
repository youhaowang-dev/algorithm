# process
1. features
2. traffic/QPS for each feature
3. availability and consistency
4. high level design
5. data flow for each feature
6. db table design
7. scale discussion
## features
Q: What features do we want to design in this meeting?  
A: feature1 and feature2  
Q: Can we assume we are only designing the backend of the features?  
A: yes/no  
## traffic
Q: What is the traffic for feature1/feature2?  
A: n per day/week/month  
## availability and consistency
Q: any requirement for data consistency and service availability?  
A: yes...  
Q: any addiitonal requirements we want to add? Otherwise, we can start the high level design  
## high level design
Let's do a high level design first. Then we can deep dive into the details.
APIs: create_xxx get_xxx  
Client<>Server<>Cache<>DB  
Client<>LB Cluster<>Server Cluster<>Cache Cluster<>DB Cluster  

## data flow
### Data flow for feature1:  
Client->Server: do something  
Server: do something  
Server->DB: save something  
Server->Client: return something  

## db table design
table_name_table  
id  PK  
uid FK  
...  

## scale discussion
cache, replica, sharding, consistent hashing...

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
* Use cases: Search engine indexing, Web archiving, Web mining, Web monitoring
* web crawler algorithm
  1. Given a set of URLs, download all the web pages addressed by the URLs. 
  2. Extract URLs from these web pages
  3. Add new URLs to the list of URLs to be downloaded. Repeat these 3 steps.
* Q and A
  * Candidate: What is the main purpose of the crawler? Is it used for search engine indexing, data mining, or something else?
  * Interviewer: Search engine indexing.
* characteristics of a good web crawler:
  * Scalability: The web is very large. There are billions of web pages out there. Web crawling should be extremely efficient using parallelization.
  * Robustness: The web is full of traps. Bad HTML, unresponsive servers, crashes, malicious links, etc. are all common. The crawler must handle all those edge cases.
  * Politeness: The crawler should not make too many requests to a website within a short time interval.
  * Extensibility: The system is flexible so that minimal changes are needed to support new content types. For example, if we want to crawl image files in the future, we should not need to redesign the entire system.
* flow
  * seed urls add to queue => DNS Resolver => download HTML => parser => dedup => add unvisited urls to queue => save content in db
* DNS Resolver
  * To download a web page, a URL must be translated into an IP address. The HTML Downloader calls the DNS Resolver to get the corresponding IP address for the URL. For instance, URL www.wikipedia.org is converted to IP address 198.35.26.96 as of 3/5/2019.
* DFS/BFS
  * DFS may cause frequent visits for the same domain
  * BFS won't hammer the domain but it does not consider priorities.
* Server-side rendering: Numerous websites use scripts like JavaScript, AJAX, etc to generate links on the fly. If we download and parse web pages directly, we will not be able to retrieve dynamically generated links. To solve this problem, we perform server-side rendering (also called dynamic rendering) first before parsing a page [12].
* Filter out unwanted pages: With finite storage capacity and crawl resources, an anti-spam component is beneficial in filtering out low quality and spam pages [13] [14].
* Database replication and sharding: Techniques like replication and sharding are used to improve the data layer availability, scalability, and reliability.
* Horizontal scaling: For large scale crawl, hundreds or even thousands of servers are needed to perform download tasks. The key is to keep servers stateless.

# Design Notification
* Q and A
  * Candidate: What types of notifications does the system support? 
  * Interviewer: Push notification, SMS message, and email.
  * Candidate: Is it a real-time system?
  * Interviewer: Let us say it is a soft real-time system. We want a user to receive notifications as soon as possible. However, if the system is under a high workload, a slight delay is acceptable.
  * Candidate: What are the supported devices?
  * Interviewer: iOS devices, android devices, and laptop/desktop.
  * Candidate: What triggers notifications?
  * Interviewer: Notifications can be triggered by client applications. They can also be scheduled on the server-side.
  * Candidate: Will users be able to opt-out?
  * Interviewer: Yes, users who choose to opt-out will no longer receive notifications.
  * Candidate: How many notifications are sent out each day?
  * Interviewer: 10 million mobile push notifications, 1 million SMS messages, and 5 million emails.
* flow
  * fanout server => message queue => ios/android/email servers => pull template from db and send notification
* Cache: User info, device info, notification templates are cached. 
* DB: It stores data about user, notification, settings, etc.
* Message queues: They remove dependencies between components. Message queues serve as buffers when high volumes of notifications are to be sent out. Each notification type is assigned with a distinct message queue so an outage in one third-party service will not affect other notification types.
* Reliability: We proposed a robust retry mechanism to minimize the failure rate.
* Security: AppKey/appSecret pair is used to ensure only verified clients can send notifications.
* Tracking and monitoring: These are implemented in any stage of a notification flow to capture important stats.
* Respect user settings: Users may opt-out of receiving notifications. Our system checks user settings first before sending notifications.
* Rate limiting: Users will appreciate a frequency capping on the number of notifications they receive.

# Design News Feed
* auth and rate limiting are enforced
* flow
  * client => server: get_feed()
  * server => db: query friend table to get all friend ids, then query post db to get all posts, aggregate all posts
  * server => client: return all posts
* pre-process to build new_feed table
  * news_feed_table: uid, post_id
  * pros: fast
  * cons: many writes if many followers, have delays, costs disk spaces, inactive users
* push posts in cache
  * pros: fast
  * cons: cache is limited resource

# Design Chat
* assume auth is done
* Q and A
  * Candidate: What kind of chat app shall we design? 1 on 1 or group based?
  * Interviewer: It should support both 1 on 1 and group chat.
* flow
  * user1 => server: send_message(uid2, message)
    * uid2 can be group_id for group message
  * server: save message in db
  * user2 => server: poll every n seconds get_message()
  * server => user2: return all messages
* issues
  * no ways to tell if a user is online
  * poll is not efficient because not always a user will have a message
* socket connection
  * bi-directional and persistent
  * design is simplified for 2-way connection
* message table
  * id, from_uid, to_uid, content, ctime
* group message table
  * id, from_uid, group_id, content, ctime
* message id should be unqiue and sortable
  * can use distributed ID generator
  * can also use local sequential ID as the group_id + sequential ID will be unique in the scope of the same group
* Online presence
  * An online presence indicator is an essential feature of many chat applications. Usually, you can see a green dot next to a user’s profile picture or username.
  * Periodically, an online client sends a heartbeat event to presence servers. If presence servers receive a heartbeat event within a certain time, say x seconds from the client, a user is considered as online. Otherwise, it is offline.
* Extend the chat app to support media files such as photos and videos. Media files are significantly larger than text in size. Compression, cloud storage, and thumbnails are interesting topics to talk about.
* End-to-end encryption. Whatsapp supports end-to-end encryption for messages. Only the sender and the recipient can read messages. Interested readers should refer to the article in the reference materials [9].
* Caching messages on the client-side is effective to reduce the data transfer between the client and server.
* Improve load time. Slack built a geographically distributed network to cache users’ data, channels, etc. for better load time [10].

# Design Location Based Service
* Examples: Uber, Lyft, Google Map
* geo hash: base32 to chunk world map recursively
  * longer hash == more accurate
* city data model: use a few geo hash points

# Design Booking System
* Examples: airbnb, hotel
* high level design
  * owner<>listing service<>inventory db
  * renter<>searching service<>search engine<>inventory db
  * renter<>reservation service<>[inventory db, reservation db, payment db] need transaction to ensure data consistency

# Design Typeahead (Autocomplete)
* Q and A:
  * Candidate: Is the matching only supported at the beginning of a search query or in the middle as well?
  * Interviewer: Only at the beginning of a search query.
  * Candidate: How many autocomplete suggestions should the system return?
  * Interviewer: 5
  * Candidate: How does the system know which 5 suggestions to return?
  * Interviewer: This is determined by popularity, decided by the historical query frequency.
  * Candidate: Does the system support spell check? 
  * Interviewer: No, spell check or autocorrect is not supported.
  * Candidate: Are search queries in English?
  * Interviewer: Yes. If time allows at the end, we can discuss multi-language support.
  * Candidate: Do we allow capitalization and special characters?
  * Interviewer: No, we assume all search queries have lowercase alphabetic characters.
* flow
  * aggregator server: use the data from analytic db to create a trie tree, save the the trie tree in db and push it to cache
  * query server: get all matches for the prefix from the trie tree, then return the top 5 frequent queries
    1. Find the prefix takes O(len(prefix))
    2. Find all queries takes O(node_count)
    3. Get top k takes O(node_count * logk)
    4. this result can be cached

* Trie DB. Trie DB is the persistent storage. Two options are available to store the data:
  * blob store: Since a new trie is built weekly, we can periodically take a snapshot of it, serialize it, and store the serialized data in the database.
  * Key-value store: A trie can be represented in a hash table form [4] by applying the following logic:
    * Every prefix in the trie is mapped to a key in a hash table.
    * Data on each trie node is mapped to a value in a hash table.
    * we can directly query from db if need to save cache
* when the trie grows too large to fit in one server
  * there are a lot more words that start with the letter ‘c’ than ‘x’. This creates uneven distribution.
  * do a data analysis, then shard by prefix
* Followup
  * Interviewer: How do you extend your design to support multiple languages?
  * To support other non-English queries, we store Unicode characters in trie nodes. If you are not familiar with Unicode, here is the definition: “an encoding standard covers all the characters for all the writing systems of the world, modern and ancient” [5].
  * Interviewer: What if top search queries in one country are different from others?
  * In this case, we might build different tries for different countries. To improve the response time, we can store tries in CDNs.
  * Interviewer: How can we support the trending (real-time) search queries?
  * Assuming a news event breaks out, a search query suddenly becomes popular. Our original design will not work because:
    * Offline workers are not scheduled to update the trie yet because this is scheduled to run on weekly basis.
    * Even if it is scheduled, it takes too long to build the trie.

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

## Isolation Levels from low to high
* Read Uncommitted: Can read data when other Transactions are writing/reading
* Read Committed: Can only read after another Transaction finished commit
* Repeatable Read: Cannot write after another Transaction reads the data
* Serializable: Cannot read/write when another Transaction locks the data
* MySQL default=Repeatable Read, Oracle default=Read Committed
* 
| Isolation Level  | Issues                                        |
| ---------------- | --------------------------------------------- |
| Read Uncommitted | phantom read, non-repeatable read, dirty read |
| Read Committed   | phantom read, non-repeatable read             |
| Repeatable Read  | phantom read                                  |
| Serializable     | no inconsistency                              |


* NOTE: All isolation levels do not allow Dirty Write.
* Dirty Write
  * Time: [-------------------------------------------------------->]
  * T1:   [Read X=1				Write X=3 Rollback X=1]
  * T2:   [Read X=1 Write X=2 Commit X=2]
  * The rollback of T1 rollbacks the submission of T2. 
  * All isolation levels do not allow Dirty Write.

* Dirty Read
  * Time: [-------------------------------------------------------->]
  * T1: [Read X=1 Write X=2 			Rollback X=1]
  * T2:	[                   Read X=2                ]
  * The rollback of T1 causes T2 to read the uncommitted X=2.
  * Read Uncommitted will cause dirty reads.
  * Increasing isolation level to Read Committed can avoid dirty reads.
* Non-repeatable Read
  * Reads get different values for a same transaction.
  * Time: [-------------------------------------------------------->]
  * T1:   [Read X=1 						         Read X=2]
  * T2:   [         Read X=1 Write X=2 Commit X=2]
  * T1 is still being executed and T2 submitted. Two reads of T1 have different results, so the reads are not repeatable.
  * Read Committed isolation level can cause Non-repeatable Reads. Increasing the isolation level to Repeatable Read can fix this problem.
* Phantom Reads
  * Time: [-------------------------------------------------------->]
  * T1:   [Read(x<5)=[1,2,3]			    Read(x<5)=[1,2,3,4]]
  * T2:	  [	                Insert 4 Commit]
  * 1,2,3 are locked for write by Repeatable Read, but 4 can still be inserted. 
  * Phantom Reads can happen for non-determined multi-row reads like range query. Repeatable Road only locks determined rows.
  * Repeatable Read allows Phantom Read. Increase isolation level to Serializable to avoid this.

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