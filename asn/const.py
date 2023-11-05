import os
import pathlib
import time
import uuid

TRUE_CUR_PATH = os.path.dirname(__file__)
TRUE_CUR_PATH = TRUE_CUR_PATH if TRUE_CUR_PATH != "" else "."

# TRUE_CUR_PATH = pathlib.Path.cwd()

pl_TRUE_CUR_PATH = pathlib.Path(TRUE_CUR_PATH)
BASE_PATH = pl_TRUE_CUR_PATH.parent
DATA_PATH = BASE_PATH / 'data'

# Check the auto root path is correct
try:
    assert BASE_PATH.name == "accelerate-sf-notifications"
except Exception as e:
    print("Base dir should be something like ....../accelerate-sf-notifications/: ", BASE_PATH)
    print("Important! Ensure TRUE_CUR_PATH is your working directory:", TRUE_CUR_PATH)
    print("Exception:", e)
