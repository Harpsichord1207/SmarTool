import logging

from .datetime import DTUtil
from .retry import retry
from .timeout import TimeoutException, timeout

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


def hello():
    welcome_msg = "===== Hello, this is SmarTool! ====="
    print(welcome_msg)
    print(" Author: Harpsichord")
    print(" Email: tliu1217@163.com")
    print(" Install: pip install SmarTool")
    print(" Github: https://github.com/Harpsichord1207/SmarTool")
    print("=" * len(welcome_msg))


__all__ = [retry.__name__, hello.__name__, timeout.__name__, TimeoutException.__name__]
