#!/usr/bin/env python
# Python Startup file for repls

import os, sys, inspect, platform, site, pathlib
from pprint import pprint

Path = pathlib.Path

__file__ = "/home/carlc/ubucode/my-new-py-proj/pystartupfile.py"
__file2__ = Path(os.environ.get('PYTHONSTARTUP'))

print(f'{__file__} has been loaded')
print(f'{__file2__} is the file too')
