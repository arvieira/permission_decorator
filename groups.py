from enum import Enum

from permissions import Permissions


class Groups(Enum):
    estoquista = [Permissions.edit_item, Permissions.move_item, Permissions.split_item]
    financeiro = [Permissions.fisco_view, Permissions.buy]
