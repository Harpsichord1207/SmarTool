import logging

from .datetime import DTUtil
from .retry import retry

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


def hello():
    welcome_msg = "===== Hello, this is SmarTool! ====="
    print(welcome_msg)
    print(" Author: Harpsichord")
    print(" Email: tliu1217@163.com")
    print(" Install: pip install SmarTool")
    print(" Github: https://github.com/Harpsichord1207/SmarTool")
    print("=" * len(welcome_msg))
