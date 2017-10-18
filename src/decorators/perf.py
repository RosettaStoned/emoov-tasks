import time
from src.decorators import log

def performance(filename):

    def decorator(func):
        func_name = func.__name__

        def new_func(*args, **kwargs):

            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            total = end - start

            @log.log(filename, msg=total, name=func_name)
            def __log():
                return result 

            return __log()


        new_func.__name__ = func_name
        return new_func

    return decorator

