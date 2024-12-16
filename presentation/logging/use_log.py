# An example application to do some automated logging of script activity

from datetime import datetime

def track_calls(func):
    def wrapper(*args, **kwargs):
        with open('function_log.txt', 'a') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[{timestamp}] Calling {func.__name__} with args: {args}, kwargs: {kwargs}\n")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Usage
@track_calls
def my_function(x, y,default="TRUE"):
    return x + y

my_function(1, 2,default="false")
my_function(x=3, y=4)

