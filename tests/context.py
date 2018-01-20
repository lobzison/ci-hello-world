"""
Context for correct imports
"""

import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../ci-hello-world')))

import ci_hello_world
