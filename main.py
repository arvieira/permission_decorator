from groups import Groups
from permission_manager import has_perm
from permissions import Permissions

from user import User

# andre é o request.user
andre = User(Groups.estoquista)


@has_perm(andre, Permissions.buy)
def view():
    print('Beleza')


if __name__ == '__main__':
    view
