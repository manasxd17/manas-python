import functools
from time import time

def timer(function):
    @functools.wraps(function)
    def wrapper():
        start_time = time()
        func = function()
        end_time = time()
        runtime = end_time - start_time
        print(f"Time taken:{runtime:.8f} seconds")
        return func
    return wrapper

@timer
def Table():
    return (10000000000000  ** 200)
    
print(Table())
    
        
