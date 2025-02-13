# code-utils

## This is work in progress.

## Install requirements

Using virtualenv we can create and install the requirements.

Create virtual environment.

`virtualenv utils-env`

Install dependencies.
`pip install -r requirements.txt`

Activate environment.
`source utils-env/bin/activate`


### Add environment variable with path to connectedhomeip directory.

Example `export MATTER_BASE_PATH=/Users/<youruser>/workspace/connectedhomeip`

## Using the script 
### Run the python steps generator from the yaml file using.

Example:

`python generate_steps_from_yaml.py --test Test_TC_MOD_1_2.yaml`

Output example:

```
PICSNAMES:MOD.S
TESTNAME is:80.2.1. [TC-MOD-1.2] Cluster attributes with DUT as Server
Found 7 steps in the yaml file.
TestStep(1, "Commission DUT to TH (can be skipped if done in a preceding test)."),
TestStep(1, "TH reads the SupportedModes attribute from DUT"),
TestStep(2, "TH reads the CurrentMode attribute from the DUT"),
TestStep(3, "TH reads the OnMode attribute from the DUT"),
TestStep(4, "TH reads the StartUpMode attribute from the DUT"),
TestStep(5, "TH reads the Description attribute from the DUT"),
TestStep(6, "TH reads the StandardNamespace attribute from the DUT")
```

### Copy the steps from the cmd:

`python generate_steps_from_yaml.py --test Test_TC_MOD_1_2.yaml  -v  | grep TestStep | pbcopy`

### Copy PICS values
`python generate_steps_from_yaml.py --test Test_TC_MOD_1_2.yaml  -v  | grep PICS | cut -d ':' -f 2 | tr -d '\n'  | pbcopy`

### Copy Testname
`python generate_steps_from_yaml.py --test Test_TC_MOD_1_2.yaml  -v  | grep TESTNAME | cut -d ':' -f 2 | tr -d '\n' | pbcopy`

