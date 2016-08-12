import os


def compress(path):
    """

    :param path:
    :return: the return value of tar
    """
    pass


def uncompress(path):
    """
    It make use of the tar to uncompress file(s)
    **\*nix only**
    :param path:
    :return: the return value of tar
    """
    return os.system("tar -xf %s" % path)
