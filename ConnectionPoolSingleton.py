import threading
from MyConnection import *

class ConnectionPoolSingleton(object):
    _instance = None
    _lock = threading.Lock()
    _max_connections = 20

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance:
            return cls._instance
        cls._lock.acquire()
        try:
            if cls._instance is None: #t1 + t2
                cls._instance = cls.__new__(cls)
                cls._instance.connections = [MyConnection(i) for i in range(cls._max_connections)]
        finally:
            cls._lock.release()
        return cls._instance


