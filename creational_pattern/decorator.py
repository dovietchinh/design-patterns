from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        print('args: ',args)
        print('kwargs: ',kwargs)
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x,y):
   """Do some math."""
   return x + y

result = addition_func(4,5)
result = addition_func(6,7)
print(result)

