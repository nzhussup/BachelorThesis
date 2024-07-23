import time
from functools import wraps

def time_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Record start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.perf_counter()  # Record end time
        execution_time = round(end_time - start_time,2)  # Calculate execution time
        return result, execution_time  # Return the result and execution time
    return wrapper
