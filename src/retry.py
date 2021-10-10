# -*- coding: utf-8 -*-

import logging
import functools
import time

logger = logging.getLogger('SmarTool')


# 参考py38新语法, "/"前的参数严格遵守位置, 且不会提示出来
def retry(func=None, /,  times=5, delay=2, catch_error=None, ignore_error=None):

    times = int(times)
    delay = float(delay)
    catch_error = _check_error_parameter(catch_error)
    ignore_error = _check_error_parameter(ignore_error)

    if catch_error and ignore_error:
        logger.warning("Both catch error and ignore error provided, only use catch error!")
        ignore_error = []

    def wrapper(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            count = 0
            while 1:
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    # 如果传入了需要retry的catch_error且实际发生的error不属于其中，则直接raise
                    if catch_error and not _check_raised_error(e, catch_error):
                        raise
                    # 如果传入了不需要retry的ignore_error且实际发生的error属于其中，则直接raise
                    if ignore_error and _check_raised_error(e, ignore_error):
                        raise

                    count += 1
                    logger.warning(f'Failed to run function "{f.__name__}", retry {times-count}, error: {e}')
                    if count == times:
                        raise
                    time.sleep(delay)
        return inner

    if func is None:
        return wrapper
    elif callable(func):
        return wrapper(func)
    else:
        raise ValueError(f'Invalid parameter: {func} is not callable')


def _check_error_parameter(errors):
    if errors is None:
        return []
    elif isinstance(errors, (list, tuple)):
        for error in errors:
            _check_error_parameter(error)
        return list(errors)
    elif issubclass(errors, Exception):
        return [errors]
    else:
        raise ValueError(f'Invalid parameter "{errors}", must be Exception/List[Exception]/Tuple[Exception]')


def _check_raised_error(error, error_list):
    for e in error_list:
        if isinstance(error, e):
            return True
    return False
