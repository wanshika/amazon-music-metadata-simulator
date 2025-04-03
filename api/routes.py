from flask import Blueprint, jsonify
import pandas as pd
from datetime import datetime

catalog_routes = Blueprint('catalog', __name__)

# Load data
tracks = pd.read_csv("data/tracks.csv")
rights = pd.read_csv("data/rights.csv")

# Convert to datetime
rights["valid_from"] = pd.to_datetime(rights["valid_from"])
rights["valid_to"] = pd.to_datetime(rights["valid_to"])
today = pd.to_datetime(datetime.today().date())

# 1. Expired Rights
@catalog_routes.route('/tracks/expired', methods=['GET'])
def expired_rights():
    expired = rights[rights["valid_to"] < today]
    return jsonify(expired.to_dict(orient="records")), 200

# 2. Missing Rights
@catalog_routes.route('/tracks/missing-rights', methods=['GET'])
def missing_rights():
    track_ids = set(tracks["track_id"])
    rights_ids = set(rights["track_id"])
    missing = list(track_ids - rights_ids)
    return jsonify(missing), 200

# 3. Overlapping Rights
@catalog_routes.route('/tracks/overlapping-rights', methods=['GET'])
def overlapping_rights():
    overlapping = []
    for track_id, group in rights.groupby("track_id"):
        group = group.sort_values("valid_from")
        for i in range(len(group) - 1):
            if group.iloc[i+1]["valid_from"] < group.iloc[i]["valid_to"]:
                overlapping.append(track_id)
                break
    return jsonify(overlapping), 200
