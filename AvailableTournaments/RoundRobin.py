#TODO: Implement

__author__ = "Paul Council, Anand Patel"
__version__ = "sprint1"
__credits__ = ["William Ezekiel"]

# imports
from ServerPackage.Tournament import *
import random


class RoundRobin(Tournament):
    """
    RoundRobin Tournament Type:
    For Large player counts. Divides players into groups and runs AllPlayAll on those groups
    """