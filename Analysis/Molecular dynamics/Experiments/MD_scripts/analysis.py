import matplotlib.pyplot as plt
import MDAnalysis as mda
from MDAnalysis.analysis import rms, align
import numpy as np

u = mda.Universe("step5_input.psf", "step7_production.dcd")

# receptor only
receptor = u.select_atoms("protein and name CA")

# Align all frames on receptor
align.AlignTraj(
    u,
    u,
    select="protein and name CA",
    in_memory=True
).run()

# 7. TM3 TM6 distance
TM3_START, TM3_END = 89, 110  # your DeepTMHMM boundaries
TM6_START, TM6_END = 231, 247  # your DeepTMHMM boundaries

tm3_helix = receptor.select_atoms(f"resid {TM3_START}:{TM3_END} and name CA")
tm6_helix = receptor.select_atoms(f"resid {TM6_START}:{TM6_END} and name CA")

tm3_tm6_dist = []
for ts in u.trajectory:
    tm3_tm6_dist.append(np.linalg.norm(
        tm3_helix.center_of_mass() - tm6_helix.center_of_mass()))
np.savetxt("tm3_tm6_distanceApo9.dat", np.array(
    tm3_tm6_dist))      # HERE YOU CHANGE THE NAME
