"""
@author: Zhaoqing Liu
@email : Zhaoqing.Liu-1@student.uts.edu.au
@date  : 21/4/21 11:29 am
@desc  :
"""
import multiprocessing
import os
import time
from decimal import Decimal

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold

from fuzzy_trees.fuzzy_decision_tree import FuzzyDecisionTreeClassifier
from fuzzy_trees.fuzzy_decision_tree_proxy import FuzzificationParams, FuzzyDecisionTreeProxy, CRITERIA_FUNC_CLF, \
    CRITERIA_FUNC_REG
from fuzzy_trees.fuzzy_gbdt import FuzzyGBDTClassifier
from fuzzy_trees.util_data_processing_funcs import extract_fuzzy_features
import fuzzy_trees.util_plotter as plotter


if __name__ == '__main__':
    print("Main Process (%s) started." % os.getpid())
    # Record the start time used to calculate the time spent running one experiment.
    time_start = time.time()

    # Specify the names of all the datasets on which the model is being trained.
    # dataset_name_list = ["Vehicle", "German_Credit", "Diabetes", "Iris", "Wine"]
    ds_name_list = ["Iris"]

    # Create a FDT proxy, and do the pretraining via it.
    clf = FuzzyDecisionTreeProxy(fdt_class=FuzzyDecisionTreeClassifier, disable_fuzzy=False,
                                 fuzzification_params=FuzzificationParams(),
                                 criterion_func=CRITERIA_FUNC_CLF["gini"], max_depth=5)
    clf.pretrain_fuzzy_clf(ds_name_list=ds_name_list, conv_k_lim=(2, 3, 1), fuzzy_reg_lim=(0, 1.0, 0.01))

    # Show the fuzzy regulation coefficient versus training error and test error by the FDT proxy.
    clf.plot_fuzzy_reg_vs_err()

    print("Total elapsed time: {:.5}s".format(time.time() - time_start))
    print("Main Process (%s) ended." % os.getpid())

