from enum import Enum


class GetAccountInvoicesStatus(Enum):
    """An enumeration representing different categories.

    :cvar PAID: "PAID"
    :vartype PAID: str
    """

    PAID = "PAID"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, GetAccountInvoicesStatus._member_map_.values())
        )
