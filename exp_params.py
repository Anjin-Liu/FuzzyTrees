"""
@author: Zhaoqing Liu
@email : Zhaoqing.Liu-1@student.uts.edu.au
@date  : 21/4/21 11:58 am
@desc  :
"""
import multiprocessing
from enum import Enum


class ComparisionMode(Enum):
    NAIVE = "my_naive_vs_sklearn_naive"
    FF3 = "ff3_vs_naive"  # With only Feature Fuzzification, conv_k=3
    FF4 = "ff4_vs_naive"  # With only Feature Fuzzification, conv_k=4
    FF5 = "ff5_vs_naive"  # With only Feature Fuzzification, conv_k=5
    FUZZY = "fcart_vs_ccart"
    BOOSTING = "fgbdt_vs_nfgbdt"
    MIXED = "mfgbdt_vs_nfgbdt"


# The maximum number of available CPU cores per cluster.
# For example, the maximum number of available CPU cores per Mars cluster is 16 for UTS,
# 30 for each Laureate cluster, 26 for each Mercury cluster, and 8 for each Venus cluster.
# You should check the maximum number of CPU cores available for the other clusters.
NUM_CPU_CORES = multiprocessing.cpu_count()

# The datasets' names on which you want to run experiments.
DATASET_NAMES = ["Vehicle", "German_Credit", "Diabetes", "Iris", "Wine"]