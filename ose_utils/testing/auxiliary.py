import random
import string
import shutil
import os


def fresh_directory(func):

    # TODO: Maybe we could use a context manager here.
    def wrapper_fresh_directory(*args, **kwargs):

        dirname = get_testdir()

        os.mkdir(dirname)
        os.chdir(dirname)

        func(*args, **kwargs)

        os.chdir('../')

        shutil.rmtree(dirname)

    return wrapper_fresh_directory


def get_testdir(length=6):
    """ This function creates a random string that is used as the testing
    subdirectory.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

