from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        print('args: ',args)
        print('kwargs: ',kwargs)
        result = func(*args, **kwargs)
        print('result of function: ',result)
        return result
    return with_logging

@logit
def addition_func(x,y):
   """Do some math."""
   return x + y

if __name__ == '__main__':
    result = addition_func(4,5)
    print("result: ",result)

