import yaml
import re
import argparse
from os import environ

# This variable is the path to your matter base directory at connectedhomeip
base_path = environ.get('MATTER_BASE_PATH')
if not base_path:
    print("MATTER_BASE_PATH is not defined as env variable")
    exit(1) 

certification_test_path = f"{base_path}/src/app/tests/suites/certification"
yaml_file = None
not_steps = []
steps_list = []

parser = argparse.ArgumentParser(prog="Matter test utils",description="Some utils",epilog="Some text")
parser.add_argument("-t","--test")
parser.add_argument("-v","--verbose",action='store_true')

args = parser.parse_args()
if args.test is None:
    print("No test provided")
    exit(1)

test_case = args.test
path = f"{certification_test_path}/{test_case}"

try:
    with open(path,'r') as yl:
        yaml_file = yaml.safe_load(yl)
except yaml.YAMLError as err:
    print(str(err))
    exit(1)
except FileNotFoundError as nf:
    print("Ouch:",str(nf))
    exit(1)
if args.verbose:
    print(f"Found yaml file at {path}.")
test_steps =  yaml_file['tests']
reg = re.compile(r"^\d+$")
flag = 1

# print the pics
pics = yaml_file['PICS']
for pic in pics:
    print(f"PICSNAMES:{pic}")
# print name
print(f"TESTNAME is:{yaml_file['name']}")

steps_size = 0
parsed_steps = []
for step in test_steps:
    label = step['label']

    if 'step' in str(label).lower():
        steps_size += 1
        label_arr = label.split(":",1)
        step_str = label_arr[0]
        label = label_arr[1].strip()

        step_number = step_str.split("Step")[1].strip()
        is_number = reg.match(step_number)
        code_step = ""
        if is_number is None:
            code_step = f"TestStep(\"{step_number}\", \"{label}\")"
        else:
            code_step = f"TestStep({step_number}, \"{label}\")"
        parsed_steps.append(code_step)
    else:
        # This is not a steps but something else
        continue

if args.verbose:
    print(f"Found {steps_size} steps in the yaml file.")

if steps_size == 0:
    print(f"No steps found at file: {path}")
    exit(1)

# Print the steps
for step_n,code_step in enumerate(parsed_steps,start=1):
    if step_n < steps_size:
        print(f"{code_step},")
    else:
        print(code_step)
print("Completed!!")
