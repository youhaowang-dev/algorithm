# hash map
See DesignHashMap.py

# lru cache
See LRUCache.py

# call center
class WorkerStatus(Enum):
    OK = 1
    BUSY = 2
class WorkerBase:
    def __init__(self, id, name, type):
        self.status = WorkerStatus.OK
    def start_call():
    def end_call():
    def transfer_call():
class Worker1(WorkerBase):
class Worker2(WorkerBase):
class Worker3(WorkerBase):
class CallCenter:
    def __init__(self):
        # load workers from db
        self.workers = 
        self.calls_queue = deque()
        self.start_work()

    def add_worker():
    def remove_worker():
    def update_worker():

    def dispatch_call():
        if self.has_available_worker():

    def start_work():
        # create scheduler to call dispatch_call every N seconds

    def end_work():
        # delete scheduler

