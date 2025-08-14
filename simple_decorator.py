import logging
from functools import wraps

logging.basicConfig(
    filename='function-calls.log',
    format="%(levelname)s %(name)s %(asctime)s %(message)s",
    level=logging.DEBUG,
)


def log_calls(original_function):  # decorator

    @wraps(original_function)
    def _wrapper(*args, **kwargs):   # wrapper
        logging.debug(original_function.__name__)  # extra code
        return_value = original_function(*args, **kwargs)    # original function
        return return_value
    
    return _wrapper  # replaces original function

@log_calls
def spam(count):
    print("SPAM" * count)
# spam = log_calls(spam)

@log_calls
def ham():
    print("HAM")
# ham = log_calls(ham)

spam(4) # calling _wrapper(...)
spam(10) # same
ham()    # same