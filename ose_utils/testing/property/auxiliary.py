import importlib
import datetime
import inspect
import pkgutil
import shutil
import os

from ose_utils.testing.auxiliary import get_testdir


def get_property_tests(package):
    tests = list()
    for _, modname, _ in pkgutil.iter_modules([package.__path__[0]+"/tests"]):
        module = importlib.import_module(package.__package__ + '.'+"tests"+"." + modname)
        for func in inspect.getmembers(module, inspect.isfunction):
            if 'test_' not in func[0]:
                continue
            tests.append(func)
    if tests == []:
        raise Exception("test import doesnt work")
    return tests


def run_property_tests(package, minutes):
    tests = get_property_tests(package)

    stop = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    while datetime.datetime.now() < stop:

        for test in tests:

            dirname = get_testdir()

            os.mkdir(dirname)
            os.chdir(dirname)

            test[1]()

            os.chdir('../')

            shutil.rmtree(dirname)
