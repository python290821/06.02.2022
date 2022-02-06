import threading

# Singleton
# 1. cannot create more than 1 instances
# 2. when getting the object twice (or more) --> we will get the same object every time
# 3. when getting the object from two places at once it will work (later in course)

# hack the __init__

class MySingleton(object):
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance:
            return cls._instance
        # lock ----------------
        # t1, t2, t3 t4 t5 t6
        with cls._lock:
            if cls._instance is None: #t1 + t2
                cls._instance = cls.__new__(cls)
                cls._instance.name = 'itay'  # maybe from config
            return cls._instance

    def print_hello(self):
        print('hello')


sing1 = MySingleton.get_instance()
sing2 = MySingleton.get_instance()
print(sing1 == sing2)
print(sing1)
print(sing2)
print(sing1.name)
sing1.print_hello()
