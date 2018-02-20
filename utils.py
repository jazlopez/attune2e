from colorama import Fore
from colorama import init


def __init__():

    """
    Init colorama for util functions

    :return:
    """

    init(autoreset=True)


def error(message):

    """
    Log an error to standard output

    :param message
    :return
    """

    print(Fore.RED + '[ X ] {}'.format(message))


def log(of, out, message):

    """
    Log a successfully performed action

    :param of:
    :param out:
    :param message:
    :return:
    """

    print(Fore.BLUE + "[ \u2713 ] {}/{} {}".format(of, out, message))