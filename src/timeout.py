# -*- coding: utf-8 -*-
import functools
import signal
import sys


class TimeoutException(Exception):

    def __init__(self, func_name, timeout_):
        self.func_name = func_name
        self.timeout = timeout_

    def __str__(self):
        return f'Function {self.func_name} timeout after {self.timeout}s'


def timeout(func=None, /,  seconds=5):

    if sys.platform == 'win32':
        raise NotImplementedError('Timeout Not support win32 platform currently.')

    seconds = int(seconds)

    def wrapper(f):

        def handler(signum, frame):
            raise TimeoutException(f.__name__, seconds)

        @functools.wraps(f)
        def inner(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                return f(*args, **kwargs)
            except Exception:
                raise
            finally:
                signal.signal(signal.SIGALRM, signal.SIG_IGN)

        return inner

    if func is None:
        return wrapper
    elif callable(func):
        return wrapper(func)
    else:
        raise ValueError(f'Invalid parameter: {func} is not callable')
