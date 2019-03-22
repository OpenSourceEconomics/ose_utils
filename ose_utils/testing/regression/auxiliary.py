import numpy as np

from ose_utils.testing.auxiliary import fresh_directory


def create_regression_vault(func, num_tests):
    tests = []
    for i, seed in enumerate(range(num_tests)):
        rslt = func(seed)
        tests.append((seed, rslt))
    return tests


@fresh_directory
def check_regression_vault(func, num_tests, vault):
    for i, test in enumerate(vault[:num_tests]):
        seed, rslt = test
        np.testing.assert_equal(func(seed), rslt)
