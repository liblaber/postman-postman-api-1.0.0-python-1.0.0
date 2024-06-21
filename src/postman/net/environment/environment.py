"""
An enum class containing all the possible environments for the SDK
"""

from enum import Enum


class Environment(Enum):
    """The environments available for the SDK"""

    DEFAULT = "https://api.getpostman.com"
    US = "https://api.getpostman.com"
    EU = "https://api.eu.postman.com"
