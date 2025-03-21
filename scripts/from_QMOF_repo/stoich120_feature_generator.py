from matminer.featurizers.composition import Meredig
from ase.io import read
from pymatgen.io import ase as pm_ase
import numpy as np
import pandas as pd
import os

# Settings
data_path = os.path.join('..','..','data','QMOF','qmof_database','qmof_database')
xyz_path = os.path.join(data_path,'relaxed_structures.xyz') # list of appended XYZs (length N)
refcodes_path = os.path.join(data_path,'refcodes.csv') # list of refcodes (length N)

#---------------------------------------
# Read in structures
ase_mofs = read(xyz_path, index=':')
refcodes = np.genfromtxt(refcodes_path, delimiter=',', dtype=str)
adaptor = pm_ase.AseAtomsAdaptor()
pm_mofs = [adaptor.get_structure(ase_mof) for ase_mof in ase_mofs]

# Initialize feature object
featurizer = Meredig()
features = featurizer.feature_labels()
df = pd.DataFrame(columns=features)

# Get features
for i, pm_mof in enumerate(pm_mofs):
	print('Generating fingerprint: '+str(i))
	fingerprint = featurizer.featurize(pm_mof.composition)
	refcode = refcodes[i]
	df.loc[refcode, :] = fingerprint

# Export features
df.index.name = 'MOF'
df.to_csv(os.path.join(data_path,'stoich120_fingerprints.csv'), index=True)
