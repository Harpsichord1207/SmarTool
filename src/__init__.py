import logging

from .retry import retry

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


def hello():
    print("== Hello, this is SmarTool! ==")
