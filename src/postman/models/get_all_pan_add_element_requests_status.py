<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from enum import Enum


class GetAllPanAddElementRequestsStatus(Enum):
    """An enumeration representing different categories.

    :cvar PENDING: "pending"
    :vartype PENDING: str
    :cvar DENIED: "denied"
    :vartype DENIED: str
    """

    PENDING = "pending"
    DENIED = "denied"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                GetAllPanAddElementRequestsStatus._member_map_.values(),
            )
        )
