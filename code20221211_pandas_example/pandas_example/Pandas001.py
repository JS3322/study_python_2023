"""
link :
pandas class
"""

import math


class Pandas001:
    """
    pandas 관련 주석
    """
    def __init__(self, var1, var2):
        self.data001 = math.sqrt(var1)
        self.data002 = math.sqrt(var2)

    def get_data001(self):
        return self.data001

    def set_data001(self, var1):
        self.data001 = var1
