import numpy as np

from ose_utils.testing.auxiliary import fresh_directory


def create_regression_vault(func_evaluate_request, func_generate_request, num_tests):
    tests = []
    for _ in range(num_tests):
        request = func_generate_request()
        rslt = func_evaluate_request(request)
        tests.append((request, rslt))
    return tests


# TODO: SEED is a bad name in the utils library as it might well be an init file
@fresh_directory
def check_regression_vault(func, num_tests, vault):
    for i, test in enumerate(vault[:num_tests]):
        seed, rslt = test
        np.testing.assert_equal(func(seed), rslt)
