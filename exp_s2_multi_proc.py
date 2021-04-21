"""
@author: Zhaoqing Liu
@email : Zhaoqing.Liu-1@student.uts.edu.au
@date  : 21/4/21 11:53 am
@desc  :
"""
import multiprocessing

from exp_s2 import exec_exp_clf
from exp_params import ComparisionMode, DATASET_NAMES, NUM_CPU_CORES

if __name__ == '__main__':
    # Create a pool containing n processes. Make sure that n is <= the number of CPU cores available.
    # The parameters to the Pool indicate how many parallel processes are called to run the program.
    # The default size of the Pool is the number of compute cores on the CPU, i.e. multiprocessing.cpu_count().
    pool = multiprocessing.Pool(NUM_CPU_CORES)

    # Complete all tasks by the pool.
    # !!! NB: If you want to complete the experiment faster, you can use distributed computing. Or you can divide
    # the task into k groups to execute in k py programs, and then run one on each of k clusters simultaneously.
    for ds_name in DATASET_NAMES:
        # Add a process into the pool. apply_async() is asynchronous equivalent of "apply()" builtin.
        pool.apply_async(exec_exp_clf, args=(ComparisionMode.BOOSTING, ds_name))
    pool.close()
    pool.join()



    # 2nd method: using multiprocessing.Process purely, not multiprocessing.Pool.
    # # Create more than 2 Worker processes (the main is the Master processes), and each process execute
    # # an experiment on one dataset.
    # # NB: Make sure that the total number "n" of processes is less than the number of cores of CPU,
    # # e.g. in a server Mars, n < 14.
    # p1 = multiprocessing.Process(target=exec_exp_clf, args=(ComparisionMode.BOOSTING, DatasetName.VEHICLE))
    # p2 = multiprocessing.Process(target=exec_exp_clf, args=(ComparisionMode.BOOSTING, DatasetName.GERMAN_CREDIT))
    # p3 = multiprocessing.Process(target=exec_exp_clf, args=(ComparisionMode.BOOSTING, DatasetName.DIABETES))
    # p4 = multiprocessing.Process(target=exec_exp_clf, args=(ComparisionMode.BOOSTING, DatasetName.IRIS))
    # p5 = multiprocessing.Process(target=exec_exp_clf, args=(ComparisionMode.BOOSTING, DatasetName.WINE))
    #
    # # Start all processes.
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    #
    # # Join all processes to the system resource request queue.
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
