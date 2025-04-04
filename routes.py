from flask import Blueprint, jsonify
import pandas as pd
from datetime import datetime
import os

catalog_routes = Blueprint('catalog', __name__)

# ✅ Load data safely
try:
    tracks = pd.read_csv("data/tracks.csv")
    rights = pd.read_csv("data/rights.csv")

    rights["valid_from"] = pd.to_datetime(rights["valid_from"])
    rights["valid_to"] = pd.to_datetime(rights["valid_to"])
    today = pd.to_datetime(datetime.today())  # ✅ FIXED: convert to datetime64[ns]

except Exception as e:
    print("❌ Error loading data:", e)
    tracks, rights, today = None, None, None

# ✅ Expired Rights
@catalog_routes.route('/catalog/tracks/expired', methods=['GET'])
def expired_rights():
    try:
        expired = rights[rights["valid_to"] < today]
        return jsonify(expired.to_dict(orient="records")), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Missing Rights
@catalog_routes.route('/catalog/tracks/missing-rights', methods=['GET'])
def missing_rights():
    try:
        track_ids = set(tracks["track_id"])
        rights_ids = set(rights["track_id"])
        missing = list(track_ids - rights_ids)
        return jsonify(missing), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Overlapping Rights
@catalog_routes.route('/catalog/tracks/overlapping-rights', methods=['GET'])
def overlapping_rights():
    try:
        overlapping = []
        for track_id, group in rights.groupby("track_id"):
            group = group.sort_values("valid_from")
            for i in range(len(group) - 1):
                if group.iloc[i+1]["valid_from"] < group.iloc[i]["valid_to"]:
                    overlapping.append(track_id)
                    break
        return jsonify(overlapping), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
