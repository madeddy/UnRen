#!/usr/bin/env python2

"""
This is a wrapper app around tools for the works with RenPy files. It provides multiple
functionality through a simple text menu.


Requirements: python 3.6+

import os
import sys
import argparse
import tempfile
import pickle
import base64
import textwrap



__title__ = 'UnRen'
__license__ = 'Apache-2'
__author__ = 'F95sam, madeddy'
__status__ = 'Development'
__version__ = 'vers_placeholder'


# TODO: Placeholder: On completition of the python 3 version the code needs to be
# copied over and adjusted for python 2.7
def main():
    """This executes all program steps.
    """
    if not sys.version_info[:2] == (2, 7):
        raise Exception("Must be executed in Python 2.7.x but not 3.x or later.\n"
                        "You are running {}".format(sys.version))

if __name__ == '__main__':
    main()
