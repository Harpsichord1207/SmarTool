import logging
import functools
import time

logger = logging.getLogger('SmarTool')


def retry(func=None, /, *, times=5, delay=2, catch_error=None, ignore_error=None):

    times = int(times)
    delay = float(delay)

    def wrapper(fun):
        @functools.wraps(fun)
        def inner(*args, **kwargs):
            count = 0
            while 1:
                try:
                    return fun(*args, **kwargs)
                except Exception as e:
                    logger.warning(f'Failed to run function {func.__name__}({func}), error: {e}')
                    count += 1
                    if count == times:
                        raise
                    time.sleep(delay)
        return inner

    if func is None:
        return wrapper
    elif callable(func):
        return wrapper(func)
    else:
        raise ValueError(f'Value {func} is not callable')
