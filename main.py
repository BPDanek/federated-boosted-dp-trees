from experiments.replication_experiments.experiment_replicator import ExperimentReplicator

import os
os.chdir('/home/bdanek2/federated-boosted-dp-trees/')

e = ExperimentReplicator()
e.replicate(2, overwrite=False)