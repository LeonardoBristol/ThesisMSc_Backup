import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. PEPTIDE RMSD COMPARISON
# ============================================================

# <<< CHANGE FILE NAMES HERE IF NEEDED
rmsd_job1 = np.loadtxt("peptide_rmsd9.dat")
rmsd_job2 = np.loadtxt("peptide_rmsd63.dat")

plt.figure(figsize=(8, 5))

plt.plot(
    rmsd_job1[:, 0],
    rmsd_job1[:, 1],
    lw=2,
    label="Job9"
)

plt.plot(
    rmsd_job2[:, 0],
    rmsd_job2[:, 1],
    lw=2,
    label="Job63"
)

plt.xlabel("Frame")
plt.ylabel("Peptide RMSD (Å)")
plt.title("Peptide RMSD Comparison")

plt.legend()

plt.tight_layout()
plt.savefig("rmsd_comparison.png", dpi=300)
plt.close()


# ============================================================
# 2. COM DISTANCE COMPARISON
# ============================================================

# <<< CHANGE FILE NAMES HERE IF NEEDED
com_job1 = np.loadtxt("com_distance9.dat")
com_job2 = np.loadtxt("com_distance63.dat")

plt.figure(figsize=(8, 5))

plt.plot(
    com_job1,
    lw=2,
    label="Job9"
)

plt.plot(
    com_job2,
    lw=2,
    label="Job63"
)

plt.xlabel("Frame")
plt.ylabel("COM Distance (Å)")
plt.title("Peptide-Receptor COM Distance")

plt.legend()

plt.tight_layout()
plt.savefig("com_comparison.png", dpi=300)
plt.close()


# ============================================================
# 3. HYDROGEN BOND COMPARISON
# ============================================================

# <<< CHANGE FILE NAMES HERE IF NEEDED
hb_job1 = np.loadtxt("hbonds_count9.dat")
hb_job2 = np.loadtxt("hbonds_count63.dat")

plt.figure(figsize=(8, 5))

plt.plot(
    hb_job1,
    lw=2,
    label="Job9"
)

plt.plot(
    hb_job2,
    lw=2,
    label="Job63"
)

plt.xlabel("Frame")
plt.ylabel("Number of H-bonds")
plt.title("Peptide-Receptor Hydrogen Bonds")

plt.legend()

plt.tight_layout()
plt.savefig("hbonds_comparison.png", dpi=300)
plt.close()

# ============================================================
# 4. APO TM3-TM6 DISTANCE COMPARISON
# ============================================================

# <<< CHANGE FILE NAMES HERE IF NEEDED
tm3tm6_apo1 = np.loadtxt("tm3_tm6_distanceApo9.dat")
tm3tm6_apo2 = np.loadtxt("tm3_tm6_distance9.dat")

plt.figure(figsize=(8, 5))

plt.plot(
    tm3tm6_apo1,
    lw=2,
    label="Apo 9"
)

plt.plot(
    tm3tm6_apo2,
    lw=2,
    label="Job9"
)

plt.xlabel("Frame")
plt.ylabel("TM3-TM6 Distance (Å)")
plt.title("Job 9 TM3-TM6 Distance")

plt.legend()

plt.tight_layout()
plt.savefig("tm3tm6_Job9_comparison.png", dpi=300)
plt.close()


# ============================================================
# 5. APO TM3-TM6 DISTANCE COMPARISON
# ============================================================

# <<< CHANGE FILE NAMES HERE IF NEEDED
tm3tm6_apo1 = np.loadtxt("tm3_tm6_distanceApo63.dat")
tm3tm6_apo2 = np.loadtxt("tm3_tm6_distance63.dat")

plt.figure(figsize=(8, 5))

plt.plot(
    tm3tm6_apo1,
    lw=2,
    label="Apo 63"
)

plt.plot(
    tm3tm6_apo2,
    lw=2,
    label="Job63"
)

plt.xlabel("Frame")
plt.ylabel("TM3-TM6 Distance (Å)")
plt.title("Job 63 TM3-TM6 Distance")

plt.legend()

plt.tight_layout()
plt.savefig("tm3tm6_Job63_comparison.png", dpi=300)
plt.close()


print("All comparison plots generated successfully.")
