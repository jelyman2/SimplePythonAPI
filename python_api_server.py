""" Python API Server
"""

import os
from endpoints.interface.simple import Server

s = Server()
s.serve_forever()
