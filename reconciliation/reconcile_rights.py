import pandas as pd
from datetime import datetime

# Load the data
df_tracks = pd.read_csv("data/tracks.csv")
df_rights = pd.read_csv("data/rights.csv")

# Convert date columns to datetime
df_rights["valid_from"] = pd.to_datetime(df_rights["valid_from"])
df_rights["valid_to"] = pd.to_datetime(df_rights["valid_to"])

# Set today's date
today = pd.to_datetime(datetime.today().date())

# -----------------------------
# 1. Expired Rights
# -----------------------------
expired_rights = df_rights[df_rights["valid_to"] < today]
print(f"\n❌ Expired Rights Found: {len(expired_rights)}")
print(expired_rights[["track_id", "owner_name", "valid_to"]].head())

# -----------------------------
# 2. Tracks with Missing Rights
# -----------------------------
tracks_with_rights = set(df_rights["track_id"])
all_tracks = set(df_tracks["track_id"])
missing_rights = all_tracks - tracks_with_rights

print(f"\n⚠️ Tracks Missing Rights: {len(missing_rights)}")
print(list(missing_rights)[:5])  # show first 5

# -----------------------------
# 3. Tracks with Overlapping Rights Windows
# -----------------------------
def has_overlap(group):
    group = group.sort_values(by="valid_from")
    for i in range(len(group) - 1):
        if group.iloc[i+1]["valid_from"] < group.iloc[i]["valid_to"]:
            return True
    return False

overlapping_tracks = []

for track_id, group in df_rights.groupby("track_id"):
    if len(group) > 1 and has_overlap(group):
        overlapping_tracks.append(track_id)

print(f"\n🔁 Tracks with Overlapping Rights Windows: {len(overlapping_tracks)}")
print(overlapping_tracks[:5])  # show first 5

# -----------------------------
# Summary
# -----------------------------
print("\n✅ Reconciliation Complete.")
