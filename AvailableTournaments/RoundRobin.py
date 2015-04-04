#TODO: Implement

__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["William Ezekiel"]

# imports
from ServerPackage import Tournament
import random


class RoundRobin(Tournament.Tournament):
    """
    RoundRobin Tournament Type:
    For Large player counts. Divides players into groups and runs AllPlayAll on those groups
    """