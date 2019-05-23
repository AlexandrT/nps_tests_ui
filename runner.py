import subprocess
import argparse
import os


class LangAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        os.environ["TEST_LANG"] = values
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser(description="Run ui-tests")
parser.add_argument("--language", action=LangAction, help="Select localization")

args = parser.parse_args()

pytest_run_arr = ['py.test', 'tests/', '-vv', '-l', \
        '--html=reports/report.html', '--self-contained-html', '--driver', 'Chrome']

tests_proc = subprocess.run(pytest_run_arr)

if tests_proc.returncode != 0:
    raise Exception('Some tests is failed.')
