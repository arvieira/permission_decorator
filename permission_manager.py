from permissions import Permissions


def has_perm(*args, **kwargs):
    def wrapper(func):
        if args[1] in args[0].group.value:
            func()
        else:
            print('Você não tem permissão')

    return wrapper
