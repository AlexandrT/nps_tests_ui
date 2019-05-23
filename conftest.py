import sys
import os
import pytest
import logging

from lib.config import set_env


LOG_NAME = 'test.log'

logging.basicConfig(filename=LOG_NAME,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filemode='w')

logger = logging.getLogger('ui_site')

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))

logger.info(f"Tests runs on the {set_env()} environment")
