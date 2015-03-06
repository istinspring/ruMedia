import os
import sys


DEBUG = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


DB_NAME = 'ruMedia'
