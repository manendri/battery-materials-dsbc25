from ase.io import read, write
import os

data_path = os.path.join('..','..','data','QMOF','qmof_database','qmof_database')
cif_path = os.path.join(data_path, 'relaxed_structures')
cifs = os.listdir(cif_path)
cifs.sort()
print(cifs)

refcodes = []
mofs = []
for cif in cifs:
	refcodes.append(cif.split('.cif')[0])
	mofs.append(read(os.path.join(cif_path, cif)))
	
write(os.path.join(data_path,'relaxed_structures.xyz'), mofs)

with open(os.path.join(data_path,'refcodes.csv'),'w') as w:
	for refcode in refcodes:
		if refcode == refcodes[-1]:
			w.write(refcode)
		else:
			w.write(refcode+',')
