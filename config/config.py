import os
from pathlib import Path


MODULE_PATH = Path(os.path.abspath(__file__)).parent.parent
RESULTS_PATH = os.path.join(MODULE_PATH, "results")
