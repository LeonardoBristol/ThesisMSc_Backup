import json
import glob
import os
import pandas as pd

results = []

folders = glob.glob("af2_job_*")

for folder in folders:

    # Find score file
    score_files = glob.glob(os.path.join(folder, "*scores_rank_001*.json"))

    if not score_files:
        continue

    score_file = score_files[0]

    with open(score_file) as f:
        data = json.load(f)

    # Extract scores
    iptm = data.get("iptm", None)

    # Some versions store plddt differently
    plddt_list = data.get("plddt", [])
    plddt_mean = sum(plddt_list)/len(plddt_list) if plddt_list else None

    results.append({
        "job": folder,
        "iptm": iptm,
        "plddt": plddt_mean
    })

# Create table
df = pd.DataFrame(results)

# Rank by interaction strength
df = df.sort_values(by="iptm", ascending=False)

print(df)

# Save results
df.to_csv("af2_ranking.csv", index=False)
