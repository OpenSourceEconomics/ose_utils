import datetime
from ose_utils.testing.auxiliary import fresh_directory


@fresh_directory
def run_robustness_tests(func_evaluate_request, func_generate_request, hours):
    stop = datetime.datetime.now() + datetime.timedelta(hours=hours)
    while datetime.datetime.now() < stop:
        func_evaluate_request(func_generate_request())

